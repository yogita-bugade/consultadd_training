'''Write a Python program to check if a string is an anagram of
another string.
string1 = "listen", string2 = "silent"
Output: True'''
def check_anagram(s1,s2):
    s1 = s1.lower().replace(" ","")
    s2 = s2.lower().replace(" ","")

    if len(s1) != len(s2):
        return False

    count1 = {}
    count2 = {}

    for char in s1:
        count1[char] = count1.get(char,0) + 1

    for char in s2:
        count2[char] = count2.get(char,0) + 1

    return count1 == count2

string1 = input("Enter string one: ")
string2 = input("Enter string two: ")
if check_anagram(string1,string2):
    print("True")
else:
    print("False")
