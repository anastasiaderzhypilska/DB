from flask import Blueprint, jsonify, request
from app.controllers.review_controller import ReviewController

review_bp = Blueprint("review_bp", __name__, url_prefix="/api/reviews")

@review_bp.route("/", methods=["GET"])
def get_all_reviews():
    reviews = ReviewController.get_all()
    return jsonify([r.to_dict() for r in reviews]), 200

@review_bp.route("/<int:review_id>", methods=["GET"])
def get_review(review_id):
    review = ReviewController.get_by_id(review_id)
    if not review:
        return jsonify({"error": "Not found"}), 404
    return jsonify(review.to_dict()), 200

@review_bp.route("/", methods=["POST"])
def create_review():
    data = request.get_json()
    review = ReviewController.create(data)
    return jsonify(review.to_dict()), 201

@review_bp.route("/<int:review_id>", methods=["PUT"])
def update_review(review_id):
    data = request.get_json()
    review = ReviewController.update(review_id, data)
    if not review:
        return jsonify({"error": "Not found"}), 404
    return jsonify(review.to_dict()), 200

@review_bp.route("/<int:review_id>", methods=["DELETE"])
def delete_review(review_id):
    success = ReviewController.delete(review_id)
    if not success:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"message": "Deleted"}), 200
