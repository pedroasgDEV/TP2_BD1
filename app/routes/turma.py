from flask import Blueprint, request, jsonify
from app.models.turma import Turma

turma_bp = Blueprint('turma_bp', __name__)

# Criar uma Turma
@turma_bp.route('/', methods=['POST'])
def create_turma():
    turma = Turma()
    data = request.get_json()
    
    result = turma.insert(data)       
    turma.close()
    
    if result is None:
        return jsonify({'message': 'Turma não criada'}), 400
    return jsonify({'message': 'Turma criada', 'id': result}), 201

# Obter todos
@turma_bp.route('/', methods=['GET'])
def get_turma():
    turma = Turma()
    
    result = turma.get_all()
    turma.close()

    if result is None:
        return jsonify({'message': 'Turma não encontrada'}), 404
    return jsonify(result), 200

# Atualizar dados do turma
@turma_bp.route('/<int:turma_id>', methods=['PUT'])
def update_turma(turma_id):
    turma = Turma()
    data = request.get_json()
    
    result = turma.update(turma_id, data)
    turma.close()
    
    if result:
        return jsonify({'message': 'Turma atualizada'}), 204
    return jsonify({'message': 'Turma não atualizada'}), 404

# Deletar turma
@turma_bp.route('/<int:turma_id>', methods=['DELETE'])
def delete_turma(turma_id):
    turma = Turma()
    
    result = turma.delete(turma_id)
    turma.close()
    
    if result:
        return jsonify({'message': 'Turma deletada'}), 204
    return jsonify({'message': 'Turma não encontrada'}), 403