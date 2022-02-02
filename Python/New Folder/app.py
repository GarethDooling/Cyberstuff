'''Create 2 new Python files. In one file, write a function that will generate a number between 1 and 6. Make this a module called dice.

In the second file, use the dice module to simulate throwing 2 dice and print the values you get from the dice.

import math
import random

def dice():
    return math.ceil(random.randint(1, 6))

for _ in range(2):
    print(dice())
    
In a new Python file, create a class of students.

It should contain the following attributes: name, age, and class with default value "student".

It should also contain a method which takes in 3 test scores and prints the students average test score.'''

import student 

def testcalc(number1, number2, number3):
    answer = (number1 + number2 + number3)/300*100
    return answer

testave = testcalc(5,10,15)
print(testave)