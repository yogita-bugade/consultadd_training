'''Create a list of size 5 and execute the slicing structure'''
my_list = [10, 20, 30, 40, 50]

print("Original list:", my_list)

slice1 = my_list[1:3]
print("Slice 1:", slice1)

slice2 = my_list[2:]
print("Slice 2:", slice2)

slice3 = my_list[:3]
print("Slice 3:", slice3)

slice4 = my_list[::2]
print("Slice 4:", slice4)

slice5 = my_list[-3:-1]
print("Slice 5:", slice5)
