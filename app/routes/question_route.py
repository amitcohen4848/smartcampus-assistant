from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.dependecies.dependency import require_login
from service.llm_service import llm_answer

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
    answer = llm_answer(question)

    return templates.TemplateResponse(
        "ask.html",
        {"request": request, "answer": answer}
    )

