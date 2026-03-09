from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

app = FastAPI()

class Question(BaseModel):
    question: str
    age: int


@app.post("/ask")
def ask_question(data: Question):

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=data.question
    )

    answer = response.output[0].content[0].text

    return {"answer": answer}