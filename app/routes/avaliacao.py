from flask import Blueprint, request, jsonify
from app.models.avaliacao import Avaliacao

avaliacao_bp = Blueprint('avaliacao_bp', __name__)

# Criar uma avaliação
@avaliacao_bp.route('/', methods=['POST'])
def create_avaliacao():
    avaliacao = Avaliacao()
    data = request.get_json()
    
    result = avaliacao.insert(data)       
    avaliacao.close()
    
    if result is None:
        return jsonify({'message': 'Avaliação não criada'}), 400
    return jsonify({'message': 'Avaliação criada', 'id_turma': result[0], 'data_aplicacao': result[1]}), 201

# Obter todas as avaliações
@avaliacao_bp.route('/', methods=['GET'])
def get_avaliacoes():
    avaliacao = Avaliacao()
    result = avaliacao.get_all()
    avaliacao.close()
    
    if not result:
        return jsonify({'message': 'Nenhuma avaliação encontrada'}), 404
    return jsonify(result), 200

# Deletar uma avaliação específica
@avaliacao_bp.route('/<int:turma_id>/<data_aplicacao>', methods=['DELETE'])
def delete_avaliacao(turma_id, data_aplicacao):
    avaliacao = Avaliacao()
    
    result = avaliacao.delete(turma_id, data_aplicacao)
    avaliacao.close()
    
    if result:
        return jsonify({'message': 'Avaliação deletada'}), 204
    return jsonify({'message': 'Avaliação não encontrada'}), 403
