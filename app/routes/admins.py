from flask import Blueprint, request, jsonify
from app.utils.tables.admins import Admins

admins_bp = Blueprint('admins_bp', __name__)

# Insert Data
@admins_bp.route('/', methods=['POST'])
def create_item():
    adm = Admins()
    data = request.get_json()
    
    result = adm.insert(data)       
    adm.close()
    
    if result is False: return jsonify({'message': 'Admin not created'}), 400
    else: return jsonify({'message': 'Admin created', 'id': result}), 201

# Select Data
@admins_bp.route('/<id>', methods=['GET'])
def select_item(id):
    adm = Admins()
    
    if id == "all": result = adm.select_all()
    else: result = adm.select(id)
    
    adm.close()
    
    if result is False: return jsonify({'message': 'Admin not found'}), 404
    else: return jsonify(result), 200

# Update Data
@admins_bp.route('/<id>', methods=['PUT'])
def update_item(id):
    adm = Admins()
    data = request.get_json()
    
    result = adm.update(id, data)
    adm.close()
    
    if result: return jsonify({'message': 'Admin updated'}), 200
    else: return jsonify({'message': 'Admin not updated'}), 404

# Delete Data
@admins_bp.route('/<id>', methods=['DELETE'])
def delete_item(id):
    adm = Admins()
    
    result = adm.delete(id)
    adm.close()
    
    if result: return jsonify({'message': 'Admin deleted'}), 200
    else: return jsonify({'message': 'Admin not found'}), 404
