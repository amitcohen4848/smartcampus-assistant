from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.dependecies.dependency import require_login

router = APIRouter()
templates = Jinja2Templates(directory="static/html")

@router.get("/eladcampus")
def campus_home(request: Request, user_id = Depends(require_login)):
    return templates.TemplateResponse(
        "eladcampus.html",
        {"request": request, "user_id": user_id}
    )