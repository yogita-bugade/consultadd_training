'''Write a program to count the lines in a file “demo.txt”'''
def count_lines(file_path):
    try:
        with open(file_path,'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return -1
    except Exception as e:
        print(f"Error: {e}")
        return -1

file_path = "C:/Users/yogit/Desktop/demo.txt"
lines_count = count_lines(file_path)
if lines_count != -1:
    print(f"The file '{file_path}' contains {lines_count} lines.")