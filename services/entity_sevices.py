from pymongo import MongoClient
from config import ConfigMongo

client = MongoClient(ConfigMongo.MONGO_URI)
db = client[ConfigMongo.MONGO_DBNAME]


class Entity:
    def __init__(self, name, factory):
        self.name = name
        self.factory = factory

    def entity_save(self):
        db.entity.insert_one({
            'name': self.name,
            'factory': self.factory,

        })

    @staticmethod
    def find_entity_name(name, factory):
        return db.entity.find_one({'name': name, 'factory': factory})

    @staticmethod
    def entity_get(page, per_page):
        _entity = []
        total_count = db.entity.count_documents({})

        # Calculate pagination parameters
        skip = (page - 1) * per_page
        limit = per_page

        # Fetch factories for the specified page
        for entity in db.entity.find({}, {'_id': 0}).skip(skip).limit(limit):
            _entity.append({
                'factory': entity['factory'],
                'name': entity['name']

            })

        pagination = {

            'total': total_count,
            'page': page,
            'per_page': per_page
        }

        return _entity, pagination
