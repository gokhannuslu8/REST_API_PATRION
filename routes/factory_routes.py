from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.factory_services import Factory


factory_bp = Blueprint('factory', __name__)

@factory_bp.route('/factories', methods=['POST'])
@jwt_required()
def create_factory():
    data = request.get_json()
    name = data['name']
    location = data['location']
    capacity = data['capacity']

    if Factory.find_factory_name(name):
        return jsonify({'message': 'Factory Name already exists'}), 400

    factory = Factory(name, location, capacity)
    factory.factory_save()

    return jsonify({'message': 'Factory created successfully'}), 201


@factory_bp.route('/factories', methods=['GET'])
@jwt_required()
def get_factories():
    page = request.args.get("page", type=int, default=1)
    per_page = request.args.get("per_page", type=int, default=10)
    factories, pagination = Factory.factory_get(page, per_page)
    return jsonify(factories, pagination), 200


@factory_bp.route('/factories/<factory_id>', methods=['DELETE'])
@jwt_required()
def delete_factory(factory_id):
    factory = Factory.factory_get_by_id(factory_id)
    print(factory)
    if not factory:
        return jsonify({'message': 'Factory not found'}), 404

    Factory.factory_delete(factory["_id"])
    return jsonify({'message': 'Factory deleted successfully'}), 200


@factory_bp.route('/factories/<factory_id>', methods=['PUT'])
@jwt_required()
def update_factory(factory_id):
    data = request.get_json()
    name = data['name']
    location = data['location']
    capacity = data['capacity']

    factory = Factory.factory_get_by_id(factory_id)
    if not factory:
        return jsonify({'message': 'Factory not found'}), 404

    Factory.factory_update(factory_id, name, location, capacity)
    return jsonify({'message': 'Factory updated successfully'}), 200
