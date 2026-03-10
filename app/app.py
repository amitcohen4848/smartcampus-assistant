# ===============================
# Imports
# ===============================
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from starlette.middleware.sessions import SessionMiddleware
from pydantic import BaseModel

from database.db import get_connection

from app.routes.student_route import router as student_router
from app.routes.course_route import router as course_router
from app.routes.auth import router as auth_router
from app.routes.eladcampus import router as eladcampus_router
from app.routes.question_route import router as question_router


# ===============================
# Logging
# ===============================

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("smartcampus")


# ===============================
# Startup / Shutdown
# ===============================

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        conn = get_connection()
        conn.execute("SELECT 1")
        conn.close()
        logger.info("Database connection OK")

    except Exception as e:
        logger.error(f"Database startup check failed: {e}")
        raise

    yield

    logger.info("Server shutting down")


# ===============================
# App Initialization
# ===============================

app = FastAPI(lifespan=lifespan)


# ===============================
# Static Files
# ===============================

app.mount("/static", StaticFiles(directory="static"), name="static")


# ===============================
# Middleware
# ===============================

app.add_middleware(
    SessionMiddleware,
    secret_key="secret-key"
)


@app.middleware("http")
async def log_user_requests(request: Request, call_next):

    # Pass the request forward to the next middleware / route handler
    # and wait until the route finishes executing
    response = await call_next(request)

    # if a session exists (SessionMiddleware creates this)
    session = request.scope.get("session")

    # If the request has a session attached
    if session:

        # Extract the user id stored in the session cookie
        user_id = session.get("user_id")

        # Extract the role stored during login (student / lecturer)
        role = session.get("user_role")

        # If a user is authenticated (user_id exists in the session)
        if user_id:

            # Log which user made the request, what role they have,
            # and which endpoint they accessed
            logger.info(f"{role}:{user_id} → {request.method} {request.url.path}")

    # Return the response back to the client (browser)
    return response


# ===============================
# Routes
# ===============================

@app.get("/")
def root():
    return RedirectResponse(url="/login")


# Register routers
app.include_router(auth_router)
app.include_router(student_router)
app.include_router(course_router)
app.include_router(eladcampus_router)
app.include_router(question_router)


# ===============================
# Future Models
# ===============================

class Question(BaseModel):
    question: str
    age: int