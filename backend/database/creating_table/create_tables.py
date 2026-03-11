import sqlite3
from backend.config import DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# -------------------------
# STUDENT TABLE
# -------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    role TEXT NOT NULL DEFAULT 'student',
    personal_id_number TEXT UNIQUE NOT NULL)
""")

# -------------------------
# LECTURER TABLE
# -------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS lecturer (
    lecturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    role TEXT NOT NULL DEFAULT 'lecturer',
    department TEXT
)
""")

# -------------------------
# COURSE TABLE
# -------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS course (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT UNIQUE NOT NULL,
    course_name TEXT NOT NULL,
    lecture_hours TEXT NOT NULL,
    class_room TEXT NOT NULL DEFAULT 'distance learning',
    lecturer_id INTEGER NOT NULL,
    course_description TEXT NOT NULL DEFAULT 'No Description Provided',

    FOREIGN KEY (lecturer_id) REFERENCES lecturer(lecturer_id)
)
""")

# -------------------------
# Question TABLE
# -------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS question (
    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    answer_text TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (student_id) REFERENCES student(student_id)
)
""")

# -------------------------
# Student - Courses TABLE
# -------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS student_course (
    student_course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    UNIQUE(student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id))
""")

conn.commit()
conn.close()

print("Database created successfully. 👌")