from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['RestApiPatrion']


class Factory:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity
    def factory_save(self):
        db.factory.insert_one({
            'name': self.name,
            'location': self.location,
            'capacity': self.capacity
        })

