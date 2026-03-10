import logging
from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from app.dependecies.dependency import require_login
from service.llm_service import classify_question, llm_answer
from service.nlp_utils import extract_course, data_filter, contains_warning
from service.intents import choose_query
from constants_utils.cons_utils import VALID_INTENTS
from crud.questions_crud import save_question

logger = logging.getLogger(__name__)

router = APIRouter()
templates = Jinja2Templates(directory="static/html")


@router.get("/ask")
def ask_page(request: Request, user_id=Depends(require_login)):
    return templates.TemplateResponse(
        "ask.html",
        {"request": request}
    )


@router.post("/ask")
def ask_ai(
    request: Request,
    question: str = Form(...),
    user_id=Depends(require_login)
):

    filtered = data_filter(question)

    if not filtered:
        answer = "Invalid question format."

    else:
        word_count = len(filtered.split())

        if word_count < 3:
            answer = "Your question is too short. Please be more specific."

        elif word_count > 20:
            answer = "Your question is too long. Please shorten it."

        elif contains_warning(filtered):
            logger.warning(f"Potential prompt injection attempt: {question}")
            answer = "Your question cannot be processed. Please rephrase it."

        else:

            previous_intent = request.session.get("last_intent")

            intent = classify_question(filtered)

            if intent not in VALID_INTENTS:
                intent = "unknown"

            course = extract_course(filtered)

            # recover intent when user just clarifies course name
            if intent == "course_name" and course:
                if previous_intent in {
                    "course_classroom",
                    "course_time",
                    "course_lecturer",
                    "course_description"
                }:
                    intent = previous_intent

            # store corrected intent
            request.session["last_intent"] = intent

            logger.info(f"Question: {question}")
            logger.info(f"Intent: {intent}")
            logger.info(f"Course extracted: {course}")

            # -----------------------------
            # Recover course context
            # -----------------------------
            courses_context = request.session.get("last_courses")

            if not course and courses_context:

                if len(courses_context) == 1:
                    course = courses_context[0]

                elif len(courses_context) > 1:
                    options = ", ".join(courses_context)

                    return templates.TemplateResponse(
                        "ask.html",
                        {
                            "request": request,
                            "answer": f"You are enrolled in multiple courses: {options}. Which course do you mean?",
                            "question": question
                        }
                    )

            # -----------------------------
            # Run SQL query
            # -----------------------------
            result = choose_query(intent, course, user_id)

            # -----------------------------
            # Store context
            # -----------------------------
            if intent == "student_courses" and result:
                request.session["last_courses"] = result

            elif course:
                request.session["last_courses"] = [course]

            # -----------------------------
            # Format result for LLM
            # -----------------------------
            if isinstance(result, list):
                result = ", ".join(result) if len(result) > 1 else result[0]

            logger.info(f"Query result: {result}")

            answer = llm_answer(question, result, intent)

            # -----------------------------
            # Store successful Q&A
            # -----------------------------
            if intent != "unknown":
                save_question(user_id, question, answer)

    return templates.TemplateResponse(
        "ask.html",
        {
            "request": request,
            "answer": answer,
            "question": question
        }
    )