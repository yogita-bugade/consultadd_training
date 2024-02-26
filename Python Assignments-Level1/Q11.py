'''Write a Python program to calculate the sum of digits of a given
number until the sum becomes a single-digit number.
Sample Input: num = 987
Sample Output: Sum_of_digits = 24,
Again compute the sum of digits so that it can be reduced to
on single digit.
Final Output: 6'''
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

def reduce_to_single_digit(num):
    while num >= 10:
        num = sum_of_digits(num)
    return num


num = 987
sum_result = sum_of_digits(num)
print("Sum_of_digits:", sum_result)

final_sum_result = reduce_to_single_digit(sum_result)
print("Final output:", final_sum_result)