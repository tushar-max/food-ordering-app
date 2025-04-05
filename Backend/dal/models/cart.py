from .. import db



class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerid = db.Column(db.Integer, db.ForeignKey('customer.id'))
    dishid = db.Column(db.Integer, db.ForeignKey('menu.id'))
    dishtitle = db.Column(db.String(100))

    customer = db.relationship('Customer', backref='cart_items')
    dish = db.relationship('Menu', backref='cart_items')
