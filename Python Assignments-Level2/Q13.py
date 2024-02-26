'''Write a Python program to find if a given string starts with a
given character using Lambda.
Sample input: input_string = "Hello, World!", given_char = "H"
Sample Output: True'''
check_startswith = lambda input_string, given_char: input_string.startswith(given_char)
input_string = "Hello, World!"
given_char = "H"

result = check_startswith(input_string,given_char)
print(result)