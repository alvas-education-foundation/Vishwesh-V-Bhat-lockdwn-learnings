import hashlib

flag = 0

pass_hash = input("enter md5 hash: ".upper())
wordlist = input("file name: ".upper())
try :
    pass_file = open(wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    print(word)
    print(digest)
    print(pass_hash)

    if digest == pass_hash:
        print("Password found!!")
        print("password is " + word)
        break

if flag == 0:
    print("password is not in the list!!")