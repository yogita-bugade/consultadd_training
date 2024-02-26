'''Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
and n(both 1 and n included).
Sample input: n=5
Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}'''
def create_dict(n):
    result_dict = {x: x*x for x in range(1, n+1)}
    return result_dict

n = 5
output_dict = create_dict(n)
print("Output dictionary:", output_dict)
