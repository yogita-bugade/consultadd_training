'''Write a program that accepts a string as an input from the user and calculate the number of digits
and letters.
Sample input: consul72
Expected output: Letters 6 Digits 2'''
input_string = "consul72"

num_letters = 0
num_digits = 0

for char in input_string:
    if char.isalpha():
        num_letters += 1
    elif char.isdigit():
        num_digits += 1

print("Letters:", num_letters, "Digits:", num_digits)
