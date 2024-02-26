'''Write a Python function that counts the number of vowels in a
given string.
Sample Input: string = "Hello, World!"
Sample Output: Number of vowels: 3'''
def count_vowels(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

string = "Hello,World!"
num_vowels = count_vowels(string)
print("Number of vowels:",num_vowels)