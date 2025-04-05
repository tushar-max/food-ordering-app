from flask_restful import Resource

from bl.owner.dish_by_id import delete_data, get_dish_by_id


class IDBookAPI(Resource):
    def get(self,dishid):
        return get_dish_by_id(dishid)

    def delete(self,dishid):
        result = delete_data(dishid)
        if result:
            return {'message': 'Book deleted successfully'}, 200
        else:
            return {'message': 'Some error occured'}, 500