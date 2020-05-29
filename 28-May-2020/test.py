def sent(phr):
    intrr = ("what","when","why","where","how")
    capitalized = phr.capitalize()
    if phr.startswith(intrr):
        return "{}?".format(capitalized) 
    else:
        return "{}.".format(capitalized)

res = []
while True:
    x = input("Say something: ")
    if x == "done":
        break
    else:
        res.append(sent(x))

print(" ".join(res))
  