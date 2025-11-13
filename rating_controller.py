from flask import jsonify, request, Blueprint
from app.services.rating_service import RatingService

rating_bp = Blueprint('rating_bp', __name__)

def get_json_data():
    if request.is_json:
        return request.get_json()
    else:
        try:
            return request.get_json(force=True)
        except:
            return None

@rating_bp.route('/ratings', methods=['GET'])
def get_all_ratings():
    try:
        ratings = RatingService.get_all_ratings()
        return jsonify([{
            'rating_id': rating.rating_id,
            'rating_name': rating.rating_name
        } for rating in ratings])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@rating_bp.route('/ratings/<int:rating_id>', methods=['GET'])
def get_rating(rating_id):
    try:
        rating = RatingService.get_rating_by_id(rating_id)
        if rating:
            return jsonify({
                'rating_id': rating.rating_id,
                'rating_name': rating.rating_name
            })
        return jsonify({'error': 'Rating not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@rating_bp.route('/ratings', methods=['POST'])
def create_rating():
    try:
        data = get_json_data()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        rating = RatingService.create_rating(data)
        return jsonify({
            'rating_id': rating.rating_id,
            'rating_name': rating.rating_name
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@rating_bp.route('/ratings/<int:rating_id>', methods=['PUT'])
def update_rating(rating_id):
    try:
        data = get_json_data()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        rating = RatingService.update_rating(rating_id, data)
        if rating:
            return jsonify({
                'rating_id': rating.rating_id,
                'rating_name': rating.rating_name
            })
        return jsonify({'error': 'Rating not found'}), 404
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@rating_bp.route('/ratings/<int:rating_id>', methods=['DELETE'])
def delete_rating(rating_id):
    try:
        success = RatingService.delete_rating(rating_id)
        if success:
            return jsonify({'message': 'Rating deleted successfully'})
        return jsonify({'error': 'Rating not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500