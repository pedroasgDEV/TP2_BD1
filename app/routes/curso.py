from flask import Blueprint, request, jsonify
from app.models.curso import Curso

curso_bp = Blueprint('curso_bp', __name__)

# Criar um Curso
@curso_bp.route('/', methods=['POST'])
def create_curso():
    curso = Curso()
    data = request.get_json()
    
    result = curso.insert(data)       
    curso.close()
    
    if result is None:
        return jsonify({'message': 'Curso não criado'}), 400
    return jsonify({'message': 'Curso criado', 'codigo': result}), 201

# Obter todos
@curso_bp.route('/', methods=['GET'])
def get_curso():
    curso = Curso()
    
    result = curso.get_all()
    curso.close()

    if result is None:
        return jsonify({'message': 'Curso não encontrado'}), 404
    return jsonify(result), 200

# Atualizar dados do curso
@curso_bp.route('/<int:codigo>', methods=['PUT'])
def update_curso(codigo):
    curso = Curso()
    data = request.get_json()
    
    result = curso.update(codigo, data)
    curso.close()
    
    if result:
        return jsonify({'message': 'Curso atualizado'}), 204
    return jsonify({'message': 'Curso não atualizado'}), 404

# Deletar curso
@curso_bp.route('/<int:codigo>', methods=['DELETE'])
def delete_curso(codigo):
    curso = Curso()
    
    result = curso.delete(codigo)
    curso.close()
    
    if result:
        return jsonify({'message': 'Curso deletado'}), 204
    return jsonify({'message': 'Curso não encontrado'}), 403