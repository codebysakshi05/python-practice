print("=" * 60)
print(" AI PERSONAL FINANCE & BUDGET INTELLIGENCE SYSTEM  ")
print("=" * 60)

name = input("Enter Name: ")

income = float(input("Monthly Income (₹): "))

food = float(input("Food Expense (₹): "))
travel = float(input("Travel Expense (₹): "))
shopping = float(input("Shopping Expense (₹): "))
entertainment = float(input("Entertainment Expense (₹): "))
education = float(input("Education Expense (₹): "))
other = float(input("Other Expense (₹): "))

categories = {
    "Food": food,
    "Travel": travel,
    "Shopping": shopping,
    "Entertainment": entertainment,
    "Education": education,
    "Other": other
}

total_expense = sum(categories.values())

savings = income - total_expense

savings_percent = (savings / income) * 100

budget_score = 100 - ((total_expense / income) * 100)

if budget_score < 0:
    budget_score = 0

highest_category = max(categories, key=categories.get)

print("\n" + "=" * 60)
print(" FINANCIAL ANALYTICS DASHBOARD ")
print("=" * 60)

print("Name:", name)
print("Income: ₹", income)
print("Total Expense: ₹", total_expense)
print("Savings: ₹", savings)

print("\nBudget Score:", round(budget_score, 2), "/100")

if budget_score >= 80:
    health = "Excellent"

elif budget_score >= 60:
    health = "Good"

elif budget_score >= 40:
    health = "Average"

else:
    health = "Poor"

print("Financial Health:", health)

print("\nHighest Spending Category:", highest_category)

print("\nExpense Percentage Analysis")

for category, amount in categories.items():

    percentage = (amount / income) * 100

    print(category, ":", round(percentage, 2), "%")

print("\nExpense Ranking")

sorted_expenses = sorted(
    categories.items(),
    key=lambda x: x[1],
    reverse=True
)

for rank, item in enumerate(sorted_expenses, start=1):

    print(rank, ".", item[0], "- ₹", item[1])

print("\nOverspending Alerts")

for category, amount in categories.items():

    if amount > income * 0.30:

        print("⚠ High Spending in", category)

print("\nFuture Savings Projection")

future_savings = savings * 12

print("Expected Yearly Savings: ₹", round(future_savings, 2))

print("\nAI Recommendation")

if budget_score < 40:
    print("Reduce unnecessary spending immediately.")

elif budget_score < 60:
    print("Create a monthly budget and track expenses.")

elif budget_score < 80:
    print("Increase investments and emergency savings.")

else:
    print("Excellent financial management. Focus on wealth creation.")

save = input("\nSave Report? (yes/no): ").lower()

if save == "yes":

    file = open("finance_report.txt", "w", encoding="utf-8")

    file.write("AI Finance Intelligence Report\n")
    file.write("=" * 50 + "\n")

    file.write("Name: " + name + "\n")
    file.write("Income: ₹" + str(income) + "\n")
    file.write("Expense: ₹" + str(total_expense) + "\n")
    file.write("Savings: ₹" + str(savings) + "\n")
    file.write("Budget Score: " + str(round(budget_score, 2)) + "\n")
    file.write("Financial Health: " + health + "\n")
    file.write("Highest Category: " + highest_category + "\n")

    file.close()

    print("Report Saved Successfully!")

print("\nThank You For Using AI Finance Intelligence System")