'''Write a program to check the data type of the entered values.
HINT: Printed output should say - The data type of the input value is : int/float/string/etc'''
user_input = input("Enter a value: ")
data_type = type(user_input).__name__
print("The data type of the input value is:", data_type)
