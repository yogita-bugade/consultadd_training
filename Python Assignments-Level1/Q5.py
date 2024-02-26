'''Write a Python program to find the factorial of a number using a
for loop.'''
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i
    return fact

number = int(input("Enter a number: "))
result = factorial(number)
print(f"Factorial of the given number is {result}")