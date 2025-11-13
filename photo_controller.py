from flask import jsonify, request, Blueprint
from app.services.photo_service import PhotoService

photo_bp = Blueprint('photo_bp', __name__)

def get_json_data():
    if request.is_json:
        return request.get_json()
    else:
        try:
            return request.get_json(force=True)
        except:
            return None

@photo_bp.route('/photos', methods=['GET'])
def get_all_photos():
    try:
        photos = PhotoService.get_all_photos()
        return jsonify([{
            'photo_id': photo.photo_id,
            'place_id': photo.place_id,
            'photo_url': photo.photo_url,
            'upload_date': photo.upload_date.isoformat() if photo.upload_date else None
        } for photo in photos])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@photo_bp.route('/photos/<int:photo_id>', methods=['GET'])
def get_photo(photo_id):
    try:
        photo = PhotoService.get_photo_by_id(photo_id)
        if photo:
            return jsonify({
                'photo_id': photo.photo_id,
                'place_id': photo.place_id,
                'photo_url': photo.photo_url,
                'upload_date': photo.upload_date.isoformat() if photo.upload_date else None
            })
        return jsonify({'error': 'Photo not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@photo_bp.route('/photos', methods=['POST'])
def create_photo():
    try:
        data = get_json_data()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        photo = PhotoService.create_photo(data)
        return jsonify({
            'photo_id': photo.photo_id,
            'place_id': photo.place_id,
            'photo_url': photo.photo_url,
            'upload_date': photo.upload_date.isoformat() if photo.upload_date else None
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@photo_bp.route('/photos/<int:photo_id>', methods=['PUT'])
def update_photo(photo_id):
    try:
        data = get_json_data()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        photo = PhotoService.update_photo(photo_id, data)
        if photo:
            return jsonify({
                'photo_id': photo.photo_id,
                'place_id': photo.place_id,
                'photo_url': photo.photo_url,
                'upload_date': photo.upload_date.isoformat() if photo.upload_date else None
            })
        return jsonify({'error': 'Photo not found'}), 404
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@photo_bp.route('/photos/<int:photo_id>', methods=['DELETE'])
def delete_photo(photo_id):
    try:
        success = PhotoService.delete_photo(photo_id)
        if success:
            return jsonify({'message': 'Photo deleted successfully'})
        return jsonify({'error': 'Photo not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@photo_bp.route('/places/<int:place_id>/photos', methods=['GET'])
def get_place_photos(place_id):
    try:
        photos = PhotoService.get_photos_by_place(place_id)
        return jsonify([{
            'photo_id': photo.photo_id,
            'photo_url': photo.photo_url,
            'upload_date': photo.upload_date.isoformat() if photo.upload_date else None
        } for photo in photos])
    except Exception as e:
        return jsonify({'error': str(e)}), 500