'''
#Show Databases/ create databases
import mysql.connector

mydb = mysql.connector.connect(
    host ="localhost",
    user="root",
    passwd="")
print(mydb)
    
#mycursor = mydb.cursor()
#mycursor.execute("SHOW DATABASES")

#for x in mycursor:
   # print(x)
'''  

'''
=====================================================================
import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",passwd="",database="rohit123")
cursor = db.cursor()

#mycursor.execute("ALTER TABLE table2 ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY)")

============================================================================
'''

#Show/CREATE/UPDATE Tables
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="rohit123")

mycursor = mydb.cursor()
#mycursor.execute("ALTER TABLE table3 ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#mycursor.execute("CREATE TABLE table3 (name VARCHAR(25) NOT NULL, AGE int, COMPANY VARCHAR(225))")
mycursor.execute("UPDATE table2 set name = 'rajeev' where name = 'raj'")

mydb.commit()

print(mycursor.rowcount, "records effect")

'''
#INSERT DATA in TABLES
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",passwd="",database="rohit123")
mycursor = mydb.cursor()
sql = "INSERT INTO table3 (name, age) values(%s, %s)"
val = [("rohit",'27'),
       ("rohit",'24'),
       ("ranjan", '23')
       ]
mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted.")

print(mycursor.lastrowid)
============================================================================
'''
'''
#SELECT FROM TABLE/COLUMN- fechall/fetchone
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",passwd="",database="rohit123")
mycursor = mydb.cursor()
mycursor.execute("SELECT NAME, ID, AGE FROM table3")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
=============================================================================
'''

'''
#WHERE CLAUSE/

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",passwd="",database="rohit123")
mycursor = mydb.cursor()
sql = ("SELECT * FROM table3 where name='rohit'")
mycursor.execute(sql)
myresult = mycursor.fetchone()

for x in myresult:
    print(x)

=====================================================================
'''
'''
#DELETE COLUMN/TABLE OR DELETE placeholder %s method:
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",passwd="",database="rohit123")
mycursor = mydb.cursor()
sql = ("DELETE FROM table3 where age='25'")
#sql = ("DELETE FROM table3 where name='%s'")
#name =("rohit")
mycursor.execute(sql)
mydb.commit()
#print(mycursor.rowcount, "records delete")

mycursor.execute("SELECT age FROM table3")
myresult = mycursor
for x in myresult:
    print(x)
====================================================================
'''

