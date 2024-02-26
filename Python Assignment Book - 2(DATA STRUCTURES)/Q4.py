'''Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
the number which is divisible by 3 and is a multiple of 2.'''
for number in range(1, 1100):
    if number % 3 == 0 and number % 2 == 0:
        print(number)
