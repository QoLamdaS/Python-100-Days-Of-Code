
#* Important Notes

#! This is a For Loop
#for i in "BanaNA":
    #print(i.lower())

YELLOW = '\033[33m'
END = '\033[0m'

myString = "An apple and a banAnA"
for letter in myString:
    if letter.lower() == "a": #! Alternative : if letter.upper() == "A":
    #? Why the all letters not transformed to the lowerNase?
    #* Because it's not at the print() and letter.lower() is at the If-Statement
        print(YELLOW, end = "")
    print(letter, end = "") #* end = "" >>> LINK : https://www.toppr.com/guides/python-guide/questions/what-does-end-do-in-python/#:~:text=The%20end%20parameter%20in%20the,whitespace%20and%20not%20a%20newline.
    print(END, end = "")

#! This is End parameter for print
print("\n\nThis is the first line", end = "")
print("SECOND LINE")