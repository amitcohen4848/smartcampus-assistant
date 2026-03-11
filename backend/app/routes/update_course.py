import logging
from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from backend.app.dependecies.dependency import require_lecturer
from backend.crud.update_course_description import update_course_description

router = APIRouter()
templates = Jinja2Templates(directory="frontend/static/html")

logger = logging.getLogger(__name__)


@router.get("/update-course", response_class=HTMLResponse)
def update_course_page(request: Request, user_id=Depends(require_lecturer)):
    return templates.TemplateResponse(
        "update_course.html",
        {"request": request}
    )


@router.post("/update-course")
def update_course(
    course_name: str = Form(...),
    description: str = Form(...),
    user_id=Depends(require_lecturer)
):

    update_course_description(course_name, description)

    logger.info(f"Lecturer {user_id} updated course '{course_name}' description")

    return RedirectResponse("/eladcampus", status_code=303)
