from .. import db
from dal.models.restaurant_owner import RestaurantOwner
from dal.models.restaurant import Restaurant
from dal.models.menu import Menu


# --- DAL Functions ---

def get_data_dal():
    try:
        dishes = []
        menu_items = Menu.query.all()
        for item in menu_items:
            restaurant = item.restaurant
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
    except Exception as e:
        return {"message": "Error fetching data", "error": str(e)}, 500


def add_data_dal(args):
    try:
        owner = RestaurantOwner.query.filter_by(email=args['storeid']).first()
        if not owner:
            return {'message': 'Restaurant owner not found'}, 404

        restaurant = Restaurant.query.filter_by(owner_id=owner.id).first()
        if not restaurant:
            return {'message': 'Restaurant not found'}, 404

        new_dish = Menu(
            resid=restaurant.id,
            name=args['name'],
            price=args['price'],
            description=args['description']
        )
        db.session.add(new_dish)
        db.session.commit()
        return {'message': 'Dish added successfully'}, 201
    except Exception as e:
        db.session.rollback()
        return {'message': 'Error adding dish', 'error': str(e)}, 500


def update_data_dal(args):
    dish_id = args['id']
    try:
        dish = Menu.query.get(dish_id)
        if not dish:
            return {'message': 'Dish not found'}, 404

        # Dynamically update fields
        if 'name' in args and args['name'] is not None:
            dish.name = args['name']
        if 'price' in args and args['price'] is not None:
            dish.price = args['price']
        if 'description' in args and args['description'] is not None:
            dish.description = args['description']

        db.session.commit()
        return {'message': 'Dish updated successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'message': 'Error updating dish', 'error': str(e)}, 500
