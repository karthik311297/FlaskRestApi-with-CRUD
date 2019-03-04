import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required 

class Item(Resource):
    
    parser=reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help="This field cannot be left blank!")
    
    @jwt_required()
    def get(self,name):
        item=self.find_by_name(name)
        if item:
            return item
        return {'message':'item not found'},404
           
    @classmethod
    def find_by_name(cls,name):
        conn=sqlite3.connect('data.db')
        cursor=conn.cursor()
        query="select * from items where name=?"
        result=cursor.execute(query,(name,))
        row=result.fetchone()
        conn.close()
        if row:
           return {'item':{'name':row[0],'price':row[1]}}
            
    @classmethod
    def insert(cls,item):
        conn=sqlite3.connect('data.db')
        cursor=conn.cursor()
        query="insert into items values(?,?)"
        cursor.execute(query,(item['name'],item['price']))
        conn.commit()
        conn.close()
    
    @classmethod 
    def update(cls,item):        
        conn=sqlite3.connect('data.db')
        cursor=conn.cursor()
        query="update items set price=? where name=?"
        cursor.execute(query,(item['price'],item['name']))
        conn.commit()
        conn.close()
    
    def post(self,name):
        if self.find_by_name(name):
            return {'message':'item with name-{} already exists'.format(name)},400

        request_data=Item.parser.parse_args()
        
        item={'name':name,'price':request_data['price']}
        
        try:     
             self.insert(item)
        except:
            return {'message':'an internal error occurred while inserting the item'},500
        
        return item, 201   
    
    def delete(self,name):
        query="delete from items where name=?"
        conn=sqlite3.connect('data.db')
        cursor=conn.cursor()
        cursor.execute(query,(name,))
        conn.commit()
        conn.close()
        return {'message':'Item deleted'}
         
    def put(self,name):
        data=Item.parser.parse_args()
        item={'name':name,'price':data['price']}
        if self.find_by_name(name):
            self.update(item)
        else:
            self.insert(item)
    
        return item

class Item_List(Resource):
    def get(self):
        conn=sqlite3.connect('data.db')
        cursor=conn.cursor()
        query="select * from items"
        result=cursor.execute(query)
        items=[]
        for row in result:
            items.append({'name':row[0],'price':row[1]})
        return {'items':items}

