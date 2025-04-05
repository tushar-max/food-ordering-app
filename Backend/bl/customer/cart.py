from flask_restful import reqparse

from dal.customer.cart import add_to_cart_dal, get_cart_items_dal, remove_from_cart_dal


def get_cart_items_bl(email):
    try:
        return get_cart_items_dal(email)
    except Exception as e:
        print(e)
        return {'message': 'Some error occured'}, 500
    
    
def add_to_cart_bl(email):
    parser = reqparse.RequestParser()
    parser.add_argument('customerid', type=str, required=True, help='Email is required')
    parser.add_argument('dishid', type=int, required=True, help='Book Id is required')
    parser.add_argument('dishtitle', type=str, required=True, help='Book Title is required')
    args = parser.parse_args()
    print(args)
    try:
        return add_to_cart_dal(args)
    except:
        return {'message': 'Some error occured'}, 500
    
def remove_from_cart_bl(email):
    parser = reqparse.RequestParser()
    parser.add_argument('cartid', type=str, required=True, help='Cart Id is required')
    args = parser.parse_args()
    print(args)
    try:
        return remove_from_cart_dal(args)
    except:
        return {'message': 'Some error occured'}, 500