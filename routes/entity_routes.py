from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from flask_jwt_extended import jwt_required

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

entity_bp = Blueprint('entity', __name__)

@entity_bp.route('/entities', methods=['POST'])
@jwt_required()
def create_entity():
    data = request.get_json()
    name = data['name']
    factory = data['factory']

    db.entities.insert_one({
        'name': name,
        'factory': factory
    })

    return jsonify({'message': 'Entity created successfully'}), 201

@entity_bp.route('/entities', methods=['GET'])
@jwt_required()
def get_entities():
    page = request.args.get('page', 1)
    per_page = request.args.get('perPage', 10)
    entities = db.entities.find()
    from utils.pagination import paginate
    result = paginate(entities, page, per_page)
    return jsonify(result), 200
