from .. import db
from dal.models.order import Order


# DAL function to get orders for a customer
def get_orders_dal(email):
    try:
        orders = Order.query.filter_by(customerid=email).all()
        result = [
            {
                "id": order.id,
                "customerid": order.customerid,
                "resid": order.resid,
                "dishid": order.dishid,
                "dishtitle": order.dishtitle,
                "orderdate": order.orderdate,
                "orderstatus": order.orderstatus
            }
            for order in orders
        ]
        return result, 200
    except Exception as e:
        return {'message': 'Error fetching orders', 'error': str(e)}, 500
