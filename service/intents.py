import logging
import queries.llm_queries as ql

logger = logging.getLogger(__name__)


def choose_query(intent, course, user_id):

    course_required = [
        "course_time",
        "course_classroom",
        "course_lecturer",
        "course_description"
    ]

    if intent in course_required and not course:
        return "Please specify the course name."

    try:

        if intent == "student_courses":

            result = ql.get_student_courses(user_id)

            if not result:
                return "No student courses found."

            return result


        elif intent == "course_time":

            result = ql.get_course_time(course)

            if not result:
                return "No time for this course found."

            return result


        elif intent == "course_classroom":

            result = ql.get_course_classroom(course)

            if not result:
                return "No classroom found for this course."

            return result


        elif intent == "course_lecturer":

            result = ql.get_course_lecturer(course)

            if not result:
                return "No lecturer for this course found."

            return result


        elif intent == "course_description":

            result = ql.get_course_description(course)

            if not result:
                return "No description for this course."

            return result


    except Exception as e:

        logger.error(f"Database query failed: {e}")

        return "Database error."


    if intent == "technical_support":

        return (
            "This seems to be a technical issue. "
            "Please contact the SmartCampus IT support or your campus help desk."
        )

    return "I cannot answer that question."