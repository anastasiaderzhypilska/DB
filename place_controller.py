from flask import jsonify, request, Blueprint
from app.services.place_service import PlaceService

place_bp = Blueprint('place_bp', __name__)

def get_json_data():
    if request.is_json:
        return request.get_json()
    else:
        try:
            return request.get_json(force=True)
        except:
            return None

@place_bp.route('/places', methods=['GET'])
def get_all_places():
    try:
        places = PlaceService.get_all_places()
        return jsonify([{
            'place_id': place.place_id,
            'name': place.name,
            'description': place.description,
            'category_id': place.category_id,
            'location_id': place.location_id
        } for place in places])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@place_bp.route('/places/<int:place_id>', methods=['GET'])
def get_place(place_id):
    try:
        place = PlaceService.get_place_by_id(place_id)
        if place:
            return jsonify({
                'place_id': place.place_id,
                'name': place.name,
                'description': place.description,
                'category_id': place.category_id,
                'location_id': place.location_id
            })
        return jsonify({'error': 'Place not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@place_bp.route('/places', methods=['POST'])
def create_place():
    try:
        data = get_json_data()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        place = PlaceService.create_place(data)
        return jsonify({
            'place_id': place.place_id,
            'name': place.name,
            'description': place.description,
            'category_id': place.category_id,
            'location_id': place.location_id
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@place_bp.route('/places/<int:place_id>', methods=['PUT'])
def update_place(place_id):
    try:
        data = get_json_data()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        place = PlaceService.update_place(place_id, data)
        if place:
            return jsonify({
                'place_id': place.place_id,
                'name': place.name,
                'description': place.description,
                'category_id': place.category_id,
                'location_id': place.location_id
            })
        return jsonify({'error': 'Place not found'}), 404
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@place_bp.route('/places/<int:place_id>', methods=['DELETE'])
def delete_place(place_id):
    try:
        success = PlaceService.delete_place(place_id)
        if success:
            return jsonify({'message': 'Place deleted successfully'})
        return jsonify({'error': 'Place not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@place_bp.route('/places/<int:place_id>/owners', methods=['GET'])
def get_place_owners(place_id):
    try:
        owners = PlaceService.get_place_owners(place_id)
        return jsonify([{
            'owner_id': owner.owner_id,
            'full_name': owner.full_name,
            'contact_email': owner.contact_email
        } for owner in owners])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@place_bp.route('/places/<int:place_id>/reviews', methods=['GET'])
def get_place_reviews(place_id):
    try:
        reviews = PlaceService.get_place_reviews(place_id)
        return jsonify([{
            'review_id': review.review_id,
            'review_text': review.review_text,
            'review_date': review.review_date.isoformat() if review.review_date else None,
            'user_id': review.user_id
        } for review in reviews])
    except Exception as e:
        return jsonify({'error': str(e)}), 500