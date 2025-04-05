from .. import db


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    cusine = db.Column(db.String(100))
    owner_id = db.Column(db.Integer, db.ForeignKey('restaurant_owner.id'))

    owner = db.relationship('RestaurantOwner', backref='restaurants')
