'''Write a Python program to reverse the order of words in a given
sentence.
Input_sentence = “Hello, World! Welcome to Python
programming.”
Output after reverse = “programming. Python to Welcome
World! Hello,”'''
def reverse_sentence(input_sentence):
    words = input_sentence.split()
    reversed_words = words[::-1]
    reverse_sentence = ' '.join(reversed_words)
    return reverse_sentence

input_sentence = "Hello, World! Welcome to Python programming."
output_sentence = reverse_sentence(input_sentence)
print("Output after reverse =", f'"{output_sentence}"')
