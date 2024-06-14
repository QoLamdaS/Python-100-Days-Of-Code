AllLists = []

def ToDoLists():
    print("\nTo Do List(s):")
    for item in AllLists:
        print(item)
    print()

while True:
    UserLists = input("Choose one: 'add', 'remove', 'edit', 'view', or 'exit'? ")
    if UserLists == "view":
        print(f"Here is your All To Do List(s): {AllLists}")
    elif UserLists == "add":
        item = input("Add: ")
        AllLists.append(item) 
    elif UserLists == "remove":
        item = input("Remove: ")
        if item in AllLists:
            AllLists.remove(item)
        else:
            print(f"{item} is not in the list.")
    elif UserLists == "edit":
        item = input(f"\n{AllLists}\nWhich one do you want to edit: ")
        if item in AllLists:
            AllLists.remove(item)
            item = input("Edit: ")
            AllLists.append(item)
        else:
            print(f"{item} is not in the list.")
    elif UserLists == "exit":
        print("\nThanks for using this program.\nPlease give me some feedbacks to improve my programming skill.\n")
        quit()
    else:
        print("\nINVALID INPUT, Try again!\n")
        exit()
    
    ToDoLists()
