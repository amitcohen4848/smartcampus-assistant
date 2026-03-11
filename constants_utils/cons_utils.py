from database.db import get_connection

COURSES = []

with get_connection() as conn:
    cur = conn.cursor()

    sql_query = """
    SELECT course_name
    FROM course
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
    "unknown",
    "technical_support"
}

WARNING_WORDS = [
    ("ignore", "previous"),
    ("ignore", "instructions"),
    ("disregard", "instructions"),
    ("forget", "previous"),
    ("override", "instructions"),
    ("new", "instructions"),
    ("follow", "my", "instructions"),
    ("system", "prompt"),
    ("show", "system"),
    ("reveal", "prompt"),
    ("display", "instructions"),
    ("what", "are", "your", "instructions"),
    ("act", "as"),
    ("pretend", "to"),
    ("you", "are", "now"),
    ("drop", "table"),
    ("delete", "database"),
    ("remove", "database"),

]