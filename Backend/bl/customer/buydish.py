from flask_restful import reqparse

from dal.customer.buydish import place_order_dal

def place_order_bl():
    parser = reqparse.RequestParser()
    parser.add_argument('customerid', type=str, required=True, help='Customer email is required')
    parser.add_argument('resid', type=str, required=True, help='Restaurant Id is required')
    parser.add_argument('dishid', type=str, required=True, help='Book Id is required')
    parser.add_argument('dishtitle', type=str, required=True, help='Book title is required')
    parser.add_argument('orderdate', type=str, required=True, help='Order date is required')
    parser.add_argument('orderstatus', type=str, required=True, help='Order status is required')
    args = parser.parse_args()
    try:
        return place_order_dal(args)
    except Exception as e:
        return {'message': 'Some error occured'}, 500