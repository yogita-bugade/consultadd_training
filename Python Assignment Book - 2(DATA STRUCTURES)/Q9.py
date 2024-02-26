'''Write a program to find out the occurrence of a specific character from an alphanumeric string.
Sample input: 12abcbacbaba344ab
Expected output: a=5 b=5 c=2
NOTE: Make sure to avoid counting the occurrence of numeric values in the string.'''
input_string = "12abcbacbaba344ab"
character_count = {}

for char in input_string:
    if char.isalpha():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

for char, count in character_count.items():
    print(f"{char}={count}", end=" ")
