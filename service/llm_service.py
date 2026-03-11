import logging

from openai import OpenAI, RateLimitError
from config import OPENAI_API_KEY, CLASSIFIER_SYSTEM_PROMPT, LLM_ANSWER_PROMPT

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

client = OpenAI(api_key=OPENAI_API_KEY)

def classify_question(question: str):

    try:

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {"role": "system", "content": CLASSIFIER_SYSTEM_PROMPT},
                {"role": "user", "content": question}
            ]
        )

        return response.output_text.strip()

    except RateLimitError:
        logger.error("Classifier API rate limit reached.")
        return "unknown"

    except Exception as e:
        logger.error(f"Classifier error: {e}")
        return "unknown"


def llm_answer(question: str, data: str, intent: str):

    try:

        prompt = LLM_ANSWER_PROMPT.format(
            question=question,
            intent=intent,
            data=data
        )

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        return response.output_text.strip()

    except RateLimitError:
        logger.error("API rate limit reached.")
        return "The AI service is currently busy. Please try again later."

    except Exception as e:
        logger.error(f"LLM error: {e}")
        return "Sorry, something went wrong while generating the response."