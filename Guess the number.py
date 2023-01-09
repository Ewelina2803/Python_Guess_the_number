# A small game to guess the number invented by the computer. Try your luck! 

import random
my_number = random.randint(0,100)

guess=-1
print("Enter a number between 0 and 100")

while guess != my_number:
    guess=int(input())

    if guess == my_number:
        print("Congratulations! That's the right number :)")
    elif guess > my_number:
        print("Unfortunately, your number is too high :( Try again!")
    else:
        print("Unfortunately, your number is too small :( Try again!"),
