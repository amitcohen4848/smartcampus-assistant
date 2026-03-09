import sqlite3
from config import DB_PATH

conn = sqlite3.connect(DB_PATH)

# -------------------------
# Students
# -------------------------
conn.execute("""
INSERT INTO student (username, email, personal_id_number)
VALUES
('amit','amit@mail.com','305678980'),
('Gali','gali@mail.com','304678873'),
('Dor','dor@mail.com','205878760'),
('Niv','niv@mail.com','203878761')
""")

# -------------------------
# Lecturers
# -------------------------
conn.execute("""
INSERT INTO lecturer (username, email, department)
VALUES
('George','george@mail.com','Math'),
('Avital','avital@mail.com','Computer Science')
""")

# -------------------------
# Courses
# -------------------------
conn.execute("""
INSERT INTO course (course_name, lecture_hours, class_room, lecturer_id, course_description)
VALUES
('Linear Algebra','Monday 10:00 - 13:00','Room 200',1,'Linear Algebra for Math'),
('Python for beginners','Tuesday 09:00 - 11:00','Room 303',2,'Under Computer Science department')
""")

conn.commit()
conn.close()

print("Seed data inserted successfully.")
