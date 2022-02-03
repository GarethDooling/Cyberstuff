'''def func1(num1, num2, num3, num4, num5):
  control = 0
  list1 = [num1, num2, num3, num4, num5]
  return list1

print(func1(1,2,3,4,5)) THIS IS FUNCTION COS PRINT OUTSIDE

def func2(num1, num2, num3, num4, num5):
  control = 0
  list2 = [num1, num2, num3, num4, num5]
  print(list2) THIS IS PROCEDURE COS PRINT INSIDE
  '''  

def func1(name, hwork, assess, final):
  answer = (hwork + assess + final) / 175 * 100
  return f"{name} your total score is {answer}%"

print(func1("Gaz", 25, 50, 100))
print(func1("Taz", 12.5, 25, 50))

#this one works!!!!!






