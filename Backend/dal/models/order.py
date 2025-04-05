from .. import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerid = db.Column(db.Integer, db.ForeignKey('customer.id'))
    resid = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    dishid = db.Column(db.Integer, db.ForeignKey('menu.id'))
    dishtitle = db.Column(db.String(100))
    orderdate = db.Column(db.String(100))  # or db.DateTime if you prefer
    orderstatus = db.Column(db.String(50))

    customer = db.relationship('Customer', backref='orders')
    restaurant = db.relationship('Restaurant', backref='orders')
    dish = db.relationship('Menu', backref='orders')
