import sqlite3

conn=sqlite3.connect('data.db')

cursor=conn.cursor()

query1="create table if not exists users(id INTEGER PRIMARY KEY,username text,password text)"
query2="create table if not exists items(name text,price real)"

cursor.execute(query1)

cursor.execute(query2)


conn.commit()

conn.close() 
