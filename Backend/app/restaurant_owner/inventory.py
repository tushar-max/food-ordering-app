from flask_jwt_extended import jwt_required
from flask_restful import Resource

from bl.owner.inventory import delete_data, get_inventory



class Inventory(Resource):
    @jwt_required()
    def get(self,email):
        return get_inventory(email=email)
    
    @jwt_required()
    def delete(self,email):
        result = delete_data(email)
        if result:
            return {'message': 'Book deleted successfully'}, 200
        else:
            return {'message': 'Some error occured'}, 500