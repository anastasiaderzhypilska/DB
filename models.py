from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


place_owners = db.Table('Place_Owners',
    db.Column('place_owner_id', db.Integer, primary_key=True),
    db.Column('place_id', db.Integer, db.ForeignKey('Places.place_id')),
    db.Column('owner_id', db.Integer, db.ForeignKey('Owners.owner_id'))
)

class Owner(db.Model):
    __tablename__ = 'Owners'
    
    owner_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    contact_email = db.Column(db.String(100), nullable=False)
    

    places = db.relationship('Place', 
                        secondary=place_owners,
                        backref='owners')
    
    def to_dict(self):
        return {
            'owner_id': self.owner_id,
            'full_name': self.full_name,
            'contact_email': self.contact_email
        }

class Place(db.Model):
    __tablename__ = 'Places'
    
    place_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    category_id = db.Column(db.Integer)
    location_id = db.Column(db.Integer)
    

    reviews = db.relationship('Review', backref='place')
    
    def to_dict(self):
        return {
            'place_id': self.place_id,
            'name': self.name,
            'description': self.description,
            'category_id': self.category_id,
            'location_id': self.location_id
        }

class Review(db.Model):
    __tablename__ = 'Reviews'
    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    place_id = db.Column(db.Integer, db.ForeignKey('Places.place_id'))
    review_text = db.Column(db.Text)
    review_date = db.Column(db.Date)
    
    def to_dict(self):
        return {
            'review_id': self.review_id,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'review_text': self.review_text,
            'review_date': self.review_date.isoformat() if self.review_date else None
        }


class Category(db.Model):
    __tablename__ = 'Categories'
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    
    def to_dict(self):
        return {
            'category_id': self.category_id,
            'name': self.name
        }

class Location(db.Model):
    __tablename__ = 'Locations'
    location_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    
    def to_dict(self):
        return {
            'location_id': self.location_id,
            'city': self.city,
            'country': self.country
        }

class Rating(db.Model):
    __tablename__ = 'Ratings'
    rating_id = db.Column(db.Integer, primary_key=True)
    rating_name = db.Column(db.String(50), nullable=False)
    
    def to_dict(self):
        return {
            'rating_id': self.rating_id,
            'rating_name': self.rating_name
        }

class Photo(db.Model):
    __tablename__ = 'Photos'
    photo_id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer)
    photo_url = db.Column(db.String(255), nullable=False)
    upload_date = db.Column(db.Date)
    
    def to_dict(self):
        return {
            'photo_id': self.photo_id,
            'place_id': self.place_id,
            'photo_url': self.photo_url,
            'upload_date': self.upload_date.isoformat() if self.upload_date else None
        }

class User(db.Model):
    __tablename__ = 'Users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email
        }