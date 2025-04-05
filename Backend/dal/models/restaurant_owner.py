from .. import db


class RestaurantOwner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(15))
    password = db.Column(db.String(128))
    role = db.Column(db.String(50))
