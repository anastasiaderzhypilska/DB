from app.models import db, Category

class CategoryDAO:
    @staticmethod
    def get_all_categories():
        return Category.query.all()
    
    @staticmethod
    def get_category_by_id(category_id):
        return Category.query.get(category_id)
    
    @staticmethod
    def create_category(name):
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        return category
    
    @staticmethod
    def update_category(category_id, name):
        category = Category.query.get(category_id)
        if category:
            category.name = name
            db.session.commit()
        return category
    
    @staticmethod
    def delete_category(category_id):
        category = Category.query.get(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()
            return True
        return False