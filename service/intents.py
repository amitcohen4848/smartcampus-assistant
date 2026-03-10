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
        # query DB
        pass

    elif intent == "course_time":
        # query DB
        pass

    elif intent == "course_lecturer":
        # query DB
        pass

    elif intent == "course_description":
        # query DB
        pass

    else:
        return "I cannot answer that question."