'''Define a function that can receive two integral numbers in string form and compute their sum and
print it in the console.'''
def compute_and_print_sum(num1_str, num2_str):
    num1 = int(num1_str)
    num2 = int(num2_str)
    sum_result = num1 + num2
    print("Sum:", sum_result)

num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")
compute_and_print_sum(num1_str, num2_str)
