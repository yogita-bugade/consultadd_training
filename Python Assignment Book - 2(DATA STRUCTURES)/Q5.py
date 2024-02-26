'''Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
string with their index.'''
def reverse_string_with_vowels(string):
    vowels = "aeiouAEIOU"
    reversed_string = string[::-1]

    for index, char in enumerate(reversed_string):
        if char in vowels:
            print("Vowel:", char, "Index:", index)

input_string = input("Enter a string: ")
reverse_string_with_vowels(input_string)
