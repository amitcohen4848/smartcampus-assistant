import logging
from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from app.dependecies.dependency import require_login
from service.llm_service import classify_question, llm_answer
from service.nlp_utils import extract_course, data_filter, contains_warning
from service.intents import choose_query
from constants_utils.cons_utils import VALID_INTENTS

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

        if word_count < 4:
            answer = "Your question is too short. Please be more specific."

        elif word_count > 20:
            answer = "Your question is too long. Please shorten it."

        elif contains_warning(filtered):
            logger.warning(f"Potential prompt injection attempt: {question}")
            answer = "Your question cannot be processed. Please rephrase it."

        else:
            intent = classify_question(filtered)

            if intent not in VALID_INTENTS:
                intent = "unknown"

            course = extract_course(filtered)

            logger.info(f"Question: {question}")
            logger.info(f"Intent: {intent}")
            logger.info(f"Course: {course}")

            result = choose_query(intent, course, user_id)

            # Format result for LLM
            if isinstance(result, list):
                result = ", ".join(result) if len(result) > 1 else result[0]

            logger.info(f"Query result: {result}")

            answer = llm_answer(question, result, intent)

    return templates.TemplateResponse(
        "ask.html",
        {
            "request": request,
            "answer": answer,
            "question": question
        }
    )