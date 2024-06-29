from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.entity_sevices import Entity

entity_bp = Blueprint('entity', __name__)


@entity_bp.route('/entities', methods=['POST'])
@jwt_required()
def create_entity():
    data = request.get_json()
    name = data['name']
    factory = data['factory']

    # if Entity.find_entity_name(name, factory):
    #     return jsonify({'message': 'Factory Name already exists'}), 400

    entity = Entity(name, factory)
    entity.entity_save()

    return jsonify({'message': 'Entity created successfully'}), 201


@entity_bp.route('/entities', methods=['GET'])
@jwt_required()
def get_entity():
    page = request.args.get("page", type=int, default=1)
    per_page = request.args.get("per_page", type=int, default=10)
    print(page,per_page)
    factories, pagination = Entity.entity_get(page, per_page)
    return jsonify(factories, pagination), 200
