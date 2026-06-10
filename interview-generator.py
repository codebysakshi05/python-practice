print("=================================")
print(" AI INTERVIEW PREPARATION ASSISTANT ")
print("=================================")

python_questions = {
    "What is a list?": "A list is an ordered and mutable collection.",
    "What is a tuple?": "A tuple is ordered and immutable.",
    "What is a function?": "A function is a reusable block of code."
}

sql_questions = {
    "What is SQL?": "SQL is used to manage databases.",
    "What is a Primary Key?": "A primary key uniquely identifies a record.",
    "What is JOIN?": "JOIN combines data from multiple tables."
}

excel_questions = {
    "What is VLOOKUP?": "Used to search data vertically.",
    "What is a Pivot Table?": "Used to summarize data.",
    "What is Conditional Formatting?": "Highlights cells based on conditions."
}


def start_quiz(questions):
    score = 0

    for question, answer in questions.items():
        print("\nQuestion:")
        print(question)

        user_answer = input("Your Answer: ")

        print("Expected Answer:")
        print(answer)

        choice = input("Did your answer match? (yes/no): ")

        if choice.lower() == "yes":
            score += 1

    return score


def show_result(score, total):
    percentage = (score / total) * 100

    print("\n======================")
    print(" INTERVIEW REPORT ")
    print("======================")

    print("Score:", score, "/", total)
    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Status: Interview Ready")
    elif percentage >= 60:
        print("Status: Almost Ready")
    else:
        print("Status: Needs Improvement")


def show_career(skill):
    print("\nCareer Suggestions:")

    if skill == "python":
        print("- Python Developer")
        print("- Automation Engineer")
        print("- AI Engineer")

    elif skill == "sql":
        print("- Data Analyst")
        print("- Database Developer")

    elif skill == "excel":
        print("- Business Analyst")
        print("- Data Analyst")


print("\nAvailable Skills")
print("1. Python")
print("2. SQL")
print("3. Excel")

skill = input("\nChoose a skill: ").lower()

if skill == "python":
    score = start_quiz(python_questions)
    show_result(score, len(python_questions))
    show_career("python")

elif skill == "sql":
    score = start_quiz(sql_questions)
    show_result(score, len(sql_questions))
    show_career("sql")

elif skill == "excel":
    score = start_quiz(excel_questions)
    show_result(score, len(excel_questions))
    show_career("excel")

else:
    print("Invalid Skill Selected")

print("\nThank you for using AI Interview Assistant")