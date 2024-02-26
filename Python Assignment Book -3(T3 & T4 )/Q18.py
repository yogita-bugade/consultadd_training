'''Define a function which can generate and print a tuple where the values are square of numbers
between 1 and 20 (both 1 and 20 included).'''
def generate_square_tuple():
    square_tuple = tuple(i**2 for i in range(1, 21))
    return square_tuple

result_tuple = generate_square_tuple()
print("Tuple containing squares of numbers from 1 to 20:", result_tuple)
