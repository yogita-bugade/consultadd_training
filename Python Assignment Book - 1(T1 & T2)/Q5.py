'''Write a program to complete the task given below:
Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output'''
num1 = int(input("Enter the first number (between 1 and 10): "))
num2 = int(input("Enter the second number (between 1 and 10): "))

z = num1 + num2
result = z + 30

print("The result is:", result)
