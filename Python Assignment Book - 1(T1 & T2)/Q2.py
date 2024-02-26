'''Create a variable of type complex and swap it with another variable of type integer'''
complex_var = 3 + 4j
integer_var = 10
complex_var, integer_var = integer_var, complex_var

print("Swapped values:")
print("Complex variable:", complex_var)
print("Integer variable:", integer_var)
