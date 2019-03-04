import sqlite3
from flask_restful import Resource,reqparse

class User:
    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password
    
    @classmethod
    def find_by_username(cls,username):
        conn=sqlite3.connect('data.db')
        cursor=conn.cursor()
        selection="select * from users where username=?"
        result=cursor.execute(selection,(username,))
        row=result.fetchone()
        if row:
            user=cls(*row)
        else:
            user=None
        conn.close()
        return user
    
    @classmethod
    def find_by_id(cls,_id):
        conn=sqlite3.connect('data.db')
        cursor=conn.cursor()
        selection="select * from users where id=?"
        result=cursor.execute(selection,(_id,))
        row=result.fetchone()
        if row:
            user=cls(*row)
        else:
            user=None
        conn.close()
        return user

class Userreg(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',type=str,required=True,help="this is required")
    parser.add_argument('password',type=str,required=True,help="this is required")
    def post(self):
        data=Userreg.parser.parse_args()
        if User.find_by_username(data['username']):
            return {'message':'username already exists'},400
        conn=sqlite3.connect('data.db')
        cursor=conn.cursor()
        ins="insert into users values(NULL,?,?)"
        cursor.execute(ins,(data['username'],data['password']))
        conn.commit()
        conn.close()
        return {'message':'user created'},201
        
