marks = {"Aalu Bhujia":13,"Pakoda":17,"Zoozoo":20,"Vishwesh":30}
print("Total number of students took up test = ",len(marks))

for key,value in marks.items():
    print("{} has scored {}".format(key, value))
    if value >= 15:
        print("- Pass ".upper())
    else:
        print("- Failed ")
    
    pass_marks = [value >=15 for value in marks.values()]

