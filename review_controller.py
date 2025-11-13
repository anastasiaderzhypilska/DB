from flask import jsonify, request, Blueprint
from app.services.review_service import ReviewService

review_bp = Blueprint('review_bp', __name__)

def get_json_data():
    if request.is_json:
        return request.get_json()
    else:
        try:
            return request.get_json(force=True)
        except:
            return None

@review_bp.route('/reviews', methods=['GET'])
def get_all_reviews():
    try:
        reviews = ReviewService.get_all_reviews()
        return jsonify([{
            'review_id': review.review_id,
            'user_id': review.user_id,
            'place_id': review.place_id,
            'review_text': review.review_text,
            'review_date': review.review_date.isoformat() if review.review_date else None
        } for review in reviews])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@review_bp.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    try:
        review = ReviewService.get_review_by_id(review_id)
        if review:
            return jsonify({
                'review_id': review.review_id,
                'user_id': review.user_id,
                'place_id': review.place_id,
                'review_text': review.review_text,
                'review_date': review.review_date.isoformat() if review.review_date else None
            })
        return jsonify({'error': 'Review not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@review_bp.route('/reviews', methods=['POST'])
def create_review():
    try:
        data = get_json_data()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        review = ReviewService.create_review(data)
        return jsonify({
            'review_id': review.review_id,
            'user_id': review.user_id,
            'place_id': review.place_id,
            'review_text': review.review_text,
            'review_date': review.review_date.isoformat() if review.review_date else None
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@review_bp.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    try:
        data = get_json_data()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        review = ReviewService.update_review(review_id, data)
        if review:
            return jsonify({
                'review_id': review.review_id,
                'user_id': review.user_id,
                'place_id': review.place_id,
                'review_text': review.review_text,
                'review_date': review.review_date.isoformat() if review.review_date else None
            })
        return jsonify({'error': 'Review not found'}), 404
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@review_bp.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    try:
        success = ReviewService.delete_review(review_id)
        if success:
            return jsonify({'message': 'Review deleted successfully'})
        return jsonify({'error': 'Review not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500