List_Names = []

while True:
    First_Name = input("First Name: ").strip().capitalize()
    Last_Name = input("Last Name: ").strip().capitalize()
    FullName = f"{First_Name} {Last_Name}"
    if FullName in List_Names:
        print(f"\nERROR: DUPLICATE!!!\n{FullName}\n")
    else:
        List_Names.append(FullName)
        print(f"\n{FullName}\n")

