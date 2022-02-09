
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num = len(names)
num_length = random.randint(0,num - 1)
loser = names[num_length]
print(f"{loser} is going to buy the meal today!")

