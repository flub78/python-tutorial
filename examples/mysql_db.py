#!/usr/bin/python
# -*- coding:utf8 -*

# https://www.radishlogic.com/coding/python-3/installing-mysqldb-for-python-3-in-windows/



import MySQLdb

print ("MySql example!\n")

db = MySQLdb.connect(host="localhost", user='root', db='test')

# SELECT * FROM INFORMATION_SCHEMA.TABLES
db.query("""SELECT * FROM INFORMATION_SCHEMA.TABLES""")
# db.query("""SELECT * FROM BOOKS""")

r=db.store_result()
rows = r.fetch_row(maxrows=0)
for row in rows:
    print(row)

db.close()

print ("bye")

