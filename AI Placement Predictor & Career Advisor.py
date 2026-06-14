print("=" * 50)
print("     AI PLACEMENT PREDICTOR & CAREER ADVISOR ")
print("=" * 50)

name = input("Enter Name: ")

cgpa = float(input("Enter CGPA (0-10): "))
python_skill = int(input("Python Skill (1-10): "))
sql_skill = int(input("SQL Skill (1-10): "))
communication = int(input("Communication Skill (1-10): "))
powerbi_skill = int(input("Power BI Skill (1-10): "))

print("\nCalculating Placement Readiness...\n")

# Placement Score Calculation
placement_score = (
    (cgpa * 10 * 0.4) +
    (python_skill * 10 * 0.25) +
    (sql_skill * 10 * 0.15) +
    (communication * 10 * 0.10) +
    (powerbi_skill * 10 * 0.10)
)

print("=" * 50)
print("PLACEMENT ANALYSIS REPORT")
print("=" * 50)

print("Name :", name)
print("Placement Score :", round(placement_score, 2), "%")

# Placement Prediction

if placement_score >= 85:
    prediction = "Excellent Placement Chance"
elif placement_score >= 70:
    prediction = "Good Placement Chance"
elif placement_score >= 50:
    prediction = "Moderate Placement Chance"
else:
    prediction = "Low Placement Chance"

print("Prediction :", prediction)

# Strongest Skill

skills = {
    "Python": python_skill,
    "SQL": sql_skill,
    "Communication": communication,
    "Power BI": powerbi_skill
}

strongest_skill = max(skills, key=skills.get)

print("Strongest Skill :", strongest_skill)

# Career Recommendation

if python_skill >= 8 and sql_skill >= 7:
    career = "Data Analyst"
elif python_skill >= 8:
    career = "Python Developer"
elif communication >= 8:
    career = "Business Analyst"
elif powerbi_skill >= 8:
    career = "Power BI Developer"
else:
    career = "Software Engineer"

print("Recommended Career :", career)

# Internship Eligibility

if placement_score >= 60:
    internship = "Eligible"
else:
    internship = "Not Eligible"

print("Internship Eligibility :", internship)

# Missing Skills

missing_skills = []

if python_skill < 7:
    missing_skills.append("Python")

if sql_skill < 7:
    missing_skills.append("SQL")

if communication < 7:
    missing_skills.append("Communication")

if powerbi_skill < 7:
    missing_skills.append("Power BI")

print("\nSkill Gap Analysis")

if len(missing_skills) == 0:
    print("No Major Skill Gaps Found")
else:
    print("Need Improvement In:")
    for skill in missing_skills:
        print("-", skill)

# Learning Duration Estimate

months = len(missing_skills) * 1.5

print("\nEstimated Learning Time :", months, "Months")

# Salary Prediction

salary_data = {
    "Data Analyst": "₹4-8 LPA",
    "Python Developer": "₹5-10 LPA",
    "Business Analyst": "₹4-9 LPA",
    "Power BI Developer": "₹4-8 LPA",
    "Software Engineer": "₹4-7 LPA"
}

print("Expected Salary Range :", salary_data[career])

# AI Recommendation

print("\nAI Recommendations")

if placement_score < 50:
    print("Focus on fundamentals and build mini projects.")
elif placement_score < 70:
    print("Improve technical skills and GitHub portfolio.")
elif placement_score < 85:
    print("Start applying for internships and certifications.")
else:
    print("You are industry-ready. Focus on advanced projects.")

# Save Report

save = input("\nSave Report? (yes/no): ").lower()

if save == "yes":

    file = open("placement_report.txt", "w", encoding="utf-8")

    file.write("AI Placement Predictor Report\n")
    file.write("=" * 40 + "\n")

    file.write("Name: " + name + "\n")
    file.write("Placement Score: " + str(round(placement_score, 2)) + "%\n")
    file.write("Prediction: " + prediction + "\n")
    file.write("Strongest Skill: " + strongest_skill + "\n")
    file.write("Recommended Career: " + career + "\n")
    file.write("Internship Eligibility: " + internship + "\n")
    file.write("Salary Range: " + salary_data[career] + "\n")

    file.close()

    print("Report Saved Successfully!")

print("\nThank You For Using AI Placement Predictor ")