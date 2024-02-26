'''Find the largest and smallest number from a given list.'''
def find_largest_smallest(input_list):
    largest = max(input_list)
    smallest = min(input_list)
    return largest, smallest

my_list = [10, 5, 7, 3, 15, 2, 20]
largest_num, smallest_num = find_largest_smallest(my_list)

print("Largest number in the list:", largest_num)
print("Smallest number in the list:", smallest_num)
