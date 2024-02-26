'''Define a function that can accept two strings as input and print the string with the maximum length
in the console. If two strings have the same length, then the function should print both the strings line
by line.'''
def print_longest_string(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    if len_str1 > len_str2:
        print(str1)
    elif len_str2 > len_str1:
        print(str2)
    else:
        print(str1)
        print(str2)

input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")
print_longest_string(input_str1, input_str2)
