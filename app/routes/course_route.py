from fastapi import APIRouter, Depends
from database.db import get_db

router = APIRouter()


# Route To get course
@router.get("/course")
def get_students(db = Depends(get_db)):
    cursor = db.execute("SELECT * FROM course")
    rows = cursor.fetchall()
    return [dict(row) for row in rows]