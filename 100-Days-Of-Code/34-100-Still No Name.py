import os, time

AllEmailLists = []

def ListsEmail():
    print("\nLists of Email(s)\n")
    counter = 0
    for Email in AllEmailLists:
        counter += 1
        print(f"{counter}: {Email}")

os.system('cls')
while True:
    print("\nSPAMMER Inc.\n")
    UserInput = input("1. Add Email\n2. Remove Email\n3. Show Email(s)\n4. Get SPAMMING\n\nUser Input: ")
    if UserInput == "1":
        Email = input("New Email: ")
        AllEmailLists.append(Email)
    elif UserInput == "2":
        Email = input("Remove Email: ")
        if Email in AllEmailLists:
            AllEmailLists.remove(Email)
        else:
            print(f"{Email} isn't in the list.")
    elif UserInput == "3":
        os.system('cls')
        print("\nHere is the list of all emails: ")
        ListsEmail()
        time.sleep(15)
    elif UserInput == "4":
        print("UNFINISHED")
        #! Unfinished, still working for this
    else:
        os.system('cls')
        print("\nINVALID INPUT!!!\n")
        quit()
