from app.dao.photo_dao import PhotoDAO

class PhotoService:
    @staticmethod
    def get_all_photos():
        return PhotoDAO.get_all_photos()
    
    @staticmethod
    def get_photo_by_id(photo_id):
        return PhotoDAO.get_photo_by_id(photo_id)
    
    @staticmethod
    def create_photo(data):
        if not data.get('place_id') or not data.get('photo_url'):
            raise ValueError("Place ID and photo URL are required")
        return PhotoDAO.create_photo(
            data['place_id'],
            data['photo_url'],
            data.get('upload_date')
        )
    
    @staticmethod
    def update_photo(photo_id, data):
        if not data.get('place_id') or not data.get('photo_url'):
            raise ValueError("Place ID and photo URL are required")
        return PhotoDAO.update_photo(
            photo_id,
            data['place_id'],
            data['photo_url'],
            data.get('upload_date')
        )
    
    @staticmethod
    def delete_photo(photo_id):
        return PhotoDAO.delete_photo(photo_id)
    
    @staticmethod
    def get_photos_by_place(place_id):
        return PhotoDAO.get_photos_by_place(place_id)