'''Write a program in Python to iterate through the string “hello my name is abcde” and print the
string which is having an even length.'''
string = "hello my name is abcde"

words = string.split()

for word in words:
    if len(word) % 2 == 0:
        print(word)
