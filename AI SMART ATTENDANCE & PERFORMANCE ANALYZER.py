print("=" * 55)
print(" AI SMART ATTENDANCE & PERFORMANCE ANALYZER V2 ")
print("=" * 55)

name = input("Enter Student Name: ")

attendance = float(input("Enter Attendance Percentage: "))
marks = float(input("Enter Marks (0-100): "))

# Data Validation

if attendance < 0 or attendance > 100:
    print("Invalid Attendance Percentage")
    exit()

if marks < 0 or marks > 100:
    print("Invalid Marks")
    exit()

print("\nGenerating AI Analysis...\n")

# Grade Calculation

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

# Attendance Status

if attendance >= 85:
    attendance_status = "Excellent"
elif attendance >= 75:
    attendance_status = "Good"
elif attendance >= 60:
    attendance_status = "Average"
else:
    attendance_status = "Poor"

# Academic Performance

if marks >= 85:
    performance = "Excellent"
elif marks >= 70:
    performance = "Good"
elif marks >= 50:
    performance = "Average"
else:
    performance = "Needs Improvement"

# Risk Detection

if attendance < 75 and marks < 50:
    risk = "High Risk"
elif attendance < 75 or marks < 50:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"

# Student Category

if attendance >= 85 and marks >= 85:
    category = "Top Performer"

elif attendance >= 75 and marks >= 70:
    category = "Consistent Student"

elif attendance >= 75 and marks < 70:
    category = "Needs Academic Improvement"

elif attendance < 75 and marks >= 70:
    category = "Attendance Defaulter"

else:
    category = "Critical Attention Required"

# Readiness Score

readiness_score = (attendance * 0.4) + (marks * 0.6)

# AI Recommendation

if readiness_score >= 85:
    recommendation = "Excellent progress. Start advanced projects and internships."

elif readiness_score >= 70:
    recommendation = "Good performance. Improve technical skills consistently."

elif readiness_score >= 50:
    recommendation = "Focus on academics and regular attendance."

else:
    recommendation = "Immediate improvement required in both attendance and studies."

# Scholarship Eligibility

if attendance >= 85 and marks >= 85:
    scholarship = "Eligible"

else:
    scholarship = "Not Eligible"

# Report

print("=" * 55)
print(" STUDENT ANALYSIS REPORT ")
print("=" * 55)

print("Name :", name)
print("Attendance :", attendance, "%")
print("Marks :", marks)
print("Grade :", grade)

print("\nAttendance Status :", attendance_status)
print("Performance :", performance)

print("\nRisk Level :", risk)

print("Student Category :", category)

print("Readiness Score :", round(readiness_score, 2))

print("Scholarship Eligibility :", scholarship)

print("\nAI Recommendation :")
print(recommendation)

# Save Report

save = input("\nSave Report? (yes/no): ").lower()

if save == "yes":

    file = open("student_analysis_report.txt", "w", encoding="utf-8")

    file.write("AI Smart Attendance & Performance Analyzer V2\n")
    file.write("=" * 50 + "\n")

    file.write("Name: " + name + "\n")
    file.write("Attendance: " + str(attendance) + "%\n")
    file.write("Marks: " + str(marks) + "\n")
    file.write("Grade: " + grade + "\n")
    file.write("Attendance Status: " + attendance_status + "\n")
    file.write("Performance: " + performance + "\n")
    file.write("Risk Level: " + risk + "\n")
    file.write("Student Category: " + category + "\n")
    file.write("Readiness Score: " + str(round(readiness_score, 2)) + "\n")
    file.write("Scholarship Eligibility: " + scholarship + "\n")
    file.write("Recommendation: " + recommendation + "\n")

    file.close()

    print("\nReport Saved Successfully!")

print("\nThank You For Using AI Smart Attendance Analyzer")