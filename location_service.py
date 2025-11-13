from app.dao.location_dao import LocationDAO

class LocationService:
    @staticmethod
    def get_all_locations():
        return LocationDAO.get_all_locations()
    
    @staticmethod
    def get_location_by_id(location_id):
        return LocationDAO.get_location_by_id(location_id)
    
    @staticmethod
    def create_location(data):
        if not data.get('city') or not data.get('country'):
            raise ValueError("City and country are required")
        return LocationDAO.create_location(data['city'], data['country'])
    
    @staticmethod
    def update_location(location_id, data):
        if not data.get('city') or not data.get('country'):
            raise ValueError("City and country are required")
        return LocationDAO.update_location(location_id, data['city'], data['country'])
    
    @staticmethod
    def delete_location(location_id):
        return LocationDAO.delete_location(location_id)