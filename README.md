StudyMate AI

AI-Based Student Academic Assistant

StudyMate AI is a Python-based student academic assistant designed to
help students understand their academic performance and create a
personalized study plan.

The application takes student information, subject marks, attendance,
and examination dates as input. It analyzes the data, identifies
subjects that need attention, generates recommendations, creates a study
plan, and tracks academic progress.

Problem Statement

Students often manage marks, attendance, examination dates, and study
schedules separately. Because of this, it can be difficult to identify
which subject needs immediate attention and how much time should be
given to each subject.

StudyMate AI provides a single system to analyze this information and
generate personalized academic recommendations.

Objectives

Store student and subject information.

Analyze marks and attendance.

Track examination dates.

Identify subject priority.

Generate personalized recommendations.

Recommend daily study hours.

Create a basic study plan.

Track topic completion and overall progress.

Store academic data using SQLite database.

Main Features

1. Student Information

Stores: - Student name - Course - Semester

2. Performance Analysis

Analyzes: - Subject marks - Lowest marks - Attendance - Attendance below
75%

3. Examination Analysis

Accepts examination dates.

Calculates remaining days.

Uses examination proximity in priority analysis.

4. Recommendation Engine

The recommendation engine uses: - Marks - Attendance - Remaining exam
days

It generates: - Subject priority - Reason for priority - Personalized
recommendation

5. Study Planner

The study planner recommends study time based on marks:

Marks           Recommended Study Time

Below 40                   3 hours/day
40--49                     2 hours/day
50--59                   1.5 hours/day
60 or above                 1 hour/day

6. Progress Tracking

Tracks: - Completed topics - Total topics - Subject-wise progress -
Overall progress

7. Database

SQLite is used to store: - Student information - Subject information -
Study plans - Progress information

Technologies Used

Python

SQLite3

Basic Python functions and conditional statements

VS Code

Git and GitHub

Project Structure

StudyMate-AI/
│
├── app.py
├── database.py
├── recommendation_engine.py
├── study_planner.py
├── performance_analyzer.py
├── validation.py
│
├── studymate.db
│
├── tests/
│   ├── test_planner.py
│   ├── test_analyzer.py
│   └── test_validation.py
│
├── docs/
│   ├── architecture.png
│   ├── workflow.png
│   ├── use_case.png
│   ├── class_diagram.png
│   ├── sequence_diagram.png
│   └── er_diagram.png
│
├── README.md
└── statement.md

How the System Works

Student Input
      ↓
Performance Analysis
      ↓
Priority Analysis
      ↓
Recommendation Engine
      ↓
Study Planner
      ↓
Progress Tracking
      ↓
Database Storage
      ↓
Final Academic Summary

Recommendation Logic

The system uses rule-based logic.

Examples:

Low marks can increase study requirements.

Attendance below 75% is flagged.

An examination within a short period increases attention to that
subject.

Multiple academic concerns can result in higher priority.

The recommendation engine is implemented using basic Python functions
and conditional statements.

Database Design

The SQLite database contains four main tables:

students

Stores student information.

subjects

Stores subject name, marks, attendance, and examination date.

study_plan

Stores recommended study hours for each subject.

progress

progress

Stores completed topics, total topics, and calculated progress.

Testing

Example test cases include:

Valid marks input.

Invalid marks input.

Attendance below 75%.

Low marks with an upcoming examination.

Study-hour calculation.

Progress percentage calculation.

Database insertion and retrieval.

Future Enhancements

Streamlit graphical dashboard

More detailed topic-level planning

Reminder notifications

Graphical performance reports

User login

Cloud database

Machine-learning-based recommendations

Author

Prakshal Gadia
26MIM10080
VIT Bhopal University
Integrated M.Tech in Artificial Intelligence