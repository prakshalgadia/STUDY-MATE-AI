# StudyMate AI - Project Statement

## 1. Problem Statement

Students usually manage their marks, attendance, examination dates and study planning separately. Because of this, they may not clearly know which subject needs more attention.

StudyMate AI is developed to provide a simple academic assistant where a student can enter subject details, marks, attendance and examination dates. The system analyzes the information and provides study recommendations and a basic study plan.

## 2. Project Scope

The project focuses on academic performance analysis and personalized study planning for students.

The current system supports four subjects and provides:

- Student information
- Subject information
- Marks analysis
- Attendance analysis
- Examination date analysis
- Subject priority
- Recommended study hours
- Basic study planning
- Database storage

The current recommendation system uses rule-based logic with Python conditions. It is not a machine learning model.

## 3. Target Users

The main target users are:

- College students
- School students
- Students preparing for examinations
- Students who want to organize their study time

## 4. Objectives

The main objectives of StudyMate AI are:

1. To analyze student academic performance.
2. To identify subjects that need attention.
3. To check attendance requirements.
4. To consider examination dates.
5. To provide subject priorities.
6. To recommend study hours according to marks.
7. To generate a basic study plan.
8. To store important student and academic information.

## 5. High-Level Features

### Student Information
The system accepts basic student details such as name, course and semester.

### Subject Management
The student can enter four subjects and their academic information.

### Performance Analysis
The system checks marks and identifies subjects with low performance.

### Attendance Analysis
The system checks attendance and identifies subjects below the 75% attendance level.

### Exam Analysis
The system considers the number of days remaining before examinations.

### Recommendation Engine
The system combines marks, attendance and examination information to assign subject priority.

### Study Planner
The system recommends study hours according to marks.

### Database
SQLite is used to store student and academic information.

## 6. Project Limitations

The current version has some limitations:

- It uses rule-based recommendations.
- It does not use a machine learning model.
- The current version is designed around four subjects.
- Advanced notification and reminder features are not included.
- Cloud synchronization is not included.

## 7. Future Enhancements

Future versions can include:

- Streamlit dashboard
- Graphical performance charts
- Study reminders
- Login system
- Mobile application
- Cloud database
- Progress tracking
- More advanced recommendation algorithms
- Machine learning based recommendations