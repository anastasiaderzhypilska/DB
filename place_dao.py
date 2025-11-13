from app.models import db, Place

class PlaceDAO:
    @staticmethod
    def get_all_places():
        return Place.query.all()
    
    @staticmethod
    def get_place_by_id(place_id):
        return Place.query.get(place_id)
    
    @staticmethod
    def create_place(name, description, category_id, location_id):
        place = Place(
            name=name, 
            description=description, 
            category_id=category_id, 
            location_id=location_id
        )
        db.session.add(place)
        db.session.commit()
        return place
    
    @staticmethod
    def update_place(place_id, name, description, category_id, location_id):
        place = Place.query.get(place_id)
        if place:
            place.name = name
            place.description = description
            place.category_id = category_id
            place.location_id = location_id
            db.session.commit()
        return place
    
    @staticmethod
    def delete_place(place_id):
        place = Place.query.get(place_id)
        if place:
            db.session.delete(place)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_place_owners(place_id):
        place = Place.query.get(place_id)
        return place.owners if place else []  
    
    @staticmethod
    def get_place_reviews(place_id):
        place = Place.query.get(place_id)
        return place.reviews if place else []