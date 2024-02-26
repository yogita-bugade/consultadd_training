'''Write a program which accepts a sequence of comma-separated numbers from console and
generates a list and a tuple which contains every number in the form of string.
Sample input: 34,67,55,33,12,98
Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)'''

def generate_list_and_tuple(input_str):
    numbers_as_strings = input_str.split(',')
    numbers_as_tuple = tuple(numbers_as_strings)

    return numbers_as_strings, numbers_as_tuple

input_sequence = "34,67,55,33,12,98"
output_list, output_tuple = generate_list_and_tuple(input_sequence)

print("List:", output_list)
print("Tuple:", output_tuple)
