import re
from constants_utils.cons_utils import COURSES, WARNING_WORDS

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


def contains_warning(sentence: str):
    sentence = sentence.lower()

    for group in WARNING_WORDS:
        if all(word in sentence for word in group):
            return True

    return False