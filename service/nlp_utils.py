import re
from constants_utils.cons_utils import COURSES

def extract_course(question: str):

    question = question.lower()

    for course in COURSES:
        if course in question:
            return course

    return None


def data_filter(question: str):

    # allow only letters, numbers and spaces
    pattern = r"^[a-zA-Z0-9\s\?\.\-\,']+$"

    if not re.fullmatch(pattern, question):
        return None

    return question.strip()