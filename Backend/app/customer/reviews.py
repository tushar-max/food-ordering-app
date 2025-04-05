from flask_jwt_extended import jwt_required
from flask_restful import Resource

from bl.customer.reviews import get_reviews_bl, post_review_bl

class Reviews(Resource):
    def get(self, dishid):
        return get_reviews_bl(dishid)
    
    @jwt_required()
    def post(self,dishid):
        return post_review_bl()