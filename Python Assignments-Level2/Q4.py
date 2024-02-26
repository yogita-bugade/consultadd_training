'''Given an array of size N. The task is to rotate array by D elements
towards right
Sample Input: arr = [1, 2, 3, 4, 5], D = 2
Sample Output: arr after rotation = [4, 5, 1, 2, 3]'''
def reverse_array(arr,start,end):
    while start < end:
        arr[start],arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(arr,d):
    n = len(arr)
    d = d % n
    reverse_array(arr,0,n-1)
    reverse_array(arr,0,d-1)
    reverse_array(arr,d,n-1)

arr = [1, 2, 3, 4, 5]
D = 2
rotate_array(arr,D)
print("arr after rotation =",arr)