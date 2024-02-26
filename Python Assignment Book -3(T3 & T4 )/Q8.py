'''Create a new dictionary by concatenating the following two dictionaries:
Sample input: a={1:10,2:20} b={3:30,4:40}
Expected output: {1:10,2:20,3:30,4:40}'''
def concatenate_dicts(dict1, dict2):
    new_dict = dict1.copy()
    new_dict.update(dict2)
    return new_dict

a = {1: 10, 2: 20}
b = {3: 30, 4: 40}

result_dict = concatenate_dicts(a, b)
print("Concatenated dictionary:", result_dict)
