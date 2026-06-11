print("====================================")
print(" AI CAREER SKILL GAP ANALYZER V2 ")
print("====================================")

roles = {
    "data analyst": {
        "skills": ["python", "excel", "sql", "power bi", "statistics"],
        "salary": "₹4-12 LPA",
        "duration": "4-6 Months"
    },

    "ai engineer": {
        "skills": ["python", "sql", "machine learning", "deep learning", "ai"],
        "salary": "₹6-20 LPA",
        "duration": "8-12 Months"
    },

    "web developer": {
        "skills": ["html", "css", "javascript", "react", "git"],
        "salary": "₹3-10 LPA",
        "duration": "4-8 Months"
    }
}

skills = input("Enter Your Skills (comma separated): ").lower()
dream_role = input("Enter Dream Role: ").lower()

user_skills = skills.split(",")
user_skills = [skill.strip() for skill in user_skills]

if dream_role in roles:

    required_skills = roles[dream_role]["skills"]

    matched = 0
    missing = []

    for skill in required_skills:

        if skill in user_skills:
            matched += 1
        else:
            missing.append(skill)

    score = (matched / len(required_skills)) * 100

    print("\n========== AI REPORT ==========")

    print("Dream Role :", dream_role.title())
    print("Match Score :", round(score, 2), "%")

    print("\nMissing Skills:")

    if len(missing) == 0:
        print("No Missing Skills")
    else:
        for skill in missing:
            print("-", skill.title())

    print("\nCareer Readiness:")

    if score >= 80:
        readiness = "Job Ready"
    elif score >= 60:
        readiness = "Almost Ready"
    else:
        readiness = "Learning Phase"

    print(readiness)

    print("\nEstimated Salary Range:")
    print(roles[dream_role]["salary"])

    print("\nEstimated Learning Time:")
    print(roles[dream_role]["duration"])

    print("\nRecommended Learning Path:")

    if len(missing) == 0:
        print("Build Projects and Apply for Jobs")
    else:
        for skill in missing:
            print("→ Learn", skill.title())

    save = input("\nSave Report? (yes/no): ")

    if save.lower() == "yes":

        file = open(
            "career_reports.txt",
            "a",
            encoding="utf-8"
        )

        file.write("\n========================\n")
        file.write("Dream Role: " + dream_role + "\n")
        file.write("Match Score: " + str(round(score, 2)) + "%\n")
        file.write("Readiness: " + readiness + "\n")
        file.write("Salary: " + roles[dream_role]["salary"] + "\n")
        file.write("Learning Time: " + roles[dream_role]["duration"] + "\n")

        file.write("Missing Skills:\n")

        if len(missing) == 0:
            file.write("No Missing Skills\n")
        else:
            for skill in missing:
                file.write("- " + skill + "\n")

        file.close()

        print("Report Saved Successfully!")

    else:
        print("Report Not Saved.")

else:
    print("Role Not Found")

print("\nThank You For Using AI Career Skill Gap Analyzer!")