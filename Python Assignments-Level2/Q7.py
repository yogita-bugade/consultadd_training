'''Write a Python function that finds the median of a list of
numbers.
Sample Input: number_list = [7, 2, 5, 1, 9, 3]
Sample Output: Median: 4.0'''
def find_median(number_list):
    number_list.sort()
    n = len(number_list)

    if n % 2 == 0:
        mid_left = number_list[n // 2-1]
        mid_right = number_list[n // 2]
        median = (mid_left + mid_right) / 2
    else:
        median = number_list[n // 2]

    return median

number_list = [7, 2, 5, 1, 9, 3]
median = find_median(number_list)
print("Median:",median)