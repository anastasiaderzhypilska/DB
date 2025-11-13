from app.models import db, Rating

class RatingDAO:
    @staticmethod
    def get_all_ratings():
        return Rating.query.all()
    
    @staticmethod
    def get_rating_by_id(rating_id):
        return Rating.query.get(rating_id)
    
    @staticmethod
    def create_rating(rating_name):
        rating = Rating(rating_name=rating_name)
        db.session.add(rating)
        db.session.commit()
        return rating
    
    @staticmethod
    def update_rating(rating_id, rating_name):
        rating = Rating.query.get(rating_id)
        if rating:
            rating.rating_name = rating_name
            db.session.commit()
        return rating
    
    @staticmethod
    def delete_rating(rating_id):
        rating = Rating.query.get(rating_id)
        if rating:
            db.session.delete(rating)
            db.session.commit()
            return True
        return False