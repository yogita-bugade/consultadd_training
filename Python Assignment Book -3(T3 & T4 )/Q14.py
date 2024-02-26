'''Write a program that accepts a hyphen-separated sequence of words as input and prints the words
in a hyphen-separated sequence after sorting them alphabetically.'''


def sort_words(input_str):
    words = input_str.split('-')
    sorted_words = sorted(words)
    sorted_sequence = '-'.join(sorted_words)
    return sorted_sequence

input_sequence = input("Enter a hyphen-separated sequence of words: ")
sorted_sequence = sort_words(input_sequence)
print("Sorted sequence of words:", sorted_sequence)

