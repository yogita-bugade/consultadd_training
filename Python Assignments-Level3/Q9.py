'''Given an input string, write a function that returns the run
length encoded string for the input string.
For Example:
Input: wwwwaaadebbbbbw
Output: w4a3d1e1b5w1'''
def run_length_encoding(input_string):
    encoded_string = ""
    count = 1
    for i in range(len(input_string)):
        if i + 1 < len(input_string) and input_string[i] == input_string[i + 1]:
            count += 1
        else:
            encoded_string += input_string[i] + str(count)
    return encoded_string

input_str = "wwwwaaadebbbbbw"
encoded_str = run_length_encoding(input_str)
print("Output:", encoded_str)
