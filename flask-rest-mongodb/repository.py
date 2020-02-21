from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'user_db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/user_db'

mongo = PyMongo(app)

def get_all():
    users = mongo.db.users
    return users.find()

def get_one(name):
    users = mongo.db.users
    return users.find_one({'name' : name})

def add_one(name, email):
    users = mongo.db.users
    user_id = users.insert({'name': name, 'email': email})
    return users.find_one({'_id': user_id })