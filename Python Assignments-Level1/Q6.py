'''Write a Python program to check if a given number is a perfect
number.
A Perfect number is a positive integer that is equal to the sum of
its proper divisors. For instance, 6 has divisors 1, 2, and 3, and 1 + 2 +
3 = 6, so 6 is a perfect number.
Input: 5
Output: No'''
def is_perfect_number(num):
    if num <= 0:
        return False

    divisor_sum = 0

    for i in range(1, num // 2 + 1):
        if num % i == 0:
            divisor_sum += i

    if divisor_sum == num:
        return True
    else:
        return False

num = int(input("Enter a number: "))
if is_perfect_number(num):
    print("Yes")
else:
    print("No")