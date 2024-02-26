'''Given an array of N integers and an integer K, find the number of
pairs of elements in the array whose sum is equal to K.
Sample Input: arr = [1, 2, 3, 4, 5], k = 6
Sample Output: Pair count: 2'''
def count_pairs_with_sum(arr, k):
    pair_count = 0
    num_count = {}

    for num in arr:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    for num in arr:
        complement = k - num
        if complement in num_count:
            pair_count += num_count[complement]

        if complement == num:
            pair_count -= 1

    pair_count //= 2

    return pair_count

arr = [1, 2, 3, 4, 5]
k = 6

pair_count = count_pairs_with_sum(arr, k)
print("Pair count:", pair_count)