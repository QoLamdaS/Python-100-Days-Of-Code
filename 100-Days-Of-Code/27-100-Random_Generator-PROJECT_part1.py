import random, os, time

#* Lists Random Name for Function 1
# Yang dibawah ini gak perlu di dalam while True Loop soalnya valuenya yang ada di variable tersebut tetap sama kalau di ulang lagi Loopnya
# Jadi variable nya di declare dulu biar efisien (Gak di declare ngulang-ulang)
first_names =  ['John', 'Andy', 'Joe', 'Hitler', 'Warning']
middle_names = ['Kontol', 'Saklo', 'Wealtod', 'Herman', 'Nigga']
last_names = ['Qwasd', 'Madison', 'Kim', 'Sung', 'Huang']

# while True harus paling atas soalnya biar Function yang ada di dalam Loop ngulang lagi
while True:
    # Function 1
    def generate_random_name():
        FirstName = random.choice(first_names)
        MiddleName = random.choice(middle_names)
        LastName = random.choice(last_names)
        return f"{FirstName} DARLING {MiddleName} aYaNg {LastName}"
    LegendName = generate_random_name()

    # Function 2
    def GenerateCharacterType():
        CharacterType = random.choice(['Human', 'Elf', 'Wizard', 'Orc'])
        return CharacterType

    # Function 3
    def GenerateHealth():
        SixSided = random.randint(1, 6)
        TwelveSided = random.randint(1, 12)
        Health = (SixSided * TwelveSided) / 2 + 10
        return Health

    # Function 4
    def GenerateStrength():
        SixSided = random.randint(1, 6)
        TwelveSided = random.randint(1, 12)
        Strength = (SixSided * TwelveSided) / 2 + 12
        return Strength

#* The Print (For Output)
    print("Character Builder\n")
    time.sleep(2.5)
    print(f"Your Legend Name: {LegendName}\n")
    #! print(f"Your Legend Name: {generate_random_name()}")
    print(f"Character Type: {GenerateCharacterType()}\n")
    print(f"HEALTH: {GenerateHealth()}\n")
    
    # Experimenting
    print(GenerateHealth())
    print(GenerateHealth())
    print(GenerateHealth())
    
    print(f"STRENGTH: {GenerateStrength()}\n")
    print("May your name go down in Legend...\n")
    time.sleep(3)
    UserStatement = input("Again? (yes/no): ")
    if UserStatement == "yes" or UserStatement == "y":
        os.system("clear")
        continue
    elif UserStatement == "no" or UserStatement == "n":
        print("\nThank you for using the Character Builder!")
        time.sleep(5)
        os.system("clear")
        quit()
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        time.sleep(5)
        os.system("clear")
        exit()

