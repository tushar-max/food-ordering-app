from .. import db


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    resid = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    dishid = db.Column(db.Integer, db.ForeignKey('menu.id'))
    rating = db.Column(db.Integer)
    review = db.Column(db.Text)

    restaurant = db.relationship('Restaurant', backref='reviews')
    dish = db.relationship('Menu', backref='reviews')
