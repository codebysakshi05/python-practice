print("======================================")
print(" AI STUDENT PERFORMANCE DASHBOARD V2 ")
print("======================================")

students = []

n = int(input("How many students? "))

for i in range(n):

    name = input(f"\nEnter Student {i+1} Name: ")
    marks = float(input(f"Enter {name}'s Marks: "))

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"

    student = {
        "name": name,
        "marks": marks,
        "grade": grade
    }

    students.append(student)

all_marks = [student["marks"] for student in students]

average = sum(all_marks) / len(all_marks)

highest_student = max(students, key=lambda x: x["marks"])
lowest_student = min(students, key=lambda x: x["marks"])

passed = 0

for student in students:
    if student["marks"] >= 35:
        passed += 1

failed = len(students) - passed

print("\n==============================")
print(" DASHBOARD REPORT ")
print("==============================")

print("Total Students :", len(students))
print("Average Marks :", round(average, 2))

print("\nTop Performer")
print(highest_student["name"], "-", highest_student["marks"])

print("\nLowest Performer")
print(lowest_student["name"], "-", lowest_student["marks"])

print("\nPass Count :", passed)
print("Fail Count :", failed)

print("\n===== STUDENT REPORTS =====")

for student in students:

    print(
        student["name"],
        "| Marks:", student["marks"],
        "| Grade:", student["grade"]
    )

print("\n===== AI INSIGHTS =====")

if average >= 80:
    print("Class Performance: Excellent")

elif average >= 60:
    print("Class Performance: Good")

else:
    print("Class Performance: Needs Improvement")

if failed > 0:
    print("Recommendation: Provide extra support to weak students.")
else:
    print("Recommendation: Excellent consistency across class.")

save = input("\nSave Report? (yes/no): ")

if save.lower() == "yes":

    file = open(
        "student_dashboard_report.txt",
        "a",
        encoding="utf-8"
    )

    file.write("\n=========================\n")
    file.write("AI STUDENT DASHBOARD REPORT\n")
    file.write("=========================\n")

    file.write("Total Students: " + str(len(students)) + "\n")
    file.write("Average Marks: " + str(round(average, 2)) + "\n")

    file.write(
        "Top Performer: "
        + highest_student["name"]
        + " - "
        + str(highest_student["marks"])
        + "\n"
    )

    file.write(
        "Lowest Performer: "
        + lowest_student["name"]
        + " - "
        + str(lowest_student["marks"])
        + "\n"
    )

    file.write("Pass Count: " + str(passed) + "\n")
    file.write("Fail Count: " + str(failed) + "\n\n")

    for student in students:

        file.write(
            student["name"]
            + " | Marks: "
            + str(student["marks"])
            + " | Grade: "
            + student["grade"]
            + "\n"
        )

    file.close()

    print("Report Saved Successfully!")