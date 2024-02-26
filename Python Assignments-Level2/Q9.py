'''Write a Python program that executes an operation on a list and
handles an IndexError exception if the index is out of range.'''
def perform_operation_on_list(input_list,index):
    try:
        result = input_list[index]
        print("Result of operation:",result)
    except IndexError:
        print("Index is out of range.Please provide a valid index.")

my_list = [1, 2, 3, 4, 5]
perform_operation_on_list(my_list, 2)
perform_operation_on_list(my_list, 10)