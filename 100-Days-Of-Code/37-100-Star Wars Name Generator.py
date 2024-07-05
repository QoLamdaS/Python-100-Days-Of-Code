print("\nSTARS WARS NAME GENERATOR\n")

FirstName = input("First Name: ").strip().capitalize()
LastName = input("Last Name: ").strip().lower()
Mom_Maiden = input("Mom's Maiden Name: ").strip().capitalize()
TheCity = input("City Name: ").strip().lower()

print(f"\nYour Star Wars name is {FirstName[:3:]}{LastName[:3:]} {Mom_Maiden[:2:]}{TheCity[4::]}\n")
