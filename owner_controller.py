from flask import jsonify, request, Blueprint
from app.services.owner_service import OwnerService

owner_bp = Blueprint('owner_bp', __name__)

def get_json_data():
    """Безпечне отримання JSON даних"""
    if request.is_json:
        return request.get_json()
    else:
        try:
            return request.get_json(force=True)
        except:
            return None

@owner_bp.route('/owners', methods=['GET'])
def get_all_owners():
    try:
        owners = OwnerService.get_all_owners()
        return jsonify([{
            'owner_id': owner.owner_id,
            'full_name': owner.full_name,
            'contact_email': owner.contact_email
        } for owner in owners])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@owner_bp.route('/owners/<int:owner_id>', methods=['GET'])
def get_owner(owner_id):
    try:
        owner = OwnerService.get_owner_by_id(owner_id)
        if owner:
            return jsonify({
                'owner_id': owner.owner_id,
                'full_name': owner.full_name,
                'contact_email': owner.contact_email
            })
        return jsonify({'error': 'Owner not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@owner_bp.route('/owners', methods=['POST'])
def create_owner():
    try:
        data = get_json_data()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        owner = OwnerService.create_owner(data)
        return jsonify({
            'owner_id': owner.owner_id,
            'full_name': owner.full_name,
            'contact_email': owner.contact_email
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@owner_bp.route('/owners/<int:owner_id>', methods=['PUT'])
def update_owner(owner_id):
    try:
        data = get_json_data()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        owner = OwnerService.update_owner(owner_id, data)
        if owner:
            return jsonify({
                'owner_id': owner.owner_id,
                'full_name': owner.full_name,
                'contact_email': owner.contact_email
            })
        return jsonify({'error': 'Owner not found'}), 404
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@owner_bp.route('/owners/<int:owner_id>', methods=['DELETE'])
def delete_owner(owner_id):
    try:
        success = OwnerService.delete_owner(owner_id)
        if success:
            return jsonify({'message': 'Owner deleted successfully'})
        return jsonify({'error': 'Owner not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@owner_bp.route('/owners/<int:owner_id>/places', methods=['GET'])
def get_owner_places(owner_id):
    try:
        places = OwnerService.get_owner_places(owner_id)
        return jsonify([{
            'place_id': place.place_id,
            'name': place.name,
            'description': place.description
        } for place in places])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@owner_bp.route('/owners/debug/<int:owner_id>', methods=['GET'])
def debug_owner(owner_id):
    try:
        owner = OwnerService.get_owner_by_id(owner_id)
        if not owner:
            return jsonify({'error': 'Owner not found'}), 404
            
        places = OwnerService.get_owner_places(owner_id)
        
        return jsonify({
            'owner': {
                'owner_id': owner.owner_id,
                'full_name': owner.full_name,
                'contact_email': owner.contact_email
            },
            'places_count': len(places),
            'places': [{
                'place_id': place.place_id,
                'name': place.name,
                'description': place.description
            } for place in places]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@owner_bp.route('/owners/check', methods=['GET'])
def check_owners():
    try:
        owners = OwnerService.get_all_owners()
        owner_ids = [owner.owner_id for owner in owners]
        return jsonify({
            'available_owner_ids': owner_ids,
            'message': f'Доступні ID власників: {owner_ids}',
            'total_owners': len(owners)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500