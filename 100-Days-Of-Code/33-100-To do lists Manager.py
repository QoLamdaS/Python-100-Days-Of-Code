AllLists = [] #! Variable need to declare first as a List (empty)

def ToDoLists():
    print("\nTo Do List(s):")
    for item in AllLists: #* This is For Loop, where the output will be iterated each iteration or (e.g. Loop #1, Loop #2, Loop #3, until the for loop reach the limit or end)
        print("XAVFX#1") #*Example
        print(item)
        print("QASWKL#2") #*Example
    print()

while True:
    UserLists = input("Choose one: 'add', 'remove', 'edit', 'view', or 'exit'? ")
    if UserLists == "view":
        print(f"Here is your TO DO LISTS:{AllLists}")
        #! WRONG: print(f"Here is your TO DO LISTS:{ToDoLists()}")
        #! Because there is NO variable to stored value at that Function
    elif UserLists == "add":
        item = input("Add: ")
        AllLists.append(item) 
        #! Naming between List variable name and function name MUST be different
        #? Why is it needed? Ich weiß nicht. =)
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
