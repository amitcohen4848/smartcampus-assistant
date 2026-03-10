import logging
from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.dependecies.dependency import require_login
from service.llm_service import classify_question
from service.nlp_utils import extract_course,data_filter
from service.intents import choose_query

from constants_utils.cons_utils import VALID_INTENTS

logger = logging.getLogger(__name__)

router = APIRouter()
templates = Jinja2Templates(directory="static/html")

@router.get("/ask")
def ask_page(request: Request, user_id = Depends(require_login)):
    return templates.TemplateResponse(
        "ask.html",
        {"request": request}
    )

@router.post("/ask")
def ask_ai(
    request: Request,
    question: str = Form(...),
    user_id = Depends(require_login)
):
    filtered = data_filter(question)

    if not filtered:
        answer = "Invalid question format."
    else:
        word_count = len(filtered.split())

        if word_count < 4 or word_count > 20:
            answer = "Invalid question length."

        else:
            intent = classify_question(filtered)
            course = extract_course(filtered)

            if intent not in VALID_INTENTS:
                intent = 'unknown'

            logger.info(f"Classifier intent: {intent}")

            answer = f"Intent detected: {intent}"

    return templates.TemplateResponse(
        "ask.html",
        {"request": request, "answer": answer}
    )

