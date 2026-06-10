print("===================================")
print(" AI STUDENT PROFILE ANALYZER ")
print("===================================")

student = {}

student["name"] = input("Enter Name: ")
student["age"] = int(input("Enter Age: "))
student["course"] = input("Enter Course: ")
student["college"] = input("Enter College: ")
student["cgpa"] = float(input("Enter CGPA: "))
student["skills"] = input("Enter Skills (comma separated): ")

print("\n===================================")
print(" STUDENT PROFILE ")
print("===================================")

for key, value in student.items():
    print(key.title(), ":", value)

print("\n===================================")
print(" AI ANALYSIS REPORT ")
print("===================================")

cgpa = student["cgpa"]

if cgpa >= 8.5:
    print("Performance: Excellent")
elif cgpa >= 7:
    print("Performance: Good")
else:
    print("Performance: Needs Improvement")

skills = student["skills"].lower()

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

print("\n===================================")
print(" PROFILE ANALYSIS COMPLETE ")
print("===================================")