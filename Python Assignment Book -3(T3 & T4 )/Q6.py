'''Create a list of elements such that it contains the squares of the first and last 5 elements between
1 and30 (both included).'''
squares_list = [(num ** 2) for num in range(1, 31) if num <= 5 or num >= 26]
print("List of squares of the first and last 5 elements between 1 and 30:")
print(squares_list)
