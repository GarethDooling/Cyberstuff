# class Profile():
#     def __init__(self, name, age, email):
#         self.name = name
#         self.age = age
#         self.email = email
    
#     def __repr__(self):
#         return f"{self.name} is {self.age} years old whose email is {self.email}."

# person1 = Profile("Anne", 20, "anne@com")
# person2 = Profile("Bob", 21, "bob@com")
# person3 = Profile("Col", 22, "col@com")

# print(person1)
# print(person2)
# print(person3)


from appclasses import Student

Anne = Student("Anne", 20, "Comp")
Bill = Student("Bill", 25)

print(Anne.grade(25, 50, 75))








