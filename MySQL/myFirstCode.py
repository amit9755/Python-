import mysql.connector
Mydb = mysql.connector.connect(host="localhost", user="Amit", password="pooja@123", database="Pooja")

mycursor = Mydb.cursor()

mycursor.execute("select * from Pooja")
for i in mycursor:
    print(i)