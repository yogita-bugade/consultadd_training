'''Write a program to reverse a string.
Sample input: “1234abcd”
Expected output: “dcba4321”'''
def reverse_string(input_str):
    reversed_str = input_str[::-1]
    return reversed_str

input_str = "1234abcd"
reversed_str = reverse_string(input_str)
print("Reversed string:", reversed_str)
