from app.dao.user_dao import UserDAO

class UserService:
    @staticmethod
    def get_all_users():
        return UserDAO.get_all_users()
    
    @staticmethod
    def get_user_by_id(user_id):
        return UserDAO.get_user_by_id(user_id)
    
    @staticmethod
    def create_user(data):
        if not data.get('username') or not data.get('email'):
            raise ValueError("Username and email are required")
        return UserDAO.create_user(data['username'], data['email'])
    
    @staticmethod
    def update_user(user_id, data):
        if not data.get('username') or not data.get('email'):
            raise ValueError("Username and email are required")
        return UserDAO.update_user(user_id, data['username'], data['email'])
    
    @staticmethod
    def delete_user(user_id):
        return UserDAO.delete_user(user_id)