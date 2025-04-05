from flask_jwt_extended import jwt_required
from flask_restful import Resource

from bl.customer.buydish import place_order_bl

class BuyDish(Resource): 
    @jwt_required()
    def post(self):
        return place_order_bl()