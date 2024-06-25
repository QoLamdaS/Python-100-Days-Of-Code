import os, time

AllEmailLists = []

def ListsEmail():
    print("\nLists of Email(s)\n")
    counter = 0
    for Email in AllEmailLists:
        counter += 1
        print(f"{counter}: {Email}")

def SPAMMING():
    str(AllEmailLists) #! To avoid Bug
    print("SPAMMING!!!\n")
    counter = 0
    #? Why using If-Statements for this function?
    #* To avoid bug occurred when the total of the email list is less than from the END or range(0, 10)
    if len(AllEmailLists) <= 10: #! len() built-in function start count at 1 (one) not 0 (zero) {The list or x = [] always start at 0 (zero)}
        for index in range(0, len(AllEmailLists)):
            counter += 1
            print(f"Email {counter}\nDear, {AllEmailLists[index]}\n")
            print("It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.\nLove and hugs,\nWalter White VII\n")
            time.sleep(5)
            os.system('cls')
        quit()
    elif len(AllEmailLists) > 10:
        for index in range(0, 10):
            counter += 1
            print(f"Email {counter}\nDear, {AllEmailLists[index]}\n")
            print("It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.\nLove and hugs,\nWalter White VII\n")
            time.sleep(5)
            os.system('cls')
        quit()
    else:
        for _ in range(999): #! Underscore '_' used for ignoring value or throw-away (useless) variable
            print("\nACHTUNG!\n")
        exit()

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
        time.sleep(10)
    elif UserInput == "4":
        os.system('cls')
        SPAMMING()
    else:
        os.system('cls')
        print("\nINVALID INPUT!!!\n")
        quit()
