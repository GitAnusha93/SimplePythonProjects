
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car is started")
    elif command == "stop":
        print("car stopped")
    elif command == "quit":
        break
    else:
        print("I dont understand")
