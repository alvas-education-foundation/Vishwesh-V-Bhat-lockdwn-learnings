import mysql.connector #Imported connector(serves as connector B/W python code and server)

con = mysql.connector.connect(   #To establish connection
user = "ardit700_student",       #passing database credentials as parameter
password = "ardit700_student",   
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()     #To navigate through the tables of database

word=input("Enter the word: ") #User will i/p word

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
#(above)we create a query to select the meaning for word entered from the tables of database
#In the database table we have rows of words with associated meanings in a parallel row
#Our search is by column, each column in the row is checked for the entered word
#By "Expression =" we are giving the the column expression that has to be searched in the database
results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")
