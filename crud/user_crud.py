from database.db import get_connection


def get_user_id(username, email):

    with get_connection() as conn:
        cursor = conn.cursor()

        # check student
        cursor.execute("""
        SELECT student_id, role
        FROM student
        WHERE username=? AND email=?
        """, (username, email))

        student = cursor.fetchone()

        if student:
            return student


        # check lecturer
        cursor.execute("""
        SELECT lecturer_id, role
        FROM lecturer
        WHERE username=? AND email=?
        """, (username, email))

        lecturer = cursor.fetchone()

        if lecturer:
            return lecturer

    return None