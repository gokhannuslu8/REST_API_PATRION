from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.factory_services import Factory


factory_bp = Blueprint('factory', __name__)

@factory_bp.route('/factories', methods=['POST'])
@jwt_required()
def create_factory():
    """
        Creates a new factory record and adds it to the database.

        This function is responsible for creating and storing a new factory record
        in the database. The factory details, such as name, location, and other
        attributes, are typically provided as input parameters or through a request.

        Details of how the function works:
        - The attributes and values required for creating the factory record.
        - Validation of the provided data to ensure it meets the necessary criteria.
        - Handling of cases where the creation operation fails or the data is invalid.
        """
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
    """
        Retrieves a list of factories from the database.

        This function fetches and returns a list of factory records from the database.
        It may include options for pagination, filtering, or sorting depending on
        the implementation details.

        Details of how the function works:
        - Any parameters for filtering or pagination (if applicable).
        - The format of the data returned, such as a list of dictionaries.
        - Handling of cases where no factories are found.
        """
    page = request.args.get("page", type=int, default=1)
    per_page = request.args.get("per_page", type=int, default=10)
    factories, pagination = Factory.factory_get(page, per_page)
    return jsonify(factories, pagination), 200


@factory_bp.route('/factories/<factory_id>', methods=['DELETE'])
@jwt_required()
def delete_factory(factory_id):
    """
    Deletes a factory record from the database based on the provided factory ID.

    This function removes a specific factory record from the database using
    the given `factory_id`. It handles the deletion of the factory and may
    also manage related cleanup tasks.

    Details of how the function works:
    - `factory_id`: The unique identifier of the factory to be deleted.
    - Validation of the `factory_id` to ensure the factory exists in the database.
    - Handling of cases where the `factory_id` is not found or the deletion fails.
    """
    factory = Factory.factory_get_by_id(factory_id)
    print(factory)
    if not factory:
        return jsonify({'message': 'Factory not found'}), 404

    Factory.factory_delete(factory["_id"])
    return jsonify({'message': 'Factory deleted successfully'}), 200


@factory_bp.route('/factories/<factory_id>', methods=['PUT'])
@jwt_required()
def update_factory(factory_id):
    """
      Updates the details of a factory identified by the provided factory ID.

      This function modifies the record of a specific factory in the database
      using the given `factory_id`. The new details to be updated are typically
      provided through additional parameters or input.

      Details of how the function works:
      - `factory_id`: The unique identifier of the factory to be updated.
      - The fields and values to be updated, which should be specified or passed
        alongside the function call.
      - Validation of the `factory_id` to ensure the factory exists in the database.
      - Handling of cases where the update operation fails or the `factory_id` is
        not found.
      """
    data = request.get_json()
    name = data['name']
    location = data['location']
    capacity = data['capacity']

    factory = Factory.factory_get_by_id(factory_id)
    if not factory:
        return jsonify({'message': 'Factory not found'}), 404

    Factory.factory_update(factory_id, name, location, capacity)
    return jsonify({'message': 'Factory updated successfully'}), 200
