import os, time

os.system('cls')
NameInput = str(input("Enter name: "))
UrlInput = str(input("Enter URL: "))
DescInput = str(input("Enter description: "))
RatingInput = str(input("Enter rating: "))

time.sleep(5)
os.system('cls')

TheDictionary = {"Name": NameInput, "URL": UrlInput, "Description": DescInput, "Rating": RatingInput}

for Key, Value in TheDictionary.items():
    print(f"{Key}: {Value}")