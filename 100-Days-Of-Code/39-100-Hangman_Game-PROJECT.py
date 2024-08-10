import random
import os
import time

ListOfWords = ["british", "suave", "integrity", "accent", "evil", "gen", "downtown", "downstairs", "streamline", "funnel"]
def ChosenWord():
    The_Chosen_Word = random.choice(ListOfWords)
    return The_Chosen_Word

while True:
    os.system('cls') #os.system('cls') Windows OS #os.system('clear') Linux and Mac OS
    Chosen_Answer = ChosenWord()
    print("\nHangman Game\n")
    time.sleep(3)
    LetterInput = input("Choose a letter: ").lower()

