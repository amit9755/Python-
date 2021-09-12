import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="pooja@123", database="student")
mycursr = mydb.cursor()
mycursr.execute("select * from student")
for i in mycursr:
    print(i)