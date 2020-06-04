import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)
cursor = con.cursor()
while True:
    word = input("Enter word:")

    query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'"%word)
    results = cursor.fetchall()
    if word == '-':
        break
    if results:
        for result in results:
            print(result[0])   
    elif len(get_close_matches(word,results)) > 0:
        print("Did you mean %s"%get_close_matches(word,results)[0])
    else:
        print("No such words in the dictionary.") 
