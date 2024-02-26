'''Write a Python program to calculate the LCM (Least Common
Multiple) of two numbers.
number1 = 12, number2 = 18
LCM of 12 and 18 are: 36
'''
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a,b)


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

lcm_result = lcm(number1,number2)
print(f"LCM of {number1} and {number2} is: {lcm_result}")