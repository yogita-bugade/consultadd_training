'''Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
Make sure to use only higher order functions.'''
not_divisible_by_3_but_multiple_of_7 = lambda x: x % 3 != 0 and x % 7 == 0
numbers = range(1, 101)
result = filter(not_divisible_by_3_but_multiple_of_7, numbers)
print("Values not divisible by 3 but multiples of 7:", list(result))
