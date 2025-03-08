from flask import Blueprint, request, jsonify
from app.utils.tables.admins import Admins
from app.utils.tables.users import Users

login_bp = Blueprint('login_bp', __name__)

# Login Data
@login_bp.route('/', methods=['GET'])
def login():
    usr = Users()
    adm = Admins()
    data = request.get_json()
    
    result = usr.login(data)  
    usr.close()
    
    if result is False: 
        result = adm.login(data)
        adm.close()
        
        if result is False: return jsonify({'message': 'Not found'}), 404
        
        return jsonify({'type': 'admin', 'obj': result}), 200
            
    return jsonify({'type': 'user', 'obj': result}), 200