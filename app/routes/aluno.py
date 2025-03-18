from flask import Blueprint, request, jsonify
from app.models.aluno import Aluno

aluno_bp = Blueprint('aluno_bp', __name__)

# Criar um aluno
@aluno_bp.route('/', methods=['POST'])
def create_aluno():
    aluno = Aluno()
    data = request.get_json()
    
    result = aluno.insert(data)       
    aluno.close()
    
    if result is None:
        return jsonify({'message': 'Aluno não criado'}), 400
    return jsonify({'message': 'Aluno criado', 'n_matricula': result}), 201

# Obter todos
@aluno_bp.route('/', methods=['GET'])
def get_aluno():
    aluno = Aluno()
    
    result = aluno.get_all()
    aluno.close()

    if result is None:
        return jsonify({'message': 'Aluno não encontrado'}), 404
    return jsonify(result), 200

# Atualizar dados do aluno
@aluno_bp.route('/<n_matricula>', methods=['PUT'])
def update_aluno(n_matricula):
    aluno = Aluno()
    data = request.get_json()
    
    result = aluno.update(n_matricula, data)
    aluno.close()
    
    if result:
        return jsonify({'message': 'Aluno atualizado'}), 204
    return jsonify({'message': 'Aluno não atualizado'}), 404

# Deletar aluno
@aluno_bp.route('/<n_matricula>', methods=['DELETE'])
def delete_aluno(n_matricula):
    aluno = Aluno()
    
    result = aluno.delete(n_matricula)
    aluno.close()
    
    if result:
        return jsonify({'message': 'Aluno deletado'}), 204
    return jsonify({'message': 'Aluno não encontrado'}), 403
