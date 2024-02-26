'''Create a new list which contains the specified numbers after removing the even numbers from a
predefined list.'''
predefined_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [num for num in predefined_list if num % 2 != 0]

print("Original list:", predefined_list)
print("List after removing even numbers:", new_list)
