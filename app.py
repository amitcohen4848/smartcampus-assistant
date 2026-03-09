import logging

from fastapi import FastAPI
from contextlib import asynccontextmanager
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
from database.db import get_connection

# Logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load .env file
load_dotenv()

# Set the API-LLM
client = OpenAI()

# Checking Connection to DB
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        conn = get_connection()
        conn.execute("SELECT 1")
        conn.close()
    except Exception as e:
        logger.error(f"Database startup check failed: {e}")
        raise

    yield
    logger.info("Server shutting down")

# Init Server
app = FastAPI(lifespan=lifespan)

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