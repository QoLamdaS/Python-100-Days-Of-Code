import os

os.system('clear') #os.system('cls') for Windows #os.system('clear') for Linux and Mac
print("\nContact Card\n")
InputName = str(input("Name > "))
InputD_O_B = str(input("Date of Birth > "))
InputTelephone_Number = str(input("Telephone Number > "))
InputEmail = str(input("Email > "))
InputAddress = str(input("Address > "))

The_Dictionaries = {'NAME':InputName, 'DOB':InputD_O_B, 'TEL':InputTelephone_Number, 'EMAIL':InputEmail, 'ADDRESS':InputAddress}

os.system('clear') #os.system('cls') for Windows #os.system('clear') for Linux and MacOS
print(f"\nHere's your contact card\n\nName: {The_Dictionaries['NAME']}\nDate of Birth: {The_Dictionaries['DOB']}\nTelephone Number: {The_Dictionaries['TEL']}\nEmail: {The_Dictionaries['EMAIL']}\nAddress: {The_Dictionaries['ADDRESS']}")