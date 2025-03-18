from flask import Blueprint, request, jsonify
from app.models.areas import Areas

areas_bp = Blueprint('areas_bp', __name__)

# Criar uma Area
@areas_bp.route('/', methods=['POST'])
def create_area():
    area = Areas()
    data = request.get_json()
    
    result = area.insert(data)       
    area.close()
    
    if result is None:
        return jsonify({'message': 'Area não criada'}), 400
    return jsonify({'message': 'Areas criada', 'id': result}), 201

# Obter todos
@areas_bp.route('/', methods=['GET'])
def get_area():
    area = Areas()
    
    result = area.get_all()
    area.close()

    if result is None:
        return jsonify({'message': 'Area não encontrada'}), 404
    return jsonify(result), 200

# Atualizar dados do area
@areas_bp.route('/<int:id_area>', methods=['PUT'])
def update_area(id_area):
    area = Areas()
    data = request.get_json()
    
    result = area.update(id_area, data)
    area.close()
    
    if result:
        return jsonify({'message': 'Areas atualizada'}), 204
    return jsonify({'message': 'Areas não atualizada'}), 404

# Deletar area
@areas_bp.route('/<int:id_area>', methods=['DELETE'])
def delete_area(id_area):
    area = Areas()
    
    result = area.delete(id_area)
    area.close()
    
    if result:
        return jsonify({'message': 'Areas deletada'}), 204
    return jsonify({'message': 'Areas não encontrada'}), 403