
from pymongo import MongoClient

from config import ConfigMongo

client = MongoClient(ConfigMongo.MONGO_URI)
db = client[ConfigMongo.MONGO_DBNAME]



class Factory:
    def __init__(self, name, location, capacity):
        """
           Initializes an instance of the class with the provided name, location, and capacity.

           This constructor method sets up an object with the specified `name`, `location`,
           and `capacity` attributes. It ensures that the instance is properly initialized
           with the given values.
           """
        self.name = name
        self.location = location
        self.capacity = capacity

    def factory_save(self):
        """
           Saves the current factory instance to the database or persistent storage.

           This method is responsible for storing the state of the current factory
           instance in the database. It handles the process of inserting a new record
           or updating an existing one based on whether the factory is new or already
           exists.
           """
        db.factory.insert_one({
            'name': self.name,
            'location': self.location,
            'capacity': self.capacity
        })


    @staticmethod
    def find_factory_name(name):
        """
            Retrieves a factory record from the database based on the provided name.

            This method searches for and returns a factory record that matches the specified
            `name`. It performs a lookup in the database or other storage system to find
            the record associated with the given name.
            """
        return db.factory.find_one({'name': name})

    @staticmethod
    def factory_get(page, per_page):
        """
            Retrieves a paginated list of factory records from the database.

            This method fetches a subset of factory records based on the specified
            pagination parameters. It returns a list of factories for the requested page,
            with the number of factories per page defined by `per_page`.
            """
        factories = []
        total_count = db.factory.count_documents({})

        skip = (page - 1) * per_page
        limit = per_page

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

    @staticmethod
    def factory_get_by_id(factory_id):
        """
          Retrieves a factory record from the database based on the provided factory ID.

          This method searches for and returns a single factory record that matches the
          specified `factory_id`. It performs a lookup in the database or other storage
          system to find the record associated with the given ID.
          """
        from bson import ObjectId
        return db.factory.find_one({'_id': ObjectId(factory_id)})

    @staticmethod
    def factory_delete(factory_id):
        """
           Deletes a factory record from the database based on the provided factory ID.

           This method removes a specific factory record from the database using the given
           `factory_id`. It handles the deletion of the factory and may also manage related
           cleanup tasks.
           """
        print(factory_id)
        db.factory.delete_one({'_id': factory_id})

    @staticmethod
    def factory_update(factory_id, name, location, capacity):
        """
           Updates the details of a factory record identified by the provided factory ID.

           This method modifies the record of a specific factory in the database using the
           given `factory_id` and updates it with the new `name`, `location`, and `capacity` details.
           """
        update_data = {}
        if name:
            update_data['name'] = name
        if location:
            update_data['location'] = location
        if capacity:
            update_data['capacity'] = capacity

        from bson import ObjectId
        db.factory.update_one(
            {'_id': ObjectId(factory_id)},
            {'$set': update_data}
        )
