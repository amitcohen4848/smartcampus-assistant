from fastapi import Request
from fastapi.responses import RedirectResponse


def require_login(request: Request):
    user_id = request.session.get("user_id")

    if not user_id:
        return RedirectResponse("/login")

    return user_id

def require_lecturer(request: Request):
    role = request.session.get("user_role")

    if role != "lecturer":
        return RedirectResponse("/login")

    return request.session["user_id"]