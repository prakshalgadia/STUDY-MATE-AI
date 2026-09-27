print("-------welcome to study-mate ai------")

name = input("enter your name : ")
semester = input("enter your semester : ")
rgno = input("enter your reg number : ")
course = input("enter your course : ")
school = input("enter your school : ")

#student profile
print("-----\nStudent Profile--------")
print("Name:", name)
print("Semester:", semester)
print("Reg Number:", rgno)
print("Course:", course)
print("School:", school)

#subject information
print("-----\nSubject Information-------")
subject1= input("enter your first subject : ")
subject2= input("enter your second subject :")
subject3= input("enter your third subject :")
subject4= input("enter your fourth subject :")

#subjects list
print("-----\nYour Subjects:-----")
print("1.", subject1)
print("2.", subject2)
print("3.", subject3)
print("4.", subject4)



print("\n--- Academic Performance ---")

marks1 = float(input(f"Enter your marks in {subject1}: "))
attendance1 = float(input(f"Enter your attendance in {subject1} (%): "))

marks2 = float(input(f"Enter your marks in {subject2}: "))
attendance2 = float(input(f"Enter your attendance in {subject2} (%): "))

marks3 = float(input(f"Enter your marks in {subject3}: "))
attendance3 = float(input(f"Enter your attendance in {subject3} (%): "))

marks4 = float(input(f"Enter your marks in {subject4}: "))
attendance4 = float(input(f"Enter your attendance in {subject4} (%): "))

print("\n--- Your Academic Performance ---")

print(subject1, "- Marks:", marks1, "| Attendance:", attendance1, "%")
print(subject2, "- Marks:", marks2, "| Attendance:", attendance2, "%")
print(subject3, "- Marks:", marks3, "| Attendance:", attendance3, "%")
print(subject4, "- Marks:", marks4, "| Attendance:", attendance4, "%")

print("\n--- Performance Analysis ---")

# Finding subject with lowest marks
# Finding lowest marks

lowest_marks = min(marks1, marks2, marks3, marks4)

print("\n-------- Marks Analysis-------")
print("Lowest Marks:", lowest_marks)

if marks1 == lowest_marks:
    print(subject1, "-> Marks:", marks1, " Needs Attention")

if marks2 == lowest_marks:
    print(subject2, "-> Marks:", marks2, " Needs Attention")

if marks3 == lowest_marks:
    print(subject3, "-> Marks:", marks3, " Needs Attention")

if marks4 == lowest_marks:
    print(subject4, "-> Marks:", marks4, " Needs Attention")


# Attendance analysis
print("\n------- Attendance Analysis----------")

attendance_weak = False

if attendance1 < 75:
    print(subject1, "-> Attendance:", attendance1, "%  Below 75%")
    attendance_weak = True

if attendance2 < 75:
    print(subject2, "-> Attendance:", attendance2, "% Below 75%")
    attendance_weak = True

if attendance3 < 75:
    print(subject3, "-> Attendance:", attendance3, "%  Below 75%")
    attendance_weak = True

if attendance4 < 75:
    print(subject4, "-> Attendance:", attendance4, "%  Below 75%")
    attendance_weak = True

if attendance_weak == False:
    print("All subjects have attendance of 75% or above. ")

from datetime import datetime

print("\n---------- Exam Dates ----------")

exam1 = input("Enter exam date for " + subject1 + " (DD-MM-YYYY): ")
exam2 = input("Enter exam date for " + subject2 + " (DD-MM-YYYY): ")
exam3 = input("Enter exam date for " + subject3 + " (DD-MM-YYYY): ")
exam4 = input("Enter exam date for " + subject4 + " (DD-MM-YYYY): ")

exam_date1 = datetime.strptime(exam1, "%d-%m-%Y")
exam_date2 = datetime.strptime(exam2, "%d-%m-%Y")
exam_date3 = datetime.strptime(exam3, "%d-%m-%Y")
exam_date4 = datetime.strptime(exam4, "%d-%m-%Y")

print("\nExam dates successfully stored!")

# Getting today's date
today = datetime.now()

# Calculating remaining days (date se date minus karenge taaki exact din milein)
days1 = (exam_date1.date() - today.date()).days
days2 = (exam_date2.date() - today.date()).days
days3 = (exam_date3.date() - today.date()).days
days4 = (exam_date4.date() - today.date()).days

