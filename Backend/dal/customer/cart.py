from .. import db
from dal.models.cart import Cart


# Get all cart items for a customer
def get_cart_items_dal(email):
    try:
        carts = Cart.query.filter_by(customerid=email).all()
        result = [
            {
                "id": cart.id,
                "customerid": cart.customerid,
                "dishid": cart.dishid,
                "dishtitle": cart.dishtitle
            }
            for cart in carts
        ]
        return result, 200
    except Exception as e:
        return {"message": "Error fetching cart items", "error": str(e)}, 500


# Add an item to cart
def add_to_cart_dal(args):
    try:
        cart_item = Cart(
            customerid=args['customerid'],
            dishid=args['dishid'],
            dishtitle=args['dishtitle']
        )
        db.session.add(cart_item)
        db.session.commit()
        return {'message': 'Added to cart successfully'}, 201
    except Exception as e:
        db.session.rollback()
        return {'message': 'Error adding to cart', 'error': str(e)}, 500


# Remove an item from cart by ID
def remove_from_cart_dal(args):
    try:
        cart_item = Cart.query.get(args['cartid'])
        if cart_item:
            db.session.delete(cart_item)
            db.session.commit()
            return {'message': 'Removed from cart successfully'}, 201
        else:
            return {'message': 'Cart item not found'}, 404
    except Exception as e:
        db.session.rollback()
        return {'message': 'Error removing from cart', 'error': str(e)}, 500
