from app.dao.category_dao import CategoryDAO

class CategoryService:
    @staticmethod
    def get_all_categories():
        return CategoryDAO.get_all_categories()
    
    @staticmethod
    def get_category_by_id(category_id):
        return CategoryDAO.get_category_by_id(category_id)
    
    @staticmethod
    def create_category(data):
        if not data.get('name'):
            raise ValueError("Category name is required")
        return CategoryDAO.create_category(data['name'])
    
    @staticmethod
    def update_category(category_id, data):
        if not data.get('name'):
            raise ValueError("Category name is required")
        return CategoryDAO.update_category(category_id, data['name'])
    
    @staticmethod
    def delete_category(category_id):
        return CategoryDAO.delete_category(category_id)