import re
import logging
from rapidfuzz import process
from constants_utils.cons_utils import COURSES, WARNING_WORDS

logger = logging.getLogger(__name__)

def extract_course(text):

    text = text.lower()

    logger.info(f"Extractor input: {text}")
    logger.info(f"Available courses: {COURSES}")

    # First try fuzzy match
    match = process.extractOne(text, COURSES, score_cutoff=60)

    if match:
        logger.info(f"Fuzzy match: {match}")
        return match[0]

    # Second attempt: keyword search
    for course in COURSES:
        words = course.split()

        for w in words:
            if w in text:
                if len(w) < 4:
                    continue
                logger.info(f"Keyword match: {course}")
                return course

    logger.info("No course match found")
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