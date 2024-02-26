'''Write a Python program to find the common elements between
two lists.
Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8]
Sample output: [4, 5]'''
def find_common_elements(l1,l2):
    common_elements = []
    for item in l1:
        if item in l2:
            common_elements.append(item)
    return common_elements

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(l1,l2)
print(common_elements)