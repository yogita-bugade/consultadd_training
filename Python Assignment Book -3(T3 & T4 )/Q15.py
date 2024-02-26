'''Write a program that accepts a sequence of lines as input and prints the lines after making all
characters in the sentence capitalized.
Sample input: Hello world Practice makes man perfect
Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT'''
def capitalize_lines(input_lines):
    for line in input_lines:
        print(line.upper())
input_lines = "Hello world Practice makes man perfect".splitlines()
capitalize_lines(input_lines)
