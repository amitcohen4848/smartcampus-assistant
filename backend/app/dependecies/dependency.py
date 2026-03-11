from fastapi import Request, HTTPException


def require_login(request: Request):
    user_id = request.session.get("user_id")

    if not user_id:
        raise HTTPException(status_code=401, detail="Not logged in")

    return user_id


def require_lecturer(request: Request):
    user_id = request.session.get("user_id")
    role = request.session.get("user_role")

    if not user_id:
        raise HTTPException(status_code=401, detail="Not logged in")

    if role != "lecturer":
        raise HTTPException(status_code=403, detail="Lecturers only")

    return user_id