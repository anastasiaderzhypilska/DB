from app.dao.place_dao import PlaceDAO

class PlaceService:
    @staticmethod
    def get_all_places():
        return PlaceDAO.get_all_places()
    
    @staticmethod
    def get_place_by_id(place_id):
        return PlaceDAO.get_place_by_id(place_id)
    
    @staticmethod
    def create_place(data):
        if not data.get('name'):
            raise ValueError("Place name is required")
        return PlaceDAO.create_place(
            data['name'],
            data.get('description', ''),
            data.get('category_id'),
            data.get('location_id')
        )
    
    @staticmethod
    def update_place(place_id, data):
        if not data.get('name'):
            raise ValueError("Place name is required")
        return PlaceDAO.update_place(
            place_id,
            data['name'],
            data.get('description', ''),
            data.get('category_id'),
            data.get('location_id')
        )
    
    @staticmethod
    def delete_place(place_id):
        return PlaceDAO.delete_place(place_id)
    
    @staticmethod
    def get_place_owners(place_id):
        return PlaceDAO.get_place_owners(place_id)
    
    @staticmethod
    def get_place_reviews(place_id):
        return PlaceDAO.get_place_reviews(place_id)