List_Names = []

while True:
    First_Name = input("First Name: ").strip().capitalize()
    Last_Name = input("Last Name: ").strip().capitalize()
    FullName = f"{First_Name} {Last_Name}"
    if FullName in List_Names:
        print(f"ERROR: DUPLICATE!!!{FullName}")
    else:
        List_Names.append(FullName)
        print(FullName)

