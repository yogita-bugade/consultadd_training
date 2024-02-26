'''Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().'''
from functools import reduce

concatenate = lambda x, y: x + y
flattened_string = reduce(concatenate, map(str, [1, 2, 3, 4, 5, 6, 7]))
print("Flattened string:", flattened_string)
