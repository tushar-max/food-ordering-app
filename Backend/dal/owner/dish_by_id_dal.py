from .. import db
from dal.models.menu import Menu


def get_dish_by_id_dal(dish_id):
    dish = Menu.query.get(dish_id)

    if not dish:
        return {'message': 'Dish not found'}, 404

    restaurant = dish.restaurant
    res = {
        "id": dish.id,
        "resid": dish.resid,
        "name": dish.name,
        "price": dish.price,
        "description": dish.description,
        "restaurant_name": restaurant.name,
        "location": restaurant.location,
        "cusine": restaurant.cusine
    }
    return res, 200



# Delete


def delete_data_dal(dish_id):
    dish = Menu.query.get(dish_id)

    if not dish:
        return {'message': 'Dish not found'}, 404

    db.session.delete(dish)
    db.session.commit()
    return {'message': 'Dish deleted successfully'}, 200
