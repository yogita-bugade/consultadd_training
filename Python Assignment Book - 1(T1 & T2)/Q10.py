'''Write a program in Python to perform the following operator based task:
Ask user to choose the following option first:
If User Enter 1 - Addition
If User Enter 2 - Subtraction
If User Enter 3 - Division
If User Enter 4 - Multiplication
If User Enter 5 - Average
Ask user to enter two numbers and keep those numbers in variables num1 and num2
respectively for the first 4 options mentioned above.
Ask the user to enter two more numbers as first and second for calculating the average as
soon as the user chooses an option 5.
At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
NOTE: At a time a user can only perform one action.'''
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def division(num1, num2):
    if num2 == 0:
        return "Undefined"
    return num1 / num2

def multiplication(num1, num2):
    return num1 * num2

def average(first, second):
    return (first + second) / 2

def perform_operation(choice):
    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = addition(num1, num2)
    elif choice == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = subtraction(num1, num2)
    elif choice == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = division(num1, num2)
    elif choice == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = multiplication(num1, num2)
    elif choice == 5:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))
        result = average(first, second)
    else:
        result = "Invalid choice"

    if result == "NEGATIVE":
        print("NEGATIVE")
    else:
        print("Result:", result)

print("Choose an option:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Division")
print("4 - Multiplication")
print("5 - Average")
choice = int(input("Enter your choice: "))

perform_operation(choice)
