'''Write a program in python to print the pair of numbers whose sum is equal to the result
number that is let's say 8.
x=[1,2,3,4,5,6,7,8,9,-1]'''

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
result_number = 8
pairs = []

for i in range(len(x)):
    for j in range(i + 1, len(x)):
        if x[i] + x[j] == result_number:
            pairs.append((x[i], x[j]))

print("Pairs whose sum is equal to", result_number, ":")
for pair in pairs:
    print(pair)
