from flask import Flask, jsonify
from app.config import Config
from app.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    

    db.init_app(app)
    

    from app.controllers.owner_controller import owner_bp
    from app.controllers.place_controller import place_bp
    from app.controllers.review_controller import review_bp
    
    app.register_blueprint(owner_bp, url_prefix='/api')
    app.register_blueprint(place_bp, url_prefix='/api')
    app.register_blueprint(review_bp, url_prefix='/api')
    

    @app.route('/')
    def home():
        return jsonify({
            'message': 'Travel Reviews API is working!',
            'available_endpoints': [
                '/api/owners',
                '/api/places', 
                '/api/reviews',
                '/api/health'
            ]
        })
    
    @app.route('/api/health')
    def health_check():
        return jsonify({
            'status': 'healthy', 
            'message': 'API is running',
            'entities': ['owners', 'places', 'reviews']
        })
    

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'error': 'Endpoint not found',
            'message': 'The requested URL was not found on the server',
            'available_endpoints': [
                '/api/owners',
                '/api/places', 
                '/api/reviews',
                '/api/health'
            ]
        }), 404
    
    return app