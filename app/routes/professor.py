from flask import Blueprint, request, jsonify
from app.models.professor import Professor

professor_bp = Blueprint('professor_bp', __name__)

# Criar um Professor
@professor_bp.route('/', methods=['POST'])
def create_professor():
    professor = Professor()
    data = request.get_json()
    
    result = professor.insert(data)       
    professor.close()
    
    if result is None:
        return jsonify({'message': 'Professor não criado'}), 400
    return jsonify({'message': 'Professor criado', 'cpf': result}), 201

# Obter todos
@professor_bp.route('/', methods=['GET'])
def get_professor():
    professor = Professor()
    
    result = professor.get_all()
    professor.close()

    if result is None:
        return jsonify({'message': 'Professor não encontrado'}), 404
    return jsonify(result), 200

# Atualizar dados do professor
@professor_bp.route('/<cpf>', methods=['PUT'])
def update_professor(cpf):
    professor = Professor()
    data = request.get_json()
    
    result = professor.update(cpf, data)
    professor.close()
    
    if result:
        return jsonify({'message': 'Professor atualizado'}), 204
    return jsonify({'message': 'Professor não atualizado'}), 404

# Deletar professor
@professor_bp.route('/<cpf>', methods=['DELETE'])
def delete_professor(cpf):
    professor = Professor()
    
    result = professor.delete(cpf)
    professor.close()
    
    if result:
        return jsonify({'message': 'Professor deletado'}), 204
    return jsonify({'message': 'Professor não encontrado'}), 403