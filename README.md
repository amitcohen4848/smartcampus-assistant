# Smart Campus AI Assistant

## Project Description
Smart Campus is a web-based system that allows students to ask questions about their courses using natural language.  
The system integrates a database with an AI service to provide answers about course information such as lecturers, schedules, classrooms, and enrolled courses.

The system processes student questions, classifies their intent using an AI model, retrieves relevant information from the database, and generates a natural language response.

---

## Main Features
- Student authentication and session management
- Natural language question interface
- AI-based intent classification
- Database query execution based on detected intent
- AI-generated responses based on query results
- Prompt injection protection

---

## System Architecture
The system is composed of several main components:

1. FastAPI backend that handles HTTP requests and routes.
2. AI service that uses the OpenAI API to classify user questions and generate answers.
3. A database that stores students, lecturers, and course information.
4. NLP utilities that extract course names and filter user input.

---

## Project Structure
```
smartcampus-assistant
│
├── backend
│ ├── app
│ │ ├── dependencies
│ │ ├── routes
│ │ └── app.py
│ │
│ ├── constants_utils
│ ├── crud
│ ├── database
│ ├── evaluation
│ ├── queries
│ ├── service
│ ├── config.py
│ └── requirements.txt
│
├── frontend
│ └── static
│ ├── css
│ ├── html
│ └── images
│
├── docs
│ └── project documentation files
│
├── tests
│ └── test_llm_service.py
│
├── classifier_test.csv
└── README.md
```

---

## Installation

Clone the repository:
git clone https://github.com/amitcohen4848/smartcampus-assistant.git
cd smartcampus-assistant

Create virtual environment:


python -m venv .venv


Activate environment:

Windows:

.venv\Scripts\activate


Install dependencies:


pip install -r requirements.txt


---

## Running the Application

Start the FastAPI server:


uvicorn backend.app.app:app --reload

Open in browser:


http://127.0.0.1:8000


---

## Running Unit Tests

Run the unit test for the AI service:


pytest tests/test_llm_service.py


Expected output:


1 passed


The test verifies that the AI service correctly processes the response from the language model.

---

## Technologies Used

- Python
- FastAPI
- OpenAI API
- SQLite
- Pytest

---

## Future Improvements

- Improve prompt engineering for better AI responses
- Add more unit tests for system services
- Improve deployment and hosting
- Enhance security against prompt injection