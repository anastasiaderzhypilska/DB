from app.models import db, Review

class ReviewDAO:
    @staticmethod
    def get_all_reviews():
        return Review.query.all()
    
    @staticmethod
    def get_review_by_id(review_id):
        return Review.query.get(review_id)
    
    @staticmethod
    def create_review(user_id, place_id, review_text, review_date):
        review = Review(
            user_id=user_id,
            place_id=place_id,
            review_text=review_text,
            review_date=review_date
        )
        db.session.add(review)
        db.session.commit()
        return review
    
    @staticmethod
    def update_review(review_id, user_id, place_id, review_text, review_date):
        review = Review.query.get(review_id)
        if review:
            review.user_id = user_id
            review.place_id = place_id
            review.review_text = review_text
            review.review_date = review_date
            db.session.commit()
        return review
    
    @staticmethod
    def delete_review(review_id):
        review = Review.query.get(review_id)
        if review:
            db.session.delete(review)
            db.session.commit()
            return True
        return False