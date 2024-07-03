import os, time
#! FIRST COMMIT
AllList = []

def ToDoLists():
    Number = 0
    for TheItem in AllList: #* https://www.w3schools.com/python/python_for_loops.asp #Link for understanding the for loops in Python
        Number += 1
        print(f"No. {Number}: {TheItem}")

while True:
    os.system('cls')
    print("\nExtended TODO List Manager\n")
    UserInput = input("Do you want to 'view', 'add', 'edit', or 'remove' an item from the to do list or Delete all the list 'reset'? ")
    #* https://www.programiz.com/sites/tutorial2program/files/python-elif.png #Link for the image of IF-STATEMENT
    if UserInput == "view" or UserInput == "View" or UserInput == "VIEW":
        os.system('cls')
        ToDoLists()
        time.sleep(15)
    elif UserInput == "add" or UserInput == "Add" or UserInput == "ADD":
        Todo = str(input("Add: "))
        if Todo in AllList:
            print(f"\n'{Todo}' already exists\n")
            time.sleep(5)
        else:
            AllList.append(Todo)
    elif UserInput == "remove" or UserInput == "Remove" or UserInput == "REMOVE":
        Todo = str(input(f"{AllList}\nRemove: "))
        if Todo in AllList:
            UserInput = str(input(f"Are you sure you want to remove '{Todo}' from the list? "))
            if UserInput == "yes" or UserInput == "Yes" or UserInput == "YES" or UserInput == "y" or UserInput == "Y":
                AllList.remove(Todo)
            elif UserInput == "no" or UserInput == "No" or UserInput == "NO" or UserInput == "n" or UserInput == "N":
                print(f"\nYou cancelled to remove '{Todo}' from the list\n")
                time.sleep(5)
            else:
                print("\nInvalid input. Please try again.\n")
                exit()
        else:
            print(f"\n'{Todo}' is not in the list.\n")
            time.sleep(5)
    elif UserInput == "edit" or UserInput == "Edit" or UserInput == "EDIT":
        Todo = str(input(f"\n{AllList}\nWhich one do you want to edit: "))
        if Todo in AllList:
            print(f"\n'{Todo}'")
            Todo_Edit = str(input("Edit: "))
            if Todo_Edit in AllList:
                print(f"\n'{Todo_Edit}' is already in the list.\n")
                time.sleep(5)
            else:
                AllList.remove(Todo)
                AllList.append(Todo_Edit)
        else:
            print(f"\n'{Todo}' is not in the list.\n")
            time.sleep(5)
    elif UserInput == "reset" or UserInput == "Reset" or UserInput == "RESET":
        AllList.clear() #! clear() to remove all elements from the list (AllList)
        print("\nAll TODO(s) have been deleted from the list.\n")
        time.sleep(5)
    else:
        print("Invalid input. Please try again.\n")
        quit()
