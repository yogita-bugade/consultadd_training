'''Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
such as
counter = 1
while counter <= 5:
print(“Type in the”, counter, “number”
counter=counter+1
The program asks for five guesses (no matter whether the correct number was guessed or not). If the
correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
After the fifth guess it stops and prints “Game over!”.'''
import random

lucky_number = random.randint(1, 100)
counter = 1

while counter <= 5:
    guess = int(input("Type in the {} number: ".format(counter)))

    if guess == lucky_number:
        print("Good guess!")
        break
    else:
        print("Try again!")

    counter += 1

    if counter == 6:
        print("Game over!")
