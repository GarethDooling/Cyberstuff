import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

number = random.randint(0,1)

if number == 0:
    print("Tails")
else:
    print("Heads")




