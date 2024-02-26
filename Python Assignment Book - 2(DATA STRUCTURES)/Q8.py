'''Write a program in Python to complete the following task:
Create two lists such as even_list and odd_list
Ask user to enter a number in the range of 1,50 and make sure if the entered number is
even, append it to the even_list and if the entered number is odd append it to the odd_list.
Keep that in mind you can only add 5 items in each list
Make sure once you enter all the 5 elements, calculate the sum of the list and return the
maximum of the list.'''
even_list = []
odd_list = []

for _ in range(5):
    number = int(input("Enter a number between 1 and 50: "))

    if number % 2 == 0:
        if len(even_list) < 5:
            even_list.append(number)
        else:
            print("Even list is full!")
    else:
        if len(odd_list) < 5:
            odd_list.append(number)
        else:
            print("Odd list is full!")

even_sum = sum(even_list)
odd_sum = sum(odd_list)
even_max = max(even_list, default=0)
odd_max = max(odd_list, default=0)

print("Even list:", even_list)
print("Even sum:", even_sum)
print("Maximum of even list:", even_max)
print()
print("Odd list:", odd_list)
print("Odd sum:", odd_sum)
print("Maximum of odd list:", odd_max)
