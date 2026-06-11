def analyze_student(cgpa, skills):
    print("\n===== AI ANALYSIS REPORT =====")

    if cgpa >= 8.5:
        print("Performance: Excellent")
    elif cgpa >= 7:
        print("Performance: Good")
    else:
        print("Performance: Needs Improvement")

    skills = skills.lower()

    print("\nCareer Suggestions:")

    if "python" in skills:
        print("- Python Developer")

    if "data analytics" in skills:
        print("- Data Analyst")

    if "sql" in skills:
        print("- Database Analyst")

    if "ai" in skills:
        print("- AI Engineer")

    if "power bi" in skills:
        print("- Business Intelligence Analyst")

    print("\nLearning Suggestions:")

    if "python" not in skills:
        print("- Learn Python")

    if "sql" not in skills:
        print("- Learn SQL")

    if "power bi" not in skills:
        print("- Learn Power BI")

    if "excel" not in skills:
        print("- Learn Excel")


print("====================================")
print(" SMART AI STUDENT DATABASE SYSTEM ")
print("====================================")

student = {}

student["name"] = input("Enter Name: ")
student["age"] = int(input("Enter Age: "))
student["course"] = input("Enter Course: ")
student["college"] = input("Enter College: ")
student["cgpa"] = float(input("Enter CGPA: "))
student["skills"] = input("Enter Skills (comma separated): ")
student["interest"] = input("Enter Interest Area (AI/Data Analytics/Web Development): ")
student["graduation_year"] = input("Enter Graduation Year: ")

print("\n===== STUDENT PROFILE =====")

for key, value in student.items():
    print(key.title(), ":", value)

analyze_student(student["cgpa"], student["skills"])

print("\n===== ROADMAP =====")

interest = student["interest"].lower()

if interest == "ai":
    print("Python → SQL → Machine Learning → AI Projects")

elif interest == "data analytics":
    print("Excel → SQL → Power BI → Python → Analytics Projects")

elif interest == "web development":
    print("HTML → CSS → JavaScript → React → Full Stack Projects")

else:
    print("Keep learning Python and building projects")

save = input("\nDo you want to save profile? (yes/no): ")

if save.lower() == "yes":

    file = open("student_profiles.txt", "a")

    file.write("\n====================\n")
    file.write("Name: " + student["name"] + "\n")
    file.write("Age: " + str(student["age"]) + "\n")
    file.write("Course: " + student["course"] + "\n")
    file.write("College: " + student["college"] + "\n")
    file.write("CGPA: " + str(student["cgpa"]) + "\n")
    file.write("Skills: " + student["skills"] + "\n")
    file.write("Interest: " + student["interest"] + "\n")
    file.write("Graduation Year: " + student["graduation_year"] + "\n")

    file.close()

    print("Profile Saved Successfully!")

else:
    print("Profile Not Saved.")

print("\nThank You For Using AI Student Database System!")