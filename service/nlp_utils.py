import re


def extract_course(question: str):

    courses = [
        "Linear Algebra",
        "Python for beginners",
        "English",
        "Math"
    ]

    for course in courses:
        if course.lower() in question.lower():
            return course

    return None


def data_filter(question: str):

    # allow only letters, numbers and spaces
    pattern = r"^[a-zA-Z0-9\s\?\.\-\,']+$"

    if not re.fullmatch(pattern, question):
        return None

    return question.strip()