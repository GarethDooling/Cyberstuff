'''def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

Create a new python file. In that file create a program that works out a grade based on marks with the use of functions.
The program should take the students name, homework score (/25), assessment score (/50) and final exam score (/100) as inputs, and output their name and final ICT grade as a percentage.

Reminder: any inputs and prints should not be included inside the function definition, and should strictly be done outside.

Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)

def greet(name):
    return f"Hello {name}"

name = input("What is your name? ")
print(greet(name))'''

name = input("What's your name? ") 
homework = input("Please enter your homework score: ")
assessment = input("Please enter your assessment score: ")
final = input("Please enter your final score: ")

def exams (hscore, ascore, fscore):
  answer = (hscore + ascore + fscore) / 125 * 100
  return answer 

print(name)
print(homework)
print(assessment)
print(final) 






