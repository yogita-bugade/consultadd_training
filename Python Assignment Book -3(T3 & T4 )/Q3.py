'''Write a program to get the sum and multiply of all the items in a given list.'''
def get_sum_and_product(input_list):
    total_sum = 0
    total_product = 1
    for num in input_list:
        total_sum += num
        total_product *= num
    return total_sum, total_product

my_list = [1, 2, 3, 4, 5]
sum_result, product_result = get_sum_and_product(my_list)

print("Sum of all items in the list:", sum_result)
print("Product of all items in the list:", product_result)
