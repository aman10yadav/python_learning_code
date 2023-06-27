import math

def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def sqrt(num):
    return math.sqrt(num)

def Square(num):
    return num ** 2

def sin(num):
    return math.sin(num)

def cosine(num):
    return math.cos(num)

def tan(num):
    return math.tan(num)


print("""
Choose a number for the following operations =>
1. Addition
2. Substraction(number1, number2)
3. Multiplication(number1, number2)
4. Divide(number1, number2)
5. Square(number)
6. SquareRoot(number)
7. Sin(number)
8. cos(number)
9. tan(number)
""")

choice = int(input("Which type of operation you want to perform ? : "))
while choice < 10:
    if choice == 1:
        print("Enter the numbers to add")
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        result = add(num1, num2)
        print(f'Addition of {num1} and {num2} is {result}')

    elif choice == 2:
        print("Enter the numbers to substract : ")
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        result = substract(num1, num2)
        print(f'Substraction of {num1} and {num2} is {result}')

    elif choice == 3:
        print("Enter the numbers to multiply : ")
        num1 = int(input("Enter FirstNumbers : "))
        num2 = int(input("Enter Second Numbers : "))
        result = multiply(num1, num2)
        print(f'Multiplication of {num1} and {num2} is {result}')

    elif choice == 4:
        print("Enter the numbers to divide :")
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        result = divide(num1, num2)
        print(f'Division of {num1} and {num2} is {result}')
    
    elif choice == 5:
        print("Enter the number to square : ")
        num = int(input("Enter the number : "))
        result = Square(num)
        print(f'Square of {num} is {result}')

    elif choice == 6:
        print("Enter the number to find square root : ")
        num = int(input("Enter the number : "))
        result = sqrt(num)
        print(f'Square root of {num} is {result}')

    elif choice == 7:
        print("Enter the number to find sine : ")
        num = int(input("Enter the number : "))
        result = sin(num)
        print(f'Sin of {num} is {result}')

    elif choice == 8:
        print("Enter the number to find cosine : ")
        num = int(input("Enter the number : "))
        result = cosine(num)
        print(f'Cosine of {num} is {result}')

    elif choice == 9:
        print("Enter the number to find tangent : ")
        num = int(input("Enter the number : "))
        result = tan(num)
        print(f'Tangent of {num} is {result}')

    else :
        print("Choose a valid operation !!")

    newChoice = int(input("Do you want to continue - press 1 for 'Yes' and press 2 for 'No' : "))

    if newChoice == 1:
        choice = int(input("Which type of operation you want to perform ? : "))
    elif newChoice == 2:
        print("Thank you for using our scientific calculator !!")
        break

