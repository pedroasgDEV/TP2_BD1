from flask import Blueprint, request, jsonify
from app.utils.tables.subjects import Subjects
from app.utils.tables.user_subjects import UsrSub
from app.utils.tables.admin_subjects import AdmSub
from app.utils.tables.users import Users
from app.utils.tables.admins import Admins

subjects_bp = Blueprint('subjects_bp', __name__)

# Insert Data
@subjects_bp.route('/', methods=['POST'])
def create_subject():
    sub = Subjects()
    data = request.get_json()
    
    result = sub.insert(data)       
    sub.close()
    
    if result: return jsonify({'message': 'Subject created'}), 201
    else: return jsonify({'message': 'Subject not created'}), 400

# Select Data
@subjects_bp.route('/<subject_code>', methods=['GET'])
def select_subject(subject_code):
    sub = Subjects()
    
    if subject_code == "all": result = sub.select_all()
    else: result = sub.select(subject_code)
    
    sub.close()
    
    if result is False: return jsonify({'message': 'Subject not found'}), 404
    else: return jsonify(result), 200

# Update Data
@subjects_bp.route('/<subject_code>', methods=['PUT'])
def update_subject(subject_code):
    sub = Subjects()
    data = request.get_json()
    
    result = sub.update(subject_code, data)
    sub.close()
    
    if result: return jsonify({'message': 'Subject updated'}), 200
    else: return jsonify({'message': 'Subject not updated'}), 404

# Delete Data
@subjects_bp.route('/<subject_code>', methods=['DELETE'])
def delete_subject(subject_code):
    sub = Subjects()
    
    result = sub.delete(subject_code)
    sub.close()
    
    if result: return jsonify({'message': 'Subject deleted'}), 200
    else: return jsonify({'message': 'Subject not found'}), 404

# Create user connection
@subjects_bp.route('/users/', methods=['POST'])
def create_user_subject_connection():
    usrsub = UsrSub()
    sub = Subjects()
    usr = Users()
    
    user_id = request.args.get("user")
    subject_code = request.args.get("subject")
    
    if user_id is None or subject_code is None:
        usrsub.close()
        sub.close()
        usr.close()
        return jsonify({'message': 'Missing Args'}), 400
    
    if usr.select(user_id) is False:
        usrsub.close()
        sub.close()
        usr.close()
        return jsonify({'message': 'User not found'}), 404
    
    if sub.select(subject_code) is False: 
        usrsub.close()
        sub.close()
        usr.close()
        return jsonify({'message': 'Subject not found'}), 404
    
    result = usrsub.insert(user_id, subject_code)
    
    usrsub.close()
    sub.close()
    usr.close()
    
    if result: return jsonify({'message': 'Connection created'}), 201
    else: return jsonify({'message': 'Connection not created'}), 400

# Select user connections
@subjects_bp.route('/users/', methods=['GET'])
def select_user_subject_connection():
    usrsub = UsrSub()
    
    user_id = request.args.get("user")
    subject_code = request.args.get("subject")
    
    if user_id is not None and subject_code is not None:
        if usrsub.verify(user_id, subject_code):
            usrsub.close()
            return jsonify({'message': 'Connection found'}), 200
        else:
            usrsub.close()
            return jsonify({'message': 'Connection not found'}), 404
        
    if user_id is not None and subject_code is None:
        results = usrsub.select_all_subjects(user_id)
        usrsub.close()
        if results is False: return jsonify({'message': 'Subjects not found'}), 404
        else: return jsonify(results), 200
        
    if user_id is None and subject_code is not None:
        results = usrsub.select_all_users(subject_code)
        usrsub.close()
        if results is False: return jsonify({'message': 'Users not found'}), 404
        else: return jsonify(results), 200
    
    usrsub.close()
    return jsonify({'message': 'Missing Args'}), 400

# Delete user connection
@subjects_bp.route('/users/', methods=['DELETE'])
def delete_user_subject_connection():
    usrsub = UsrSub()
    
    user_id = request.args.get("user")
    subject_code = request.args.get("subject")
    
    if user_id is None or subject_code is None:
        usrsub.close()
        return jsonify({'message': 'Missing Args'}), 400
    
    result = usrsub.delete(user_id, subject_code)
    usrsub.close()
    
    if result: return jsonify({'message': 'Connection deleted'}), 200
    else: return jsonify({'message': 'Connection not found'}), 404

# Create admin connection
@subjects_bp.route('/admins/', methods=['POST'])
def create_admin_subject_connection():
    admsub = AdmSub()
    sub = Subjects()
    adm = Admins()
    
    admin_id = request.args.get("admin")
    subject_code = request.args.get("subject")
    
    if admin_id is None or subject_code is None:
        admsub.close()
        sub.close()
        adm.close()
        return jsonify({'message': 'Missing Args'}), 400
    
    if adm.select(admin_id) is False:
        admsub.close()
        sub.close()
        adm.close()
        return jsonify({'message': 'Admin not found'}), 404
    
    if sub.select(subject_code) is False: 
        admsub.close()
        sub.close()
        adm.close()
        return jsonify({'message': 'Subject not found'}), 404
    
    result = admsub.insert(admin_id, subject_code)
    admsub.close()
    sub.close()
    adm.close()
    
    if result: return jsonify({'message': 'Connection created'}), 201
    else: return jsonify({'message': 'Connection not created'}), 400

# Select admin connections
@subjects_bp.route('/admins/', methods=['GET'])
def select_admin_subject_connection():
    admsub = AdmSub()
    
    admin_id = request.args.get("admin")
    subject_code = request.args.get("subject")
    
    if admin_id is not None and subject_code is not None:
        if admsub.verify(admin_id, subject_code):
            admsub.close()
            return jsonify({'message': 'Connection found'}), 200
        else:
            admsub.close()
            return jsonify({'message': 'Connection not found'}), 404
        
    if admin_id is not None and subject_code is None:
        results = admsub.select_all_subjects(admin_id)
        admsub.close()
        if results is False: return jsonify({'message': 'Subjects not found'}), 404
        else: return jsonify(results), 200
        
    if admin_id is None and subject_code is not None:
        results = admsub.select_all_admins(subject_code)
        admsub.close()
        if results is False: return jsonify({'message': 'Admins not found'}), 404
        else: return jsonify(results), 200
    
    admsub.close()
    return jsonify({'message': 'Missing Args'}), 400

# Delete admin connection
@subjects_bp.route('/admins/', methods=['DELETE'])
def delete_admin_subject_connection():
    admsub = AdmSub()
    
    admin_id = request.args.get("admin")
    subject_code = request.args.get("subject")
    
    if admin_id is None or subject_code is None:
        admsub.close()
        return jsonify({'message': 'Missing Args'}), 400
    
    result = admsub.delete(admin_id, subject_code)
    admsub.close()
    
    if result: return jsonify({'message': 'Connection deleted'}), 200
    else: return jsonify({'message': 'Connection not found'}), 404