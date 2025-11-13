from flask import jsonify, request, Blueprint
from app.services.category_service import CategoryService

category_bp = Blueprint('category_bp', __name__)

def get_json_data():
    if request.is_json:
        return request.get_json()
    else:
        try:
            return request.get_json(force=True)
        except:
            return None

@category_bp.route('/categories', methods=['GET'])
def get_all_categories():
    try:
        categories = CategoryService.get_all_categories()
        return jsonify([{
            'category_id': category.category_id,
            'name': category.name
        } for category in categories])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@category_bp.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    try:
        category = CategoryService.get_category_by_id(category_id)
        if category:
            return jsonify({
                'category_id': category.category_id,
                'name': category.name
            })
        return jsonify({'error': 'Category not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@category_bp.route('/categories', methods=['POST'])
def create_category():
    try:
        data = get_json_data()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        category = CategoryService.create_category(data)
        return jsonify({
            'category_id': category.category_id,
            'name': category.name
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@category_bp.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    try:
        data = get_json_data()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
            
        category = CategoryService.update_category(category_id, data)
        if category:
            return jsonify({
                'category_id': category.category_id,
                'name': category.name
            })
        return jsonify({'error': 'Category not found'}), 404
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@category_bp.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    try:
        success = CategoryService.delete_category(category_id)
        if success:
            return jsonify({'message': 'Category deleted successfully'})
        return jsonify({'error': 'Category not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500