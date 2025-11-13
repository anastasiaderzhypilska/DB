from app.models import db, Owner

class OwnerDAO:
    @staticmethod
    def get_all_owners():
        return Owner.query.all()
    
    @staticmethod
    def get_owner_by_id(owner_id):
        return Owner.query.get(owner_id)
    
    @staticmethod
    def create_owner(full_name, contact_email):
        owner = Owner(full_name=full_name, contact_email=contact_email)
        db.session.add(owner)
        db.session.commit()
        return owner
    
    @staticmethod
    def update_owner(owner_id, full_name, contact_email):
        owner = Owner.query.get(owner_id)
        if owner:
            owner.full_name = full_name
            owner.contact_email = contact_email
            db.session.commit()
        return owner
    
    @staticmethod
    def delete_owner(owner_id):
        owner = Owner.query.get(owner_id)
        if owner:
            db.session.delete(owner)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def get_owner_places(owner_id):
        owner = Owner.query.get(owner_id)
        return owner.places if owner else []  