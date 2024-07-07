
#* Important Notes

#! This is a For Loop
#for i in "BanaNA":
    #print(i.lower())

YELLOW = '\033[33m'
END = '\033[0m'

myString = "An apple and a banAnA"
for letter in myString:
    if letter.lower() == "a": #! Alternative : if letter.upper() == "A":
    #? Why the all letters not transformed to the lowercase?
    #* Because it's not at the print() and letter.lower() is at the If-Statement
        print(YELLOW, end = '')
    print(letter)
    print(END, end = '')

