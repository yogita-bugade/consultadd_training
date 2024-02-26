'''Write a program in Python to multiply the elements of a list by itself using a traditional function
and pass the function to map() to complete the operation'''
def multiply_by_itself(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
result = map(multiply_by_itself, numbers)
print("Original list:", numbers)
print("List after multiplying each element by itself:", list(result))
