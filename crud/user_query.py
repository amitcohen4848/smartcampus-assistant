from database.db import get_connection

def get_user_id(username: str, email: str) -> int | None:
    with get_connection() as conn:
        cursor = conn.cursor()

        sql_query = """
        SELECT student_id
        FROM student
        WHERE username = ? AND email = ?
        """

        cursor.execute(sql_query, (username, email))
        row = cursor.fetchone()

        if row:
            return row["student_id"]

        return None