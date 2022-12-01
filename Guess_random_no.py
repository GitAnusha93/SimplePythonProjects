import random


number = random.randint(0,10)

while True:
    guess = int(input("Enter the guessing number"))
    if guess == number:
        print("Congo, guessed right")
        break
    if guess > number:
        print("You are far")
    else:
        print("You are near")
    





