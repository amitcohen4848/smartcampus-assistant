from openai import OpenAI
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def llm_answer(question: str):

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=question
    )

    return response.output_text