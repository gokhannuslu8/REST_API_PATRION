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
    # return jsonify({'message': 'Factory Name already exists'}), 400

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


@entity_bp.route('/entities/<entity_id>', methods=['DELETE'])
@jwt_required()
def delete_entity(entity_id):
    entity = Entity.entity_get_by_id(entity_id)
    print(entity)
    if not entity:
        return jsonify({'message': 'Entity not found'}), 404

    Entity.entity_delete(entity["_id"])
    return jsonify({'message': 'Entity deleted successfully'}), 200


@entity_bp.route('/entities/<entity_id>', methods=['PUT'])
@jwt_required()
def update_entity(entity_id):
    data = request.get_json()
    name = data.get('name')
    factory = data.get('factory')

    entity = Entity.entity_get_by_id(entity_id)
    if not entity:
        return jsonify({'message': 'Entity not found'}), 404

    Entity.entity_update(entity_id, name, factory)
    return jsonify({'message': 'Entity updated successfully'}), 200