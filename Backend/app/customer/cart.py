from flask_jwt_extended import jwt_required
from flask_restful import Resource

from bl.customer.cart import add_to_cart_bl, get_cart_items_bl, remove_from_cart_bl

class Cart(Resource): 
    @jwt_required()
    def get(self,email):
        return get_cart_items_bl(email)
        
    @jwt_required()
    def post(self,email):
        return add_to_cart_bl(email)
    
    @jwt_required()
    def put(self,email):
        return remove_from_cart_bl(email)
        