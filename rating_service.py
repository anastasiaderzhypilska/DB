from app.dao.rating_dao import RatingDAO

class RatingService:
    @staticmethod
    def get_all_ratings():
        return RatingDAO.get_all_ratings()
    
    @staticmethod
    def get_rating_by_id(rating_id):
        return RatingDAO.get_rating_by_id(rating_id)
    
    @staticmethod
    def create_rating(data):
        if not data.get('rating_name'):
            raise ValueError("Rating name is required")
        return RatingDAO.create_rating(data['rating_name'])
    
    @staticmethod
    def update_rating(rating_id, data):
        if not data.get('rating_name'):
            raise ValueError("Rating name is required")
        return RatingDAO.update_rating(rating_id, data['rating_name'])
    
    @staticmethod
    def delete_rating(rating_id):
        return RatingDAO.delete_rating(rating_id)