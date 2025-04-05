from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_cors import CORS


def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['DATABASE'] = 'database.db'
    app.config['JWT_SECRET_KEY'] = 'custom_secret_key_for_jwt'
    jwt = JWTManager(app)
    CORS(app)

    from .restaurant_owner.dishes import DishAPI
    from .restaurant_owner.dish_by_id import IDBookAPI
    from .restaurant_owner.inventory import Inventory
    from .authorization.signup import SignUp
    from .authorization.auth import Authorization
    from .customer.reviews import Reviews
    from .customer.buydish import BuyDish
    from .customer.order import Orders
    from .customer.cart import Cart
    from .restaurant_owner.manage_orders import ManageOrders
    # CreateDb.create_table(app)

    api = Api(app)
    api.add_resource(DishAPI, '/dishes')
    api.add_resource(IDBookAPI,'/dishes/<int:dishid>')
    api.add_resource(SignUp,'/signup')
    api.add_resource(Authorization,'/login')
    api.add_resource(Reviews,'/reviews/<int:dishid>')
    api.add_resource(BuyDish,'/buydish')
    api.add_resource(Orders,'/orders/<string:email>')
    api.add_resource(Cart,'/cart/<string:email>')
    api.add_resource(Inventory,'/inventory/<string:email>')
    api.add_resource(ManageOrders,'/manageOrders/<string:email>')
    return app
