'''Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.'''

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

t = (name1 + name2).lower().count("t")
r = (name1 + name2).lower().count("r")
u = (name1 + name2).lower().count("u")
e = (name1 + name2).lower().count("e")
first = t + r + u + e

l = (name1 + name2).lower().count("l")
o = (name1 + name2).lower().count("o")
v = (name1 + name2).lower().count("v")
e = (name1 + name2).lower().count("e")
second = l + o + v + e

final = (str(first) + str(second)) 
score = int(final)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 39 and score < 51:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")



