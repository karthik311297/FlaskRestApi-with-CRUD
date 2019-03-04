import sqlite3


conn=sqlite3.connect('data.db')

cursor=conn.cursor()



selection="select * from users"

for row in cursor.execute(selection):
    print(row)

conn.commit()
conn.close()

'''
create="create table users(id int,username text,password text)"

cursor.execute(create)


user=(1,'bob','xnxx')
insertion="insert into users values(?,?,?)"
cursor.execute(insertion,user)

users=[(2,'alice','abcd'),(3,'carl','efgh')]

insert_many="insert into users values(?,?,?)"
cursor.executemany(insert_many,users)
'''
