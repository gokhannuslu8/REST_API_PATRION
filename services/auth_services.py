from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient

from config import ConfigMongo

client = MongoClient(ConfigMongo.MONGO_URI)
db = client[ConfigMongo.MONGO_DBNAME]


class User:
    def __init__(self, username, password, factory):
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.factory = factory
    def save(self):
        db.users.insert_one({
            'username': self.username,
            'password_hash': self.password_hash,
            'factory_name': self.factory
        })

    @staticmethod
    def find_by_username(username):
        return db.users.find_one({'username': username})

    @staticmethod
    def check_password(hash, password):
        return check_password_hash(hash, password)


    @staticmethod
    def get_all_users():
        users = []
        for user in db.users.find({}, {'_id': 0}):
            users.append({
                'username': user['username'],
                'factory_name': user['factory_name']
            })
        return users