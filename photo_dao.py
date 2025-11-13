from app.models import db, Photo

class PhotoDAO:
    @staticmethod
    def get_all_photos():
        return Photo.query.all()
    
    @staticmethod
    def get_photo_by_id(photo_id):
        return Photo.query.get(photo_id)
    
    @staticmethod
    def create_photo(place_id, photo_url, upload_date):
        photo = Photo(place_id=place_id, photo_url=photo_url, upload_date=upload_date)
        db.session.add(photo)
        db.session.commit()
        return photo
    
    @staticmethod
    def update_photo(photo_id, place_id, photo_url, upload_date):
        photo = Photo.query.get(photo_id)
        if photo:
            photo.place_id = place_id
            photo.photo_url = photo_url
            photo.upload_date = upload_date
            db.session.commit()
        return photo
    
    @staticmethod
    def delete_photo(photo_id):
        photo = Photo.query.get(photo_id)
        if photo:
            db.session.delete(photo)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_photos_by_place(place_id):
        return Photo.query.filter_by(place_id=place_id).all()