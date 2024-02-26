'''Read the doc.txt file using Python File handling concept and
return only the even length string from the file. Consider the
content of doc.txt as given below:
Hello I am a file
Where you need to return the data string which is of even length.
Make sure you return the content in The same link as it is present.'''
def get_even_length_strings(file_path):
    even_length_strings = []

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) % 2 == 0:
                    even_length_strings.append(word)
    return even_length_strings

file_path = "C:/Users/yogit/Desktop/doc.txt"
even_length_strings = get_even_length_strings(file_path)
print("Even length strings from the file:")
print(even_length_strings)