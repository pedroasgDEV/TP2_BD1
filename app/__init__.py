from flask import Flask
from app.routes.users import users_bp
from app.routes.admins import admins_bp
from app.routes.login import login_bp
from app.routes.subjects import subjects_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(admins_bp, url_prefix='/api/admins')
    app.register_blueprint(login_bp, url_prefix='/api/login')
    app.register_blueprint(subjects_bp, url_prefix='/api/subjects')
    
    return app