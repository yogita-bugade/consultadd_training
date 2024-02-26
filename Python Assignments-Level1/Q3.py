'''Write a Python program to input marks for five subjects Physics,
Chemistry, Biology, Mathematics, and Computer. Calculate the
percentage and grade according to the following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F'''
def calculate_grade(marks):
    percentage = (sum(marks) / 500) * 100

    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    elif percentage >= 40:
        grade = 'E'
    else:
        grade = 'F'

    return percentage, grade

marks = []

print("Enter marks for Physics, Chemistry, Biology, Mathematics, and Computer:")
for subject in ['Physics','Chemistry','Biology','Mathematics','Computer']:
    mark = float(input(f"Enter marks for {subject}: "))
    marks.append(mark)

percentage, grade = calculate_grade(marks)
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