print("\n---------- Days Remaining for Exams ----------")

print(subject1, "->", days1, "days remaining")
print(subject2, "->", days2, "days remaining")
print(subject3, "->", days3, "days remaining")
print(subject4, "->", days4, "days remaining")

print("\n---------- Subject Priority ----------")

# Mathematics
if marks1 < 60 and attendance1 < 75 and days1 <= 7:
    print(subject1, "-> HIGH PRIORITY")
    print("Reason: Low Marks + Low Attendance + Exam Near")

elif marks1 < 60 or attendance1 < 75 or days1 <= 7:
    print(subject1, "-> MEDIUM PRIORITY")
    print("Reason: Needs Attention")

else:
    print(subject1, "-> LOW PRIORITY")
    print("Reason: No Major Concern")


# Python
if marks2 < 60 and attendance2 < 75 and days2 <= 7:
    print(subject2, "-> HIGH PRIORITY")
    print("Reason: Low Marks + Low Attendance + Exam Near")

elif marks2 < 60 or attendance2 < 75 or days2 <= 7:
    print(subject2, "-> MEDIUM PRIORITY")
    print("Reason: Needs Attention")

else:
    print(subject2, "-> LOW PRIORITY")
    print("Reason: No Major Concern")


# evs
if marks3 < 60 and attendance3 < 75 and days3 <= 7:
    print(subject3, "-> HIGH PRIORITY")
    print("Reason: Low Marks + Low Attendance + Exam Near")

elif marks3 < 60 or attendance3 < 75 or days3 <= 7:
    print(subject3, "-> MEDIUM PRIORITY")
    print("Reason: Needs Attention")

else:
    print(subject3, "-> LOW PRIORITY")
    print("Reason: No Major Concern")


# Communication
if marks4 < 60 and attendance4 < 75 and days4 <= 7:
    print(subject4, "-> HIGH PRIORITY")
    print("Reason: Low Marks + Low Attendance + Exam Near")

elif marks4 < 60 or attendance4 < 75 or days4 <= 7:
    print(subject4, "-> MEDIUM PRIORITY")
    print("Reason: Needs Attention")

else:
    print(subject4, "-> LOW PRIORITY")
    print("Reason: No Major Concern")

#study hours

print("\n---------- Study Hours Recommendation ----------")

# marks 1

if marks1 < 40:
    print(subject1, "-> Recommended Study Hours: 3 hours/day")

elif marks1 < 50:
    print(subject1, "-> Recommended Study Hours: 2 hours/day")

elif marks1 < 60:
    print(subject1, "-> Recommended Study Hours: 1.5 hours/day")

else:
    print(subject1, "-> Recommended Study Hours: 1 hour/day")

# marks 2

if marks2 < 40:
    print(subject2, "-> Recommended Study Hours: 3 hours/day")

elif marks2 < 50:
    print(subject2, "-> Recommended Study Hours: 2 hours/day")

elif marks2 < 60:
    print(subject2, "-> Recommended Study Hours: 1.5 hours/day")

else:
    print(subject2, "-> Recommended Study Hours: 1 hour/day")


# marks 3

if marks3 < 40:
    print(subject3, "-> Recommended Study Hours: 3 hours/day")

elif marks3 < 50:
    print(subject3, "-> Recommended Study Hours: 2 hours/day")

elif marks3 < 60:
    print(subject3, "-> Recommended Study Hours: 1.5 hours/day")

else:
    print(subject3, "-> Recommended Study Hours: 1 hour/day")


# marks 4

if marks4 < 40:
    print(subject4, "-> Recommended Study Hours: 3 hours/day")

elif marks4 < 50:
    print(subject4, "-> Recommended Study Hours: 2 hours/day")

elif marks4 < 60:
    print(subject4, "-> Recommended Study Hours: 1.5 hours/day")

else:
    print(subject4, "-> Recommended Study Hours: 1 hour/day")


# ==========================================================
# FINAL RECOMMENDATION ENGINE
# ==========================================================

print("\n\n========== AI RECOMMENDATION ENGINE ==========")

def generate_recommendation(subject, marks, attendance, days):
    
    if marks < 40 and attendance < 75 and days <= 7:
        return "HIGH PRIORITY", "Low marks, low attendance and exam is near."

    elif marks < 40 or attendance < 75 or days <= 7:
        return "MEDIUM PRIORITY", "One or more areas need attention."

    else:
        return "LOW PRIORITY", "Performance is satisfactory."


