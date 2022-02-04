
class Student:
    def __init__(self, name, age, subject="student"):
        self.name = name
        self.age = age
        self.subject = subject 

    def __repr__(self):
        return f"{self.name} is {self.age} years old from subject {self.subject}"

    def grade(self, score1, score2, score3):
        result = (score1 + score2 + score3) / 3
        return f"{self.name}'s ave test score is {result}"

        
