'''Write a Python program to count the frequency of each element
in a list.
Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}'''
def count_frequency(input_list):
    frequency = {}
    for element in input_list:
        frequency[element] = frequency.get(element,0) + 1
    return frequency

input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
frequency_count = count_frequency(input_list)
print("Frequency count:", frequency_count)
