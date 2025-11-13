from flask import jsonify, request, Blueprint
from app.services.location_service import LocationService

location_bp = Blueprint('location_bp', __name__)

def get_json_data():
    if request.is_json:
        return request.get_json()
    else:
        try:
            return request.get_json(force=True)
        except:
            return None

@location_bp.route('/locations', methods=['GET'])
def get_all_locations():
    try:
        locations = LocationService.get_all_locations()
        return jsonify([{
            'location_id': location.location_id,
            'city': location.city,
            'country': location.country
        } for location in locations])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@location_bp.route('/locations/<int:location_id>', methods=['GET'])
def get_location(location_id):
    try:
        location = LocationService.get_location_by_id(location_id)
        if location:
            return jsonify({
                'location_id': location.location_id,
                'city': location.city,
                'country': location.country
            })
        return jsonify({'error': 'Location not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@location_bp.route('/locations', methods=['POST'])
def create_location():
    try:
        data = get_json_data()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        location = LocationService.create_location(data)
        return jsonify({
            'location_id': location.location_id,
            'city': location.city,
            'country': location.country
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@location_bp.route('/locations/<int:location_id>', methods=['PUT'])
def update_location(location_id):
    try:
        data = get_json_data()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        location = LocationService.update_location(location_id, data)
        if location:
            return jsonify({
                'location_id': location.location_id,
                'city': location.city,
                'country': location.country
            })
        return jsonify({'error': 'Location not found'}), 404
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@location_bp.route('/locations/<int:location_id>', methods=['DELETE'])
def delete_location(location_id):
    try:
        success = LocationService.delete_location(location_id)
        if success:
            return jsonify({'message': 'Location deleted successfully'})
        return jsonify({'error': 'Location not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500