
started = False
while True:
    command = input("<")
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print(" Car started")
    elif command == "stop":
        if not started:
            print("Its already stopped")
        else:
            started = False
            print("car stopped")

    elif command == "help":
         print("""
        start - to start the game
        stop - to stop the game
        quit - to exit the game
         """)
    elif command == "quit":
        break
    else:
        print("I dont understand")
