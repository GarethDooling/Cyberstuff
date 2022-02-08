class Student:

    def __init__(self, name, age, class_="student"):
        self.name = name
        self.age = age
        self.class_ = class_

John = Student("John", "21", "IT")
Jane = Student("Jane", "22")
Jack = Student("Jack", "23", "Science")

print(getattr(Jack, "class_"))
