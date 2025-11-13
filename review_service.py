from app.dao.review_dao import ReviewDAO

class ReviewService:
    @staticmethod
    def get_all_reviews():
        return ReviewDAO.get_all_reviews()
    
    @staticmethod
    def get_review_by_id(review_id):
        return ReviewDAO.get_review_by_id(review_id)
    
    @staticmethod
    def create_review(data):
        if not data.get('user_id') or not data.get('place_id'):
            raise ValueError("User ID and Place ID are required")
        return ReviewDAO.create_review(
            data['user_id'],
            data['place_id'],
            data.get('review_text', ''),
            data.get('review_date')
        )
    
    @staticmethod
    def update_review(review_id, data):
        if not data.get('user_id') or not data.get('place_id'):
            raise ValueError("User ID and Place ID are required")
        return ReviewDAO.update_review(
            review_id,
            data['user_id'],
            data['place_id'],
            data.get('review_text', ''),
            data.get('review_date')
        )
    
    @staticmethod
    def delete_review(review_id):
        return ReviewDAO.delete_review(review_id)