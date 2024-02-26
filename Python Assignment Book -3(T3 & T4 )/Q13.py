'''Create a function that takes a list and returns a new list with unique elements of the first list.'''
def unique_elements(input_list):
    unique_list = list(set(input_list))
    return unique_list

my_list = [1, 2, 3, 4, 4, 5, 5, 6, 6]
result_list = unique_elements(my_list)
print("Original list:", my_list)
print("List with unique elements:", result_list)
