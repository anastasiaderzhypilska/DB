from app.models import db, Location

class LocationDAO:
    @staticmethod
    def get_all_locations():
        return Location.query.all()
    
    @staticmethod
    def get_location_by_id(location_id):
        return Location.query.get(location_id)
    
    @staticmethod
    def create_location(city, country):
        location = Location(city=city, country=country)
        db.session.add(location)
        db.session.commit()
        return location
    
    @staticmethod
    def update_location(location_id, city, country):
        location = Location.query.get(location_id)
        if location:
            location.city = city
            location.country = country
            db.session.commit()
        return location
    
    @staticmethod
    def delete_location(location_id):
        location = Location.query.get(location_id)
        if location:
            db.session.delete(location)
            db.session.commit()
            return True
        return False