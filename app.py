from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

from security import authenticate,identity
from resources.user import UserRegister
from resources.item import Item,ItemList 
from resources.store import Store,StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_ECHO'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True

app.secret_key = 'adi'
api = Api(app)

jwt = JWT(app,authenticate,identity)

api.add_resource(Store,'/store/<string:name>')    
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(StoreList,'/stores')



import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

if __name__=='__main__':
    db.init_app(app)
    app.run(port=1983,debug=True)
 