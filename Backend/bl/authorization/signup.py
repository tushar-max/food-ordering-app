from flask_restful import reqparse

from dal.authorization.signup import signup_dal

def signup_bl():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True,
                        help='Username is required')
    parser.add_argument('email', type=str, required=True,
                        help='Username is required')
    parser.add_argument('phone', type=int, required=True,
                        help='Username is required')
    parser.add_argument('password', type=str,
                        required=True, help='Password is required')
    parser.add_argument('role', type=str, required=True,
                        help='Role is required')
    parser.add_argument('location', type=str)
    parser.add_argument('cusine', type=str)
    parser.add_argument('restaurantname', type=str)
    args = parser.parse_args()
    try:
        return signup_dal(args)
    except Exception as e:
        print(e)
        return {'message': 'Some error occured'}, 500
