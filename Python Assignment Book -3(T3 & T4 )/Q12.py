'''Write a function that accepts a string and prints the number of uppercase letters and lowercase
letters.
Sample input: “abcSdefPghijQkl”
Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12'''
def count_upper_lower(input_str):
    uppercase_count = 0
    lowercase_count = 0

    for char in input_str:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    print("No. of Uppercase characters:", uppercase_count)
    print("No. of Lowercase characters:", lowercase_count)

input_str = "abcSdefPghijQkl"
count_upper_lower(input_str)
