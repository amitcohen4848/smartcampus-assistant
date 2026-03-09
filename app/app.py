import logging

from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from contextlib import asynccontextmanager

from database.db import get_connection
from app.routes.student_route import router as student_router
from app.routes.course_route import router as course_router
from app.routes.auth import router as auth
from starlette.middleware.sessions import SessionMiddleware



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

# Mount
app.mount("/static", StaticFiles(directory="static"), name="static")

# Middleware
app.add_middleware(
    SessionMiddleware,
    secret_key="secret-key"
)

# root redirect while going into link
@app.get("/")
def root():
    return RedirectResponse(url="/login")

# Include routers
app.include_router(auth)
app.include_router(student_router)
app.include_router(course_router)



#For later
class Question(BaseModel):
    question: str
    age: int

