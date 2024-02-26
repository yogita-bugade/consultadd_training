'''Write a program that accepts a string as input from the user and
calculates the number of digits and letters.
Input: Hello123
Output: Alphabets: 5 & Number : 3'''
def count_letters_and_digits(input_string):
    num_letters = 0
    num_digits = 0

    for char in input_string:
        if char.isalpha():
            num_letters += 1
        elif char.isdigit():
            num_digits += 1

    return num_letters, num_digits

input_string = input("Enter a string: ")
num_letters, num_digits = count_letters_and_digits(input_string)
print("Alphabets:", num_letters, "& Numbers:", num_digits)