from _ast import While

Secret_number = 1
Guess_count = 0
limit = 3

while Guess_count < limit:
    Guess_count += 1
    Secret = int(input("Enter secret number"))
    if Secret == Secret_number:
        print("You won")
        break
else:
    print("you lost")














