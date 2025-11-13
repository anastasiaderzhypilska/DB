from app.dao.owner_dao import OwnerDAO

class OwnerService:
    @staticmethod
    def get_all_owners():
        return OwnerDAO.get_all_owners()
    
    @staticmethod
    def get_owner_by_id(owner_id):
        return OwnerDAO.get_owner_by_id(owner_id)
    
    @staticmethod
    def create_owner(data):
        if not data.get('full_name') or not data.get('contact_email'):
            raise ValueError("Full name and contact email are required")
        return OwnerDAO.create_owner(data['full_name'], data['contact_email'])
    
    @staticmethod
    def update_owner(owner_id, data):
        if not data.get('full_name') or not data.get('contact_email'):
            raise ValueError("Full name and contact email are required")
        return OwnerDAO.update_owner(owner_id, data['full_name'], data['contact_email'])
    
    @staticmethod
    def delete_owner(owner_id):
        return OwnerDAO.delete_owner(owner_id)
    
    @staticmethod
    def get_owner_places(owner_id):
        return OwnerDAO.get_owner_places(owner_id)