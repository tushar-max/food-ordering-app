from .. import db
from dal.models.order import Order

def place_order_dal(args):
    # Create an Order object using ORM
    new_order = Order(
        customerid=args['customerid'],
        resid=args['resid'],
        dishid=args['dishid'],
        dishtitle=args['dishtitle'],
        orderdate=args['orderdate'],
        orderstatus=args['orderstatus']
    )

    # Add and commit using SQLAlchemy session
    db.session.add(new_order)
    db.session.commit()

    return {'message': 'Order Placed successfully'}, 201
