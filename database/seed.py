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
('gali','gali@mail.com','304678873'),
('dor','dor@mail.com','205878760'),
('niv','niv@mail.com','203878761'),
('maya','maya@mail.com','203878762'),
('noa','noa@mail.com','203878763'),
('yossi','yossi@mail.com','203878764'),
('david','david@mail.com','203878765'),
('lior','lior@mail.com','203878766'),
('tamar','tamar@mail.com','203878767')
""")

# -------------------------
# Lecturers
# -------------------------
conn.execute("""
INSERT INTO lecturer (username, email, department)
VALUES
('George','george@mail.com','Math'),
('Avital','avital@mail.com','Computer Science'),
('Moshe','moshe@mail.com','Biotechnology'),
('Rafi','rafi@mail.com','Neuro Science'),
('Hannah','hannah@mail.com','Economy'),
('Yotam','yotam@mail.com','Engineering')
""")

# -------------------------
# Courses
# -------------------------
conn.execute("""
INSERT INTO course (course_code, course_name, lecture_hours, class_room, lecturer_id, course_description)
VALUES
('M101','Linear Algebra','Monday 10:00 - 13:00','Room 200',1,'Linear Algebra for Math'),
('CS011','Python for beginners','Tuesday 09:00 - 11:00','Room 303',2,'Introduction to Python programming'),
('M102','Number Theory','Monday 13:00 - 15:00','Room 202',1,'Elementary Number Theory'),
('B001','Molecular Biology','Sunday 09:00 - 10:30','Room 401',3,'Basic course for biology students'),
('NS203','Statistics for Neuroscience','Wednesday 13:00 - 15:00','Room 901',4,'Statistics tools for neuroscience'),
('EC101','Microeconomics','Thursday 11:00 - 13:00','Room 305',5,'Introduction to economic theory'),
('ENG210','Thermodynamics','Sunday 12:00 - 14:00','Room 510',6,'Engineering thermodynamics'),
('CS220','Data Structures','Wednesday 09:00 - 11:00','Room 303',2,'Algorithms and data structures')
""")

# -------------------------
# Student - Course relation
# -------------------------
conn.execute("""
INSERT INTO student_course (student_id, course_id)
VALUES
(1,1),
(1,2),
(1,3),

(2,1),
(2,2),

(3,3),
(3,4),

(4,2),
(4,5),

(5,1),
(5,6),

(6,2),
(6,8),

(7,6),
(7,7),

(8,3),
(8,4),

(9,5),
(9,7),

(10,1),
(10,8)
""")

# -------------------------
# Question history (LLM logs)
# -------------------------
conn.execute("""
INSERT INTO question (student_id, question_text, answer_text)
VALUES
(1,'When is my Linear Algebra class?','Monday 10:00 - 13:00 in Room 200'),
(1,'Who teaches Number Theory?','George teaches Number Theory'),
(2,'Where is Python class?','Room 303'),
(3,'What courses am I enrolled in?','Number Theory and Molecular Biology'),
(4,'When is Statistics for Neuroscience?','Wednesday 13:00 - 15:00'),
(5,'Who teaches Microeconomics?','Hannah'),
(6,'Where is Data Structures class?','Room 303'),
(7,'What is the schedule for Thermodynamics?','Sunday 12:00 - 14:00'),
(8,'Who teaches Molecular Biology?','Moshe'),
(9,'When is my neuroscience statistics class?','Wednesday 13:00')
""")

conn.commit()
conn.close()

print("Seed data inserted successfully.")
print("DB PATH:", DB_PATH)