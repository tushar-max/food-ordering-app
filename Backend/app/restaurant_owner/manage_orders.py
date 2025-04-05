from flask_jwt_extended import jwt_required
from flask_restful import Resource

from bl.owner.manage_orders import get_order_requests, update_order_status

class ManageOrders(Resource): 
    @jwt_required()
    def get(self,email):
        return get_order_requests(email)
        
    # @jwt_required()
    def put(self,email):
        return update_order_status(email)