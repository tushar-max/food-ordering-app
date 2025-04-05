from flask_restful import reqparse

from dal.owner.dish_dal import add_data_dal, get_data_dal, update_data_dal


def get_data():
    return get_data_dal()


def add_data():
    parser = reqparse.RequestParser()
    parser.add_argument('storeid', type=str, required=True,
                        help='Restaurant id is required')
    parser.add_argument('name', type=str, required=True,
                        help='Name is required')
    parser.add_argument('price', type=int, required=True,
                        help='Price is required')
    parser.add_argument('description', type=str,
                        required=True, help='Description is required')
    args = parser.parse_args()
    # print(args)
    return add_data_dal(args)


def update_data():
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True,
                        help='Title is required')
    # parser.add_argument('resid', type=str, required=True, help='Restaurant id is required')
    parser.add_argument('name', type=str, required=True,
                        help='Name is required')
    parser.add_argument('price', type=int, required=True,
                        help='Price is required')
    parser.add_argument('description', type=str,
                        required=True, help='Description is required')
    args = parser.parse_args()
    return update_data_dal(args)
