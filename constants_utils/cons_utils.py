from database.db import get_connection

COURSES = []

with get_connection() as conn:
    cur = conn.cursor()

    sql_query = """
    SELECT course_name
    FROM courses
    """

    cur.execute(sql_query)
    rows = cur.fetchall()

    COURSES = [row[0].lower() for row in rows]



VALID_INTENTS = {
    "student_courses",
    "course_lecturer",
    "course_name",
    "course_time",
    "course_classroom",
    "course_description",
    "unknown"
}
