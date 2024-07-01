from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.entity_sevices import Entity

entity_bp = Blueprint('entity', __name__)


@entity_bp.route('/entities', methods=['POST'])
@jwt_required()
def create_entity():
    """
       Creates a new entity and adds it to the database.

       This function is responsible for creating and storing a new entity record
       in the database. The details of the entity, such as its attributes and values,
       are typically provided as input parameters or through a request.

       Details of how the function works:
       - The attributes and values required for creating the entity.
       - Validation of the provided data to ensure it meets the necessary criteria.
       - Handling of cases where the creation operation fails or the data is invalid.
       """
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
    """
       Retrieves an entity from the database based on specified criteria.

       This function fetches and returns an entity record from the database. The
       criteria for retrieving the entity, such as an identifier or query parameters,
       should be specified or provided as part of the function call.

       Details of how the function works:
       - Criteria for selecting the entity, such as an ID or query parameters.
       - Format of the returned data, typically a dictionary representing the entity.
       - Handling of cases where the entity is not found or if there are issues with
         the retrieval.
       """
    page = request.args.get("page", type=int, default=1)
    per_page = request.args.get("per_page", type=int, default=10)
    print(page,per_page)
    factories, pagination = Entity.entity_get(page, per_page)
    return jsonify(factories, pagination), 200


@entity_bp.route('/entities/<entity_id>', methods=['DELETE'])
@jwt_required()
def delete_entity(entity_id):
    """
     Deletes an entity from the database based on the provided entity ID.

     This function removes a specific entity record from the database using
     the given `entity_id`. It handles the deletion of the entity and may also
     manage related cleanup tasks.

     Details of how the function works:
     - `entity_id`: The unique identifier of the entity to be deleted.
     - Validation of the `entity_id` to ensure the entity exists in the database.
     - Handling of cases where the `entity_id` is not found or the deletion fails.
     """
    entity = Entity.entity_get_by_id(entity_id)
    print(entity)
    if not entity:
        return jsonify({'message': 'Entity not found'}), 404

    Entity.entity_delete(entity["_id"])
    return jsonify({'message': 'Entity deleted successfully'}), 200


@entity_bp.route('/entities/<entity_id>', methods=['PUT'])
@jwt_required()
def update_entity(entity_id):
    """
      Updates the details of an entity identified by the provided entity ID.

      This function modifies the record of a specific entity in the database
      using the given `entity_id`. The new details to be updated are typically
      provided through additional parameters or input.

      Details of how the function works:
      - `entity_id`: The unique identifier of the entity to be updated.
      - The fields and values to be updated, which should be specified or passed
        alongside the function call.
      - Validation of the `entity_id` to ensure the entity exists in the database.
      - Handling of cases where the update operation fails or the `entity_id` is
        not found.
      """
    data = request.get_json()
    name = data.get('name')
    factory = data.get('factory')

    entity = Entity.entity_get_by_id(entity_id)
    if not entity:
        return jsonify({'message': 'Entity not found'}), 404

    Entity.entity_update(entity_id, name, factory)
    return jsonify({'message': 'Entity updated successfully'}), 200