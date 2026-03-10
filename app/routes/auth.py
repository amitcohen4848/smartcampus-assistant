from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from crud.user_crud import get_user_id

router = APIRouter()
templates = Jinja2Templates(directory="static/html")


@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.post("/login")
def login(
    request: Request,
    username: str = Form(...),
    email: str = Form(...)
):
    user = get_user_id(username, email)

    if user:
        # since query can return None better unpacking it here:
        user_id, user_role = user

        request.session["user_id"] = user_id
        request.session["user_role"] = user_role

        return RedirectResponse("/eladcampus", status_code=303)

    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": "User does not exist"}
    )