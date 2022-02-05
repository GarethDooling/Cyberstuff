age = input("What is your current age?")

#You have 12410 days, 1768 weeks, and 408 months left.

years_left = 90 - int(age)
days = years_left * 365
weeks = years_left * 52
months = years_left * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
