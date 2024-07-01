from bson import ObjectId
from pymongo import MongoClient
from config import ConfigMongo

client = MongoClient(ConfigMongo.MONGO_URI)
db = client[ConfigMongo.MONGO_DBNAME]


class Entity:
    def __init__(self, name, factory):
        """
           Initializes an instance of the class with the provided name and factory.

           This constructor method sets up an object with the specified `name` and
           `factory` attributes. It ensures that the instance is properly initialized
           with the given values.
           """
        self.name = name
        self.factory = factory

    def entity_save(self):
        """
            Saves the current entity instance to the database or persistent storage.

            This method is responsible for storing the state of the current entity
            instance in the database. It handles the process of inserting a new record
            or updating an existing one based on whether the entity is new or already
            exists.
            """
        db.entity.insert_one({
            'name': self.name,
            'factory': self.factory,

        })

    @staticmethod
    def find_entity_name(name, factory):
        """
           Retrieves an entity from the database based on the provided name and factory.

           This method searches for and returns an entity record that matches the specified
           `name` and is associated with the given `factory`. It performs a lookup in the
           database or other storage system to find the record that matches both criteria.
           """
        return db.entity.find_one({'name': name, 'factory': factory})

    @staticmethod
    def entity_get(page, per_page):
        """
          Retrieves a paginated list of entity records from the database.

          This method fetches a subset of entity records based on the specified
          pagination parameters. It returns a list of entities for the requested page,
          with the number of entities per page defined by `per_page`.
          """
        _entity = []
        total_count = db.entity.count_documents({})

        skip = (page - 1) * per_page
        limit = per_page

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

    @staticmethod
    def entity_get_by_id(entity_id):
        """
           Retrieves an entity record from the database based on the provided entity ID.

           This method searches for and returns a single entity record that matches the
           specified `entity_id`. It performs a lookup in the database or other storage
           system to find the record associated with the given ID.
           """
        return db.entity.find_one({'_id': ObjectId(entity_id)})

    @staticmethod
    def entity_delete(entity_id):
        """
           Deletes an entity record from the database based on the provided entity ID.

           This method removes a specific entity record from the database using the given
           `entity_id`. It handles the deletion of the entity and may also manage related
           cleanup tasks.
           """
        print(entity_id)
        db.entity.delete_one({'_id': entity_id})

    @staticmethod
    def entity_update(entity_id, name, factory):
        """
            Updates the details of an entity record identified by the provided entity ID.

            This method modifies the record of a specific entity in the database using the
            given `entity_id` and updates it with the new `name` and `factory` details.
            """
        update_data = {}
        if name:
            update_data['name'] = name
        if factory:
            update_data['factory'] = factory

        db.entity.update_one(
            {'_id': ObjectId(entity_id)},
            {'$set': update_data}
        )