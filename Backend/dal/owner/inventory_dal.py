from .. import db
from dal.models.restaurant_owner import RestaurantOwner
from dal.models.restaurant import Restaurant
from dal.models.menu import Menu


def get_inventory_dal(email):
    owner = RestaurantOwner.query.filter_by(email=email).first()
    if not owner:
        return {'message': 'Restaurant owner not found'}, 404

    restaurant = Restaurant.query.filter_by(owner_id=owner.id).first()
    if not restaurant:
        return {'message': 'Restaurant not found'}, 404

    menu_items = Menu.query.filter_by(resid=restaurant.id).all()
    dishes = []
    for item in menu_items:
        dish = {
            "id": item.id,
            "resid": item.resid,
            "name": item.name,
            "price": item.price,
            "description": item.description,
            "restaurant_name": restaurant.name,
            "location": restaurant.location,
            "cusine": restaurant.cusine
        }
        dishes.append(dish)

    return dishes, 200


def delete_data_dal(id):
    try:
        id = int(id)
        dish = Menu.query.get(id)
        if not dish:
            return {'message': 'Dish not found'}, 404

        db.session.delete(dish)
        db.session.commit()
        return {'message': 'Dish deleted successfully'}, 200
    except Exception as e:
        print(e)
        return {'message': 'Error deleting dish'}, 500
