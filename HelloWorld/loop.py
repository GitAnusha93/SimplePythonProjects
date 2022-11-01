Customer_input = input("Enter phone number")
phone_number = {

    "1" : "One",
    "2" : "two",
    "10" : "ten"
}

output = ""
for ch in Customer_input:
    output += phone_number.get(ch, "!") + " "
print(output)








