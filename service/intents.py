import queries.llm_queries as ql

def choose_query(intent, course, user_id):

    # intents that require a course name
    course_required = [
        "course_time",
        "course_classroom",
        "course_lecturer",
        "course_description"
    ]

    if intent in course_required and not course:
        return "Please specify the course name."

    if intent == "student_courses":
        # query student_courses db
        result = ql.get_student_courses(user_id)

        if not result:
            return "No student courses found."

        return result


    elif intent == "course_time":
        # query course DB
        result = ql.get_course_time(course)

        if not result:
            return "No time for this course found."

        return result

    elif intent == "course_classroom":
        # query course DB
        result = ql.get_course_classroom(course)

        if not result:
            return "No classroom found for this course."

        return result


    elif intent == "course_lecturer":
        # query course DB
        result = ql.get_course_lecturer(course)

        if not result:
            return "No lecturer for this course found."

        return result

    elif intent == "course_description":
        # query course DB
        result = ql.get_course_description(course)

        if not result:
            return "No description for this course."

        return result
    else:
        return "I cannot answer that question."