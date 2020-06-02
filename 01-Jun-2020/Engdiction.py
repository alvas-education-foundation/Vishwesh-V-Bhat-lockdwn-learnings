import json
from difflib import get_close_matches

data = json.load(open("data.json"))
print("Welcome to Vishwesh's Kingdom Of Words!!!\nTo exit dictionary enter '-'")

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 5:
        yn = input("Did you mean %s? if Yes enter Y,if No enter N" % get_close_matches(w,data.keys())[5])
        if yn == "Y":
            print(data[get_close_matches(w,data.keys())[0]],)
            
        elif yn == "N":
            print("Hmmm.... not sure about that.")
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