priority1, reason1 = generate_recommendation(
    subject1, marks1, attendance1, days1
)

priority2, reason2 = generate_recommendation(
    subject2, marks2, attendance2, days2
)

priority3, reason3 = generate_recommendation(
    subject3, marks3, attendance3, days3
)

priority4, reason4 = generate_recommendation(
    subject4, marks4, attendance4, days4
)


print("\n", subject1)
print("Priority:", priority1)
print("Recommendation:", reason1)

print("\n", subject2)
print("Priority:", priority2)
print("Recommendation:", reason2)

print("\n", subject3)
print("Priority:", priority3)
print("Recommendation:", reason3)

print("\n", subject4)
print("Priority:", priority4)
print("Recommendation:", reason4)


# ==========================================================
# STUDY PLANNER
# ==========================================================

print("\n\n========== PERSONALIZED STUDY PLAN ==========")

def study_hours(marks):
    
    if marks < 40:
        return 3

    elif marks < 50:
        return 2

    elif marks < 60:
        return 1.5

    else:
        return 1


hours1 = study_hours(marks1)
hours2 = study_hours(marks2)
hours3 = study_hours(marks3)
hours4 = study_hours(marks4)


print(subject1, "->", hours1, "hours/day")
print(subject2, "->", hours2, "hours/day")
print(subject3, "->", hours3, "hours/day")
print(subject4, "->", hours4, "hours/day")


# ==========================================================
# OVERALL STUDY TIME
# ==========================================================

total_study_hours = hours1 + hours2 + hours3 + hours4

print("\nTotal Recommended Study Time:",
      total_study_hours, "hours/day")


# ==========================================================
# PROGRESS TRACKING
# ==========================================================

print("\n\n========== PROGRESS TRACKING ==========")

completed1 = int(input("Enter completed topics for " + subject1 + ": "))
total1 = int(input("Enter total topics for " + subject1 + ": "))

completed2 = int(input("Enter completed topics for " + subject2 + ": "))
total2 = int(input("Enter total topics for " + subject2 + ": "))

completed3 = int(input("Enter completed topics for " + subject3 + ": "))
total3 = int(input("Enter total topics for " + subject3 + ": "))

completed4 = int(input("Enter completed topics for " + subject4 + ": "))
total4 = int(input("Enter total topics for " + subject4 + ": "))


progress1 = (completed1 / total1) * 100
progress2 = (completed2 / total2) * 100
progress3 = (completed3 / total3) * 100
progress4 = (completed4 / total4) * 100


print("\n", subject1, "Progress:", round(progress1, 2), "%")
print(subject2, "Progress:", round(progress2, 2), "%")
print(subject3, "Progress:", round(progress3, 2), "%")
print(subject4, "Progress:", round(progress4, 2), "%")


overall_progress = (
    progress1 + progress2 + progress3 + progress4
) / 4

print("\nOverall Progress:",
      round(overall_progress, 2), "%")


# ==========================================================
# FINAL DASHBOARD
# ==========================================================

print("\n\n==============================================")
print("           STUDYMATE AI DASHBOARD")
print("==============================================")

print("\nStudent:", name)
print("Course:", course)
print("Semester:", semester)

print("\n---------- SUBJECT SUMMARY ----------")

print(subject1,
      "| Marks:", marks1,
      "| Attendance:", attendance1,
      "| Priority:", priority1)

print(subject2,
      "| Marks:", marks2,
      "| Attendance:", attendance2,
      "| Priority:", priority2)

print(subject3,
      "| Marks:", marks3,
      "| Attendance:", attendance3,
      "| Priority:", priority3)

print(subject4,
      "| Marks:", marks4,
      "| Attendance:", attendance4,
      "| Priority:", priority4)


print("\n---------- STUDY PLAN ----------")

print(subject1, ":", hours1, "hours/day")
print(subject2, ":", hours2, "hours/day")
print(subject3, ":", hours3, "hours/day")
print(subject4, ":", hours4, "hours/day")

print("\nOverall Progress:",
      round(overall_progress, 2), "%")

print("\n==============================================")
print("      StudyMate AI Analysis Completed")
print("==============================================")





