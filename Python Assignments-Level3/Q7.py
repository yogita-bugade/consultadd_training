'''Write a program to construct a dictionary from the two lists
containing the names of students and their corresponding
subjects. The dictionary should map the students with their
respective subjects. Let’s see how to do this using for loops and
dictionary comprehension.
Input: [Sam, Alice, Mona] ,
[Commerce, Science, Computer]
Output: [Sam: Commerce, Alice: Science , Mona: Computer]'''
def construct_dictionary_with_for_loop(names, subjects):
    student_subject_dict = {}
    for i in range(len(names)):
        student_subject_dict[names[i]] = subjects[i]
    return student_subject_dict

names = ['Sam', 'Alice', 'Mona'],['Commerce', 'Science', 'Computer']

result_with_for_loop = construct_dictionary_with_for_loop(names, subjects)
print("Dictionary constructed using for loop:", result_with_for_loop)

def construct_dictionary_with_dict_comprehension(names, subjects):
    return {names[i]: subjects[i] for i in range(len(names))}

result_with_dict_comprehension = construct_dictionary_with_dict_comprehension(names, subjects)
print("Dictionary constructed using dictionary comprehension:", result_with_dict_comprehension)



