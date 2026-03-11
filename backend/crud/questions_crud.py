from backend.database.db import get_connection

def save_question(student_id, question_text, answer_text):
    with get_connection() as conn:
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO question (student_id, question_text, answer_text)
        VALUES (?, ?, ?)
        """, (student_id, question_text, answer_text))

        conn.commit()