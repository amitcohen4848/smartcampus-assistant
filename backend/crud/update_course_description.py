from backend.database.db import get_connection

def update_course_description(course_name, description):

    with get_connection() as conn:
        cur = conn.cursor()

        cur.execute("""
        UPDATE course
        SET course_description = ?
        WHERE course_name = ?
        """, (description, course_name))

        conn.commit()