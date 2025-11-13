from flask import jsonify, request, Blueprint
from app.services.user_service import UserService

user_bp = Blueprint('user_bp', __name__)

def get_json_data():
    if request.is_json:
        return request.get_json()
    else:
        try:
            return request.get_json(force=True)
        except:
            return None

@user_bp.route('/users', methods=['GET'])
def get_all_users():
    try:
        users = UserService.get_all_users()
        return jsonify([{
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email
        } for user in users])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = UserService.get_user_by_id(user_id)
        if user:
            return jsonify({
                'user_id': user.user_id,
                'username': user.username,
                'email': user.email
            })
        return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/users', methods=['POST'])
def create_user():
    try:
        data = get_json_data()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        user = UserService.create_user(data)
        return jsonify({
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = get_json_data()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        user = UserService.update_user(user_id, data)
        if user:
            return jsonify({
                'user_id': user.user_id,
                'username': user.username,
                'email': user.email
            })
        return jsonify({'error': 'User not found'}), 404
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        success = UserService.delete_user(user_id)
        if success:
            return jsonify({'message': 'User deleted successfully'})
        return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500