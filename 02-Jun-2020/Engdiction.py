import json
from difflib import get_close_matches
data = json.load(open("data.json"))
data1 = json.load(open("webster.json"))
print("Welcome to Vishwesh's Kingdom Of Words!!!\nTo exit dictionary enter '-'")
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s? if Yes enter Y,if No enter N" % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            print(data[get_close_matches(w,data.keys())[0]])
        elif yn == "N":
            if w or w.title() in data1[w]:
                if len(get_close_matches(w,data1.keys())) > 0:
                    xn = input("Oh! Did you mean %s?? Y for yes N for no" %get_close_matches(w,data1.keys())[0])
                    if xn == "Y":#Whoa very deep(6th level indentation)
                        print(data1[get_close_matches(w,data1.keys())[0]])
                    elif xn == "N":
                        print("No such words in my dictionary!!")
                    else:
                        print("Sorry...didn't get that, try the word again.")
        else:
            print("There is no such word in english.")
    elif w == "\n":
        print("You didn't enter anything!!")
    else:
        print("OOps! No such words in my dictionary!!")        
while True:
    word = input("Enter word:")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    elif word == "-":
        break
    else:
        print(output)