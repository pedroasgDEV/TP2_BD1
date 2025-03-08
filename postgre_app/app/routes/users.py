from flask import Blueprint, request, jsonify
from app.utils.tables.users import Users

users_bp = Blueprint('users_bp', __name__)

# Insert Data
@users_bp.route('/', methods=['POST'])
def create_item():
    usr = Users()
    data = request.get_json()
    
    result = usr.insert(data)
    usr.close()
    
    if result: return jsonify({'message': 'User created'}), 201
    else: return jsonify({'message': 'User not created'}), 400

# Select Data
@users_bp.route('/<regis_id>', methods=['GET'])
def select_item(regis_id):
    usr = Users()
    
    result = usr.select(regis_id)
    usr.close()
    
    if result is False: return jsonify({'message': 'User not found'}), 404
    else: return jsonify(result), 200

# Update Data
@users_bp.route('/<regis_id>', methods=['PUT'])
def update_item(regis_id):
    usr = Users()
    data = request.get_json()
    
    result = usr.update(regis_id, data)
    usr.close()
    
    if result: return jsonify({'message': 'User updated'}), 200
    else: return jsonify({'message': 'User not updated'}), 404
    
# Delete Data    
@users_bp.route('/<regis_id>', methods=['DELETE'])
def delete_item(regis_id):
    usr = Users()
    
    result = usr.delete(regis_id)        
    usr.close()
    
    if result: return jsonify({'message': 'User deleted'}), 200
    else: return jsonify({'message': 'User not found'}), 404
