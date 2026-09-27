import sqlite3


# ==========================================================
# DATABASE CONNECTION
# ==========================================================

def create_connection():
    connection = sqlite3.connect("studymate.db")
    return connection


# ==========================================================
# CREATE TABLES
# ==========================================================

def create_tables():

    connection = create_connection()
    cursor = connection.cursor()

    # Student table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        course TEXT,
        semester INTEGER
    )
    """)

    # Subject table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject_name TEXT,
        marks REAL,
        attendance REAL,
        exam_date TEXT
    )
    """)

    # Study plan table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS study_plan (
        plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject_name TEXT,
        study_hours REAL
    )
    """)

    # Progress table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS progress (
        progress_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject_name TEXT,
        completed_topics INTEGER,
        total_topics INTEGER,
        progress REAL
    )
    """)

    connection.commit()
    connection.close()


# ==========================================================
# ADD STUDENT
# ==========================================================

def add_student(name, course, semester):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO students (name, course, semester)
    VALUES (?, ?, ?)
    """, (name, course, semester))

    connection.commit()

    student_id = cursor.lastrowid

    connection.close()

    return student_id


# ==========================================================
# ADD SUBJECT
# ==========================================================

def add_subject(student_id, subject_name, marks, attendance, exam_date):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO subjects
    (student_id, subject_name, marks, attendance, exam_date)
    VALUES (?, ?, ?, ?, ?)
    """,
    (student_id, subject_name, marks, attendance, exam_date))

    connection.commit()
    connection.close()


# ==========================================================
# ADD STUDY PLAN
# ==========================================================

def add_study_plan(student_id, subject_name, study_hours):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO study_plan
    (student_id, subject_name, study_hours)
    VALUES (?, ?, ?)
    """,
    (student_id, subject_name, study_hours))

    connection.commit()
    connection.close()


# ==========================================================
# ADD PROGRESS
# ==========================================================

def add_progress(
    student_id,
    subject_name,
    completed_topics,
    total_topics,
    progress
):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO progress
    (student_id, subject_name, completed_topics,
     total_topics, progress)
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        student_id,
        subject_name,
        completed_topics,
        total_topics,
        progress
    ))

    connection.commit()
    connection.close()


# ==========================================================
# VIEW STUDENT DATA
# ==========================================================

def show_student_data(student_id):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM students
    WHERE student_id = ?
    """, (student_id,))

    student = cursor.fetchone()

    print("\n---------- STUDENT DATA ----------")

    if student:
        print("Student ID:", student[0])
        print("Name:", student[1])
        print("Course:", student[2])
        print("Semester:", student[3])
    else:
        print("Student not found.")

    connection.close()


# ==========================================================
# VIEW SUBJECT DATA
# ==========================================================

def show_subject_data(student_id):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT subject_name, marks, attendance, exam_date
    FROM subjects
    WHERE student_id = ?
    """, (student_id,))

    subjects = cursor.fetchall()

    print("\n---------- SUBJECT DATA ----------")

    for subject in subjects:

        print(
            subject[0],
            "| Marks:", subject[1],
            "| Attendance:", subject[2],
            "| Exam Date:", subject[3]
        )

    connection.close()


# ==========================================================
# VIEW STUDY PLAN
# ==========================================================

def show_study_plan(student_id):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT subject_name, study_hours
    FROM study_plan
    WHERE student_id = ?
    """, (student_id,))

    plans = cursor.fetchall()

    print("\n---------- STUDY PLAN ----------")

    for plan in plans:

        print(
            plan[0],
            "->",
            plan[1],
            "hours/day"
        )

    connection.close()


# ==========================================================
# VIEW PROGRESS
# ==========================================================

def show_progress(student_id):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT subject_name,
           completed_topics,
           total_topics,
           progress
    FROM progress
    WHERE student_id = ?
    """, (student_id,))

    progress_data = cursor.fetchall()

    print("\n---------- PROGRESS ----------")

    for data in progress_data:

        print(
            data[0],
            "| Completed:",
            data[1],
            "/",
            data[2],
            "| Progress:",
            round(data[3], 2),
            "%"
        )

    connection.close()


# ==========================================================
# TEST DATABASE
# ==========================================================

if __name__ == "__main__":

    create_tables()

    print("StudyMate AI Database Created Successfully!")
