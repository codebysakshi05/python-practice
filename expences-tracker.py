print("personal expences tracker")

food = float(input("enter food expences:"))
travel = float(input("enter travel expences:"))
shopping = float(input("enter shopping expences"))

total = food + travel + shopping

print("total expences:", total)

highest = max(food, travel, shopping)

print("highest expences:", highest)

if highest == food:
    print("food expences is highest")
elif highest == travel:
    print("travel expences is highest")
else:
    print("shopping expences is highest")

