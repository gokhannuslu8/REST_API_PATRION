from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient

from config import ConfigMongo

client = MongoClient(ConfigMongo.MONGO_URI)
db = client[ConfigMongo.MONGO_DBNAME]


class User:
    def __init__(self, username, password, factory):
        """
           Initializes an instance of the class with the provided username, password, and factory.

           This constructor method sets up an object with the specified `username`,
           `password`, and `factory` attributes. It ensures that the instance is properly
           initialized with the given values.
           """
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.factory = factory

    def save(self):
        """
           Saves the current instance to the database or persistent storage.

           This method is responsible for storing the state of the current object
           in the database or other storage system. It handles the process of
           inserting or updating the record based on whether the object is new or
           already exists.
           """
        db.users.insert_one({
            'username': self.username,
            'password_hash': self.password_hash,
            'factory_name': self.factory
        })

    @staticmethod
    def find_by_username(username):
        """
         Retrieves an instance from the database based on the provided username.

         This method searches for and returns an object that matches the specified
         `username`. It performs a lookup in the database or other storage system to
         find the record associated with the given username.
         """
        return db.users.find_one({'username': username})

    @staticmethod
    def find_by_id(users_id):
        """
           Retrieves an instance from the database based on the provided user ID.

           This method searches for and returns an object that matches the specified
           `users_id`. It performs a lookup in the database or other storage system to
           find the record associated with the given ID..
           """
        return db.users.find_one({'_id': ObjectId(users_id)})

    @staticmethod
    def check_password(hash, password):
        """
         Verifies if the provided password matches the given hashed password.

         This method compares a plain-text `password` with a hashed password stored
         in the system to determine if they match. It is commonly used for user
         authentication to ensure that the entered password is correct.
         """
        return check_password_hash(hash, password)

    @staticmethod
    def get_all_users():
        """
          Retrieves a list of all user records from the database.

          This method fetches and returns a comprehensive list of user records stored
          in the database. It may include options for pagination, filtering, or sorting
          depending on the implementation.
          """
        users = []
        for user in db.users.find({}, {'_id': 0}):
            users.append({
                'username': user['username'],
                'factory_name': user['factory_name']
            })
        return users

    @staticmethod
    def users_get_by_id(users_id):
        """
            Retrieves a user record from the database based on the provided user ID.

            This method searches for and returns a user record that matches the specified
            `users_id`. It performs a lookup in the database or other storage system to
            find the record associated with the given ID.
            """
        return db.users.find_one({'_id': ObjectId(users_id)})

    @staticmethod
    def users_delete(users_id):
        """
            Deletes a user record from the database based on the provided user ID.

            This method removes a specific user record from the database using the given
            `users_id`. It handles the deletion of the user and may also manage related
            cleanup tasks.
            """
        print(users_id)
        db.users.delete_one({'_id': users_id})

    @staticmethod
    def update(user_id, username, password, factory):
        """
        Updates the details of a user record identified by the provided user ID.

        This method modifies the record of a specific user in the database using the
        given `user_id` and updates it with the new `username`, `password`, and
        `factory` details.
        """
        update_data = {}
        if username:
            update_data['username'] = username
        if password:
            update_data['password_hash'] = generate_password_hash(password)
        if factory:
            update_data['factory_name'] = factory
        db.users.update_one(
            {'_id': ObjectId(user_id)},
            {'$set': update_data}
        )