'''Write a Python program to find the sum of all odd numbers
between two given numbers.
Start = 1, stop = 10
Sum of odd numbers: 25'''
def sum_odd_numbers(start,stop):
    total = 0
    for i in range(start,stop):
        if i % 2 != 0:
            total += i
    return total


start = int(input("Start: "))
stop = int(input("Stop: "))
odd_numbers_list = sum_odd_numbers(start,stop)
print(f"Sum of odd numbers: {odd_numbers_list}")
