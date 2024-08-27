# GOOD TO BE A STANDALONE PROJECT
# Refrensinya ada di Day 27-100-Random Generator-PROJECT part 1
# Codenya spagethi, kurang rapi
# Strenght tidak saya hitung, keterangan challengenya gak jelas menurutku

import random, os, time

# Lists Random Name for Function 1a and 1b
first_names =  ['John', 'Andy', 'Joe', 'Hitler', 'Warning']
middle_names = ['Kontol', 'Saklo', 'Wealtod', 'Herman', 'Nigga']
last_names = ['Qwasd', 'Madison', 'Kim', 'Sung', 'Huang']

# Function 1a
def generate_random_nameP1():
    FirstName = random.choice(first_names)
    MiddleName = random.choice(middle_names)
    LastName = random.choice(last_names)
    return f"{FirstName} DARLING {MiddleName} aYaNg {LastName}"
LegendNameP1 = generate_random_nameP1()

# Function 1b
def GenerateRandomNameP2():
    FirstName = random.choice(first_names)
    MiddleName = random.choice(middle_names)
    LastName = random.choice(last_names)
    return f"{FirstName} {MiddleName} {LastName}"
LegendNameP2 = GenerateRandomNameP2()

# Function 2a
def GenerateCharacterTypeP1():
    CharacterType = random.choice(['Human', 'Elf', 'Wizard', 'Orc'])
    return CharacterType

# Function 2b
def GenerateCharacterTypeP2():
    CharacterType = random.choice(['Human', 'Elf', 'Wizard', 'Orc'])
    return CharacterType

# Function 3a
def GenerateHealthP1():
    SixSided = random.randint(1, 6)
    TwelveSided = random.randint(1, 12)
    Health = (SixSided * TwelveSided) / 2 + 10
    return Health
HealthP1 = GenerateHealthP1()

# Function 3b
def GenerateHealthP2():
    SixSided = random.randint(1, 6)
    TwelveSided = random.randint(1, 12)
    Health = (SixSided * TwelveSided) / 2 + 10
    return Health
HealthP2 = GenerateHealthP2()

# Function 4a
def GenerateStrengthP1():
    SixSided = random.randint(1, 6)
    TwelveSided = random.randint(1, 12)
    Strength = (SixSided * TwelveSided) / 2 + 12
    return Strength

# Function 4b
def GenerateStrengthP2():
    SixSided = random.randint(1, 6)
    TwelveSided = random.randint(1, 12)
    Strength = (SixSided * TwelveSided) / 2 + 12
    return Strength

#* INTERMISION
print("Character P1\n")
time.sleep(2.5)
print(f"Legend Name P1: {LegendNameP1}\n")
print(f"Character Type P1: {GenerateCharacterTypeP1()}\n")
print(f"HEALTH P1: {HealthP1}\n")
print(f"STRENGTH P1: {GenerateStrengthP1()}\n")
time.sleep(1.5)
print("Character P2\n")
time.sleep(2.5)
print(f"Legend Name P2: {LegendNameP2}\n")
print(f"Character Type P2: {GenerateCharacterTypeP2()}\n")
print(f"HEALTH P2: {HealthP2}\n")
print(f"STRENGTH P2: {GenerateStrengthP2()}\n")
time.sleep(3)

# The Battle Starts
os.system("clear")
print("The Battle Begins!\n")
round = 0
while True:
    def AttackDamage():
        Damage = random.randint(1, 10)
        return Damage
    TheDamage = AttackDamage()
    def PersonAttackFirst():
        Person = random.choice([LegendNameP1, LegendNameP2])
        #! Person = random.choice([generate_random_nameP1(), GenerateRandomNameP2()]) #Tidak bisa soalnya namanya belum di assign di variable nya (variable sudah absolut nilainya dan tidak bisa diubah lagi oleh Random Generator)
        # Jadi kayak komputernya generate nama lagi dari nol, meskipun komputer sudah generate nama sebelumnya
        # Yang health juga mirip seperti tadi
        # Jadi mungkin lebih baik valuenya yang sudah di generate di assign di variable nya
        # Menurut saya, jika itu kayak GenerateHealthP1() berulang kali maka komputernya akan generate yang berbeda lagi di dalam satu RUN atau saat RUN.
        return Person
    WhoAttack = PersonAttackFirst()
    round += 1
    print(f"Round {round}")
    time.sleep(3)
    
    if WhoAttack == LegendNameP1:
        HealthP2 -= TheDamage
        print(f"{LegendNameP1} attacks with {TheDamage} Damage\n")
        print(LegendNameP1)
        print(f"HEALTH P1: {HealthP1}\n")
        print(LegendNameP2)
        print(f"HEALTH P2: {HealthP2}\n")
        time.sleep(3)
        if HealthP2 <= 0:
            print(f"{LegendNameP1} WINS!\n")
            break
        elif HealthP2 > 0:
            print(f"{LegendNameP1} and {LegendNameP2} are still fighting!\n")
            time.sleep(3)
            continue
        else:
            print("Achtung!!!")
            quit()
    
    elif WhoAttack == LegendNameP2:
        HealthP1 -= TheDamage
        print(f"{LegendNameP2} attacking with {TheDamage} Damage\n")
        print(LegendNameP1)
        print(f"HEALTH P1: {HealthP1}\n")
        print(LegendNameP2)
        print(f"HEALTH P2: {HealthP2}\n")
        if HealthP1 <= 0:
            print(f"{LegendNameP2} WINS!\n")
            break
        elif HealthP2 > 0:
            print(f"{LegendNameP1} and {LegendNameP2} are still fighting!\n")
            continue
        else:
            print("Achtung!!!")
            quit()
    
    else:
        print("WARNING!!!")
        quit()

print("The Battles Ends!\n")
print("Vielen Dank\n")
exit()