from flask import Flask,request
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from user import Userreg
from items import Item,Item_List

app=Flask(__name__)
app.secret_key='karthik'
api=Api(app)

jwt=JWT(app,authenticate,identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Item_List, '/items')
api.add_resource(Userreg,'/register')

app.run(port=5000, debug=True)
 
