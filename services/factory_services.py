from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient

from config import ConfigMongo

client = MongoClient(ConfigMongo.MONGO_URI)
db = client[ConfigMongo.MONGO_DBNAME]



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


    @staticmethod
    def find_factory_name(name):
        return db.factory.find_one({'name': name})

    @staticmethod
    def factory_get(page, per_page):
        factories = []
        total_count = db.factory.count_documents({})

        # Calculate pagination parameters
        skip = (page - 1) * per_page
        limit = per_page

        # Fetch factories for the specified page
        for factory in db.factory.find({}, {'_id': 0}).skip(skip).limit(limit):
            factories.append({
                'name': factory['name'],
                'location': factory['location'],
                'capacity': factory['capacity']
            })

        pagination = {

            'total': total_count,
            'page': page,
            'per_page': per_page
        }

        return factories, pagination