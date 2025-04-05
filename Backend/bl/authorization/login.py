from flask_restful import reqparse

from dal.authorization.login import login_dal

def login_bl():
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True,
                        help='email is required')
    parser.add_argument('password', type=str,
                        required=True, help='Password is required')
    parser.add_argument('role', type=str, required=True,
                        help='Role is required')
    args = parser.parse_args()
    # print(args)
    return login_dal(args)