import os, time

AllList = []

def ToDoLists():
    Number = 0
    for Todo in AllList:
        Number += 1
        print(f"No. {Number}: {Todo}")

while True:
    os.system('cls')
    print("\nExtended TODO List Manager\n")
    UserInput = input("Do you want to 'view', 'add', 'edit', or 'remove' an item from the to do list or Delete all the list 'reset'? ")
    if UserInput == "view" or UserInput == "View" or UserInput == "VIEW":
        ToDoLists()
    elif UserInput == "add" or UserInput == "Add" or UserInput == "ADD":
        Todo = str(input("Add: "))
        if Todo in AllList:
            print(f"'{Todo}' already exists")
        else:
            AllList.append(Todo)
    elif UserInput == "remove" or UserInput == "Remove" or UserInput == "REMOVE":
        Todo = str(input(f"{AllList}\nRemove: "))
        if Todo in AllList:
            UserInput = str(input(f"Are you sure you want to remove '{Todo}' from the list? "))
            if UserInput == "yes" or UserInput == "Yes" or UserInput == "YES" or UserInput == "y" or UserInput == "Y":
                AllList.remove(Todo)
            elif UserInput == "no" or UserInput == "No" or UserInput == "NO" or UserInput == "n" or UserInput == "N":
                print(f"You cancelled to remove '{Todo}' from the list\n")
            else:
                print("Invalid input. Please try again.\n")
                exit()
        else:
            print(f"{Todo} is not in the list.")
    elif UserInput == "edit" or UserInput == "Edit" or UserInput == "EDIT":
        Todo = str(input(f"\n{AllList}\nWhich one do you want to edit: "))
        if Todo in AllList:
            print(Todo)
            AllList.remove(Todo)
            Todo = str(input("Edit: "))
            AllList.append(Todo)
        else:
            print(f"{Todo} is not in the list.")
    elif UserInput == "reset" or UserInput == "Reset" or UserInput == "RESET":
        AllList.clear() #! NEED TO ADD NOTE FOR THIS LINE
        print("\nAll TODO(s) have been deleted from the list.\n")
    else:
        print("Invalid input. Please try again.\n")
        quit()
