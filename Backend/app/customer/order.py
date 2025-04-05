from flask_jwt_extended import jwt_required
from flask_restful import Resource

from bl.customer.order import get_orders_bl

class Orders(Resource): 
    @jwt_required()
    def get(self,email):
        return get_orders_bl(email)