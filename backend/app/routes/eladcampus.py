from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from backend.app.dependecies.dependency import require_login

router = APIRouter()
templates = Jinja2Templates(directory="frontend/static/html")

@router.get("/eladcampus")
def campus_home(request: Request, user_id = Depends(require_login)):
    return templates.TemplateResponse(
        "elad_campus.html",
        {"request": request, "user_id": user_id}
    )