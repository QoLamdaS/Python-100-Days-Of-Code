import random
import os
import time

ListOfWords = ["british", "suave", "integrity", "accent", "evil", "gen", "downtown", "downstairs", "streamline", "funnel"]
Already_Picked_Letter = []
def ChosenWord():
    The_Chosen_Word = random.choice(ListOfWords)
    return The_Chosen_Word
Chosen_Answer = ChosenWord()

while True:
    os.system('clear') #os.system('cls') Windows OS #os.system('clear') Linux and Mac OS
    print("\nHangman Game\n")
    time.sleep(3)
    LetterInput = input("Choose a letter: ").lower()
