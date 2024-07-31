import os
import time

BLUE = "\033[0;34m"
RED = "\033[0;31m"
YELLOW = "\033[1;33m"
GREEN = "\033[0;32m"
END = "\033[0m"

os.system('clear') #os.system('cls') #! Use this for Windows OS
print("\nRainbow-Ising\n")
time.sleep(3)
SentenceInput = input("What sentence do you want to RAINBOW-ISING? ")

for TheLetter in SentenceInput:
    if TheLetter.lower() == "r":
        print(RED, end = "")
    elif TheLetter.lower() == "b":
        print(BLUE, end = "")
    elif TheLetter.upper() == "G":
        print(GREEN, end = "")
    elif TheLetter.upper() == "Y":
        print(YELLOW, end = "")
    elif TheLetter == " ":
        print(END, end = "")
    print(TheLetter, end = "")
