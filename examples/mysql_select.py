#!/usr/bin/python
# -*- coding:utf8 -*

import mysql.connector

print ("MySql example!\n")

db = mysql.connector.connect(host="localhost", user='root', db='test')

cursor = db.cursor()

# SELECT * FROM INFORMATION_SCHEMA.TABLES
cursor.execute("""SELECT * FROM BOOKS""")

for row in cursor:
    print(row)

db.close()

print ("bye")

