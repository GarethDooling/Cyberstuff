from budgetclass import Budget

food = Budget(200)
bills = Budget(150)
entertainment = Budget(400)

print(food)
print(bills)
print(entertainment)

food.withdraw(50)
print()
print(food)

food.deposit(500)
print()
print(food)

entertainment.deposit(food.withdraw(50))

print()
print(food)
print(entertainment)