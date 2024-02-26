'''Write a program to replace the last element in a list with another list.
Sample input: [1,3,5,7,9,10], [2,4,6,8]
Expected output: [1,3,5,7,9,2,4,6,8]'''
def replace_last_element(main_list, new_list):
    main_list[-1:] = new_list

input_list = [1, 3, 5, 7, 9, 10]
new_list = [2, 4, 6, 8]
replace_last_element(input_list, new_list)

print("Updated list:", input_list)
