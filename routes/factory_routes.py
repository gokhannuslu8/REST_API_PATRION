from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from flask_jwt_extended import jwt_required
from services.factory_services import Factory
from utils.pagination import paginate

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

factory_bp = Blueprint('factory', __name__)

@factory_bp.route('/factories', methods=['POST'])
@jwt_required()
def create_factory():
    data = request.get_json()
    name = data['name']
    location = data['location']
    capacity = data['capacity']
    factory = Factory(name, location, capacity)
    factory.factory_save()

    return jsonify({'message': 'Factory created successfully'}), 201

@factory_bp.route('/factories', methods=['GET'])
@jwt_required()
def get_factories():
    page = request.args.get('page', 1)
    per_page = request.args.get('perPage', 10)
    factories = db.factories.find()
    result = paginate(factories, page, per_page)
    return jsonify(result), 200
