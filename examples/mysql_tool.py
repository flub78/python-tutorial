"""
This script is a tool to check a MySQL database context. It performs the following tasks:

1. Checks if the connection to the database is possible.
2. Checks if the "BOOKS" table exists in the database.
3. Creates the "BOOKS" table if it doesn't exist.
4. Inserts some sample data into the "BOOKS" table.
5. Reads and prints the data from the "BOOKS" table.

The script is intended to be adapted to different projects and contexts by modifying the tables and data.
"""
#!/usr/bin/python
# -*- coding:utf8 -*
import mysql.connector

print ("MySql tool!\n")

host="localhost"
user='root'
database='test'
password=''

# connect to the database
try:
    db = mysql.connector.connect(host=host, user=user, db=database, password=password)
except:
    msg = f"Error connecting to database {db}, host={host}, user={user}, password={password}"
    print (msg)
    exit(1)

print (f"Connected to database {database} on host {host} with user {user}\n")

cursor = db.cursor(buffered=True)

# Checks that the table BOOKS exists
cursor.execute("""SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'BOOKS'""")
if cursor.rowcount == 0:
    print ("Table BOOKS does not exist")
else:
    print ("Table BOOKS exists")
    # Drop the table
    cursor.execute("DROP TABLE BOOKS")

print ("Creating table BOOKS")
cursor.execute("""CREATE TABLE BOOKS (ID INT NOT NULL AUTO_INCREMENT, TITLE VARCHAR(100), AUTHOR VARCHAR(100), PRIMARY KEY (ID))""")

# search the number of rows in the table
cursor.execute("SELECT COUNT(*) FROM BOOKS")

# print the number of rows

if cursor.rowcount == 0:
    print ("Table BOOKS is empty")
else:
    print ("Table BOOKS is not empty")  
    print ("Dropping rows")  
    # Drop the existing rows
    cursor.execute("DELETE FROM BOOKS")

# insert some data
cursor.execute("INSERT INTO BOOKS (TITLE, AUTHOR) VALUES ('The Hobbit', 'J.R.R. Tolkien')")
cursor.execute("INSERT INTO BOOKS (TITLE, AUTHOR) VALUES ('The Lord of the Rings', 'J.R.R. Tolkien')")
cursor.execute("INSERT INTO BOOKS (TITLE, AUTHOR) VALUES ('The Silmarillion', 'J.R.R. Tolkien')")
cursor.execute("INSERT INTO BOOKS (TITLE, AUTHOR) VALUES ('The Children of Hurin', 'J.R.R. Tolkien')")

# read back the data
cursor.execute("""SELECT * FROM BOOKS""")
for row in cursor:
    print(row)

db.close()

print ("bye")

