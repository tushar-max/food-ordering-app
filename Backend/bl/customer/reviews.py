from flask_restful import reqparse

from dal.customer.reviews import get_reviews_dal, post_review_dal


def get_reviews_bl(dishid):
    return get_reviews_dal(dishid)


def post_review_bl():
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help='Email is required')
    parser.add_argument('resid', type=str, required=True, help='Book Id is required')
    parser.add_argument('dishid', type=str, required=True, help='Book Id is required')
    parser.add_argument('rating', type=int, required=True, help='Rating is required')
    parser.add_argument('review', type=str, required=True, help='Review is required')
    args = parser.parse_args()
    # print(args)
    try:
        return post_review_dal(args)
    except:
        return {'message': 'Some error occured'}, 500