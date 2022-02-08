
from budgetclass import Budget

listofcurrentbudgets = []

working = True

while working:
    print("Menu: 1. Instantiate Budgets  2. View Budgets  3. Edit Budgets")
    control = int(input("Please enter your choice: "))

    if control == 1:
        food = Budget(100, "food")
        listofcurrentbudgets.append(food)
        bills = Budget(30, "bills")
        listofcurrentbudgets.append(bills)

    elif control == 2:
        control2 = True
        while control2:
            print(f"You have {str(len(listofcurrentbudgets))} current budgets")
            numberedbudgets = 1
            for item in listofcurrentbudgets:
                print(f"{numberedbudgets}: {item.name}")
                numberedbudgets += 1
            userchoice1 = input("Which budget do you want?: ")
    elif control == 9:
        working = False