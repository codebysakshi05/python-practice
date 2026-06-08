print("===== AI Resume Analyzer =====")

candidate_skills = input("Enter your skills (comma separated): ")
job_skills = input("Enter required job skills (comma separated): ")

candidate = [skill.strip().lower() for skill in candidate_skills.split(",")]
job = [skill.strip().lower() for skill in job_skills.split(",")]

matched = []
missing = []

# Find matched skills
for skill in job:
    if skill in candidate:
        matched.append(skill)
    else:
        missing.append(skill)

# Match Score
match_score = (len(matched) / len(job)) * 100

print("\n===== ANALYSIS REPORT =====")

print("\nMatched Skills:")
for skill in matched:
    print("-", skill.title())

print("\nMissing Skills:")
for skill in missing:
    print("-", skill.title())

print(f"\nMatch Score: {match_score:.2f}%")

# Job Readiness
print("\nJob Readiness Status:")
if match_score >= 80:
    print("✅ Job Ready")
elif match_score >= 60:
    print("🟡 Almost Ready")
else:
    print("🔴 Needs Improvement")

# Learning Suggestions
learning_resources = {
    "python": "Learn Python functions, OOP and projects",
    "sql": "Practice JOINs, GROUP BY and Subqueries",
    "excel": "Learn Pivot Tables and Dashboards",
    "power bi": "Learn DAX and Interactive Dashboards",
    "git": "Learn Commits, Branches and GitHub",
    "react": "Build projects using React and APIs",
    "javascript": "Learn DOM and ES6 concepts"
}

print("\nLearning Suggestions:")
for skill in missing:
    if skill in learning_resources:
        print(f"{skill.title()} -> {learning_resources[skill]}")

# Career Recommendations
print("\nRecommended Careers:")

if "python" in candidate and "sql" in candidate:
    print("- Data Analyst")
    print("- Python Developer")

if "excel" in candidate and "sql" in candidate:
    print("- Business Analyst")

if "python" in candidate and "javascript" in candidate:
    print("- Full Stack Developer")

if "python" in candidate and "power bi" in candidate:
    print("- Data Analytics Engineer")

# Interview Questions
questions = {
    "python": [
        "What is a list?",
        "Difference between list and tuple?",
        "What are functions?"
    ],
    "sql": [
        "What is JOIN?",
        "Difference between WHERE and HAVING?",
        "What is a Primary Key?"
    ],
    "excel": [
        "What is a Pivot Table?",
        "What is VLOOKUP?",
        "How do you create dashboards?"
    ]
}

print("\nInterview Questions To Practice:")

for skill in candidate:
    if skill in questions:
        print(f"\n{skill.title()} Questions:")
        for q in questions[skill]:
            print("-", q)

print("\n===== END OF REPORT =====")