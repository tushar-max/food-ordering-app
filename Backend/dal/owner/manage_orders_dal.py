from .. import db
from dal.models.restaurant_owner import RestaurantOwner
from dal.models.restaurant import Restaurant
from dal.models.menu import Menu
from dal.models.order import Order


def get_order_requests_dal(email):
    try:
        owner = RestaurantOwner.query.filter_by(email=email).first()
        if not owner:
            return [], 200

        restaurants = Restaurant.query.filter_by(owner_id=owner.id).all()
        restaurant_ids = [r.id for r in restaurants]

        menu_items = Menu.query.filter(Menu.resid.in_(restaurant_ids)).all()
        dish_ids = [dish.id for dish in menu_items]

        orders = Order.query.filter(Order.dishid.in_(dish_ids)).all()

        result = []
        for o in orders:
            order = {
                "id": o.id,
                "customerid": o.customerid,
                "resid": o.resid,
                "dishid": o.dishid,
                "dishtitle": o.dishtitle,
                "orderdate": o.orderdate,
                "orderstatus": o.orderstatus
            }
            result.append(order)

        return result, 200
    except Exception as e:
        return {"message": "Failed to fetch order requests", "error": str(e)}, 500


def update_order_status_dal(args):
    try:
        order = Order.query.get(args['id'])
        if not order:
            return {'message': 'Order not found'}, 404

        for key, value in args.items():
            if hasattr(order, key) and value is not None:
                setattr(order, key, value)

        db.session.commit()
        return {'message': 'Order updated successfully'}, 200
    except Exception as e:
        print(e)
        return {'message': 'Failed to update order'}, 500
