'''Write a program which uses map() and filter() to make a list whose elements are squares of even
numbers in [1,2,3,4,5,6,7,8,9,10].
Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
numbers in the filtered list. Use lambda() to define anonymous functions.'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
squares_of_even_numbers = map(lambda x: x ** 2, even_numbers)
squares_of_even_numbers = list(squares_of_even_numbers)
print("Squares of even numbers:", squares_of_even_numbers)
