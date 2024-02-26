'''Write a program which uses filter() to make a list whose elements are even numbers between 1
and 20 (both included)'''
even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 21)))
print("Even numbers between 1 and 20:", even_numbers)
