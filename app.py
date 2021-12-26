import re
import os


from flask import Flask
from flask_restful import Api
from flask_jwt import JWT 
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from db import db
from resources.store import Store, StoreList

uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app = Flask(__name__)
sqlite_uri = 'sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = uri if uri else sqlite_uri
#os.environ.get('DATABASE_URL','sqlite:///data.db')    # can also be Mysql, postgreSql, etc.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'abigail'
api = Api(app)


jwt = JWT(app, authenticate, identity)   # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') # http://127.0.0.0:5000/student/John
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000)

