from flask import Flask
from app.routes.aluno import aluno_bp
from app.routes.areas import areas_bp
from app.routes.avaliacao import avaliacao_bp
from app.routes.curso import curso_bp
from app.routes.disciplina import disciplina_bp
from app.routes.professor import professor_bp
from app.routes.turma import turma_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(aluno_bp, url_prefix='/api/aluno')
    app.register_blueprint(areas_bp, url_prefix='/api/areas')
    app.register_blueprint(avaliacao_bp, url_prefix='/api/avaliacao')
    app.register_blueprint(curso_bp, url_prefix='/api/curso')
    app.register_blueprint(disciplina_bp, url_prefix='/api/disciplina')
    app.register_blueprint(professor_bp, url_prefix='/api/professor')
    app.register_blueprint(turma_bp, url_prefix='/api/turma')
    
    return app