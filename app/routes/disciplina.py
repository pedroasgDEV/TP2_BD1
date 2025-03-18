from flask import Blueprint, request, jsonify
from app.models.disciplina import Disciplina

disciplina_bp = Blueprint('disciplina_bp', __name__)

# Criar uma Disciplina
@disciplina_bp.route('/', methods=['POST'])
def create_disciplina():
    disciplina = Disciplina()
    data = request.get_json()
    
    result = disciplina.insert(data)       
    disciplina.close()
    
    if result is None:
        return jsonify({'message': 'Disciplina não criada'}), 400
    return jsonify({'message': 'Disciplina criada', 'codigo': result}), 201

# Obter todos
@disciplina_bp.route('/', methods=['GET'])
def get_disciplina():
    disciplina = Disciplina()
    
    result = disciplina.get_all()
    disciplina.close()

    if result is None:
        return jsonify({'message': 'Disciplina não encontrada'}), 404
    return jsonify(result), 200

# Atualizar dados do disciplina
@disciplina_bp.route('/<codigo>', methods=['PUT'])
def update_disciplina(codigo):
    disciplina = Disciplina()
    data = request.get_json()
    
    result = disciplina.update(codigo, data)
    disciplina.close()
    
    if result:
        return jsonify({'message': 'Disciplina atualizada'}), 204
    return jsonify({'message': 'Disciplina não atualizada'}), 404

# Deletar disciplina
@disciplina_bp.route('/<codigo>', methods=['DELETE'])
def delete_disciplina(codigo):
    disciplina = Disciplina()
    
    result = disciplina.delete(codigo)
    disciplina.close()
    
    if result:
        return jsonify({'message': 'Disciplina deletada'}), 204
    return jsonify({'message': 'Disciplina não encontrada'}), 403