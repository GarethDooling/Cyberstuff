
print("Welcome to the tip calculator!")
bill = float(input("How much was the bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15%? "))
people = int(input("How many people to split the bill? "))
dutch = (bill + bill / 100 * tip) / people
#dutch_round = round(dutch, 2)
dutch_round = "{:.2f}".format(dutch)
print(f"Each person should pay ${dutch_round}")






