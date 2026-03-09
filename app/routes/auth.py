from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database.db import get_connection


router = APIRouter()
templates = Jinja2Templates(directory="static/html")
@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login", response_class=HTMLResponse)
def login(request: Request,
          username: str = Form(...)):

    user = get_user_by_username(username)

    if user:
        request.session["user_id"] = user.id
        return RedirectResponse(url="/welovemath", status_code=303)

    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": "User does not exist"}
    )