'''Read the two parts of the question below:Write a program such that it asks users to “guess the lucky number”. If the correct number is
guessed the program stops, otherwise it continues forever.
Modify the program so that it asks users whether they want to guess again each time. Use two
variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
The program continues as long as a user has not answered “no” and has not guessed the correct
number)'''
import random

lucky_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the lucky number (between 1 and 100): "))

    if guess == lucky_number:
        print("Congratulations! You guessed the lucky number!")
        break

    answer = input("Wrong guess. Do you want to guess again? (yes/no): ")
    if answer.lower() != "yes":
        break
