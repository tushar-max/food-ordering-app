from flask_jwt_extended import jwt_required
from flask_restful import Resource

from bl.owner.dish import add_data, get_data, update_data


class DishAPI(Resource):
    def get(self):
        data, status = get_data()
        return data, status
    
    @jwt_required()
    def post(self):
        result = add_data()
        return result

    @jwt_required()
    def put(self):
        result = update_data()
        if result:
            return {'message': 'Dish updated successfully'}, 200
        else:
            return {'message': 'Some error occured'}, 500