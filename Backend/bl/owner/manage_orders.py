from flask_restful import reqparse

from dal.owner.manage_orders_dal import get_order_requests_dal, update_order_status_dal

def get_order_requests(email):
    try:
        return get_order_requests_dal(email)
    except Exception as e:
        print(e)
        return {'message': 'Some error occured'}, 500
    
    
def update_order_status(email):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True, help='Id is required')
    parser.add_argument('customerid', type=str, required=True, help='Customer email is required')
    parser.add_argument('dishid', type=str, required=True, help='Book Id is required')
    parser.add_argument('dishtitle', type=str, required=True, help='Book title is required')
    parser.add_argument('orderdate', type=str, required=True, help='Order date is required')
    parser.add_argument('orderstatus', type=str, required=True, help='Order status is required')
    args = parser.parse_args()
    print(args)
    try:
        return update_order_status_dal(args)
    except:
        return {'message': 'Some error occured'}, 500