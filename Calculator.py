
import os

number = float(input(" Enter  number :"))
number2 = float(input("Enter  number :"))

print(" 1- Multiplication"
      " 2- Division"
      " 3- Subtraction"
      " 4- Addition")

os.system("cls")
select_operation = int(input("Choose(1-4):"))

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")



if select_operation == 1:
    result = number * number2
    operation = "*"
    print(f"{number}{operation}{number2} ={result}")
elif select_operation == 2:
    result = number / number2
    operation = ":"
    print(f"{number}{operation}{number2} ={result}")
elif select_operation == 3:
    result = number - number2
    operation = "-"
    print(f"{number}{operation}{number2} ={result}")
elif select_operation == 4:
    result = number + number2
    operation = "+"
    print(f"{number}{operation}{number2} ={result}")
else:
    print("You don't follow instruction donkey")


# 2

