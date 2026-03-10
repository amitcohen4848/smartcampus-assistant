from database.db import get_connection


def get_student_courses(student_id):

    with get_connection() as conn:
        cur = conn.cursor()

        query = """
        SELECT c.course_name
        FROM course c
        JOIN student_course sc
        ON c.course_id = sc.course_id
        WHERE sc.student_id = ?
        """

        cur.execute(query, (student_id,))
        rows = cur.fetchall()

        return [row[0] for row in rows]


def get_course_time(course_name):

    with get_connection() as conn:
        cur = conn.cursor()

        query = """
        SELECT lecture_hours
        FROM course
        WHERE LOWER(course_name) = ?
        """

        cur.execute(query, (course_name.lower(),))
        rows = cur.fetchall()

        return [row[0] for row in rows]


def get_course_classroom(course_name):

    with get_connection() as conn:
        cur = conn.cursor()

        query = """
        SELECT class_room
        FROM course
        WHERE LOWER(course_name) = ?
        """

        cur.execute(query, (course_name.lower(),))
        rows = cur.fetchall()

        return [row[0] for row in rows]


def get_course_lecturer(course_name):

    with get_connection() as conn:
        cur = conn.cursor()

        query = """
        SELECT l.username
        FROM course c
        JOIN lecturer l
        ON c.lecturer_id = l.lecturer_id
        WHERE LOWER(c.course_name) = ?
        """

        cur.execute(query, (course_name.lower(),))
        rows = cur.fetchall()

        return [row[0] for row in rows]


def get_course_description(course_name):

    with get_connection() as conn:
        cur = conn.cursor()

        query = """
        SELECT c.course_description
        FROM course c
        WHERE LOWER(course_name) = ?
        """

        cur.execute(query, (course_name.lower(),))
        rows = cur.fetchall()

        return [row[0] for row in rows]