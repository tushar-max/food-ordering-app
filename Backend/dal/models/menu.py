from .. import db


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resid = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    description = db.Column(db.Text)

    restaurant = db.relationship('Restaurant', backref='menu_items')
