'''In the previous question, insert break after the “Good guess!” print statement. break will terminate
the while loop so that users do not have to continue guessing after they found the number. If the user
does not guess the number at all, print “Sorry but that was not very successful”.'''
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
