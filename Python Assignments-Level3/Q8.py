'''You need to write a function that accepts an encoded string as a
parameter.
This string will contain a first name, last name, and an id.
Values in the string can be separated by any number of zeros. The
id is a numeric value but will contain no zeros. The function should
parse the string and return a Python dictionary that contains the
first name, last name, and id values.
For example:
Input : “Robert000Smith000123”
Output:
{ “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }'''


def parse_encoded_string(encoded_string):
    parts = encoded_string.split('0')
    parts = [part for part in parts if part]

    first_name = parts[0]
    last_name = parts[1]
    id_ = parts[2]

    result = {
        "first_name": first_name,
        "last_name": last_name,
        "id": id_
    }
    return result

encoded_string = "Robert000Smith000123"
parsed_dict = parse_encoded_string(encoded_string)
print(parsed_dict)
