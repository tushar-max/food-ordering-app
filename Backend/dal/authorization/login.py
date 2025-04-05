from datetime import timedelta
from flask_jwt_extended import create_access_token
from dal.models.customer import Customer
from dal.models.restaurant_owner import RestaurantOwner

def login_dal(args):
    role = args.get('role')
    email = args.get('email')
    password = args.get('password')

    if not all([role, email, password]):
        return {'message': 'Missing credentials'}, 400

    user = None

    if role == 'customer':
        user = Customer.query.filter_by(email=email, password=password).first()
    elif role == 'restaurantowner':
        user = RestaurantOwner.query.filter_by(email=email, password=password).first()
    else:
        return {'message': 'Invalid role'}, 400

    if user:
        access_token = create_access_token(
            identity=user.email,
            additional_claims={
                'role': user.role,
                'phone': user.phone
            },
            expires_delta=timedelta(days=1)
        )
        return {'access_token': access_token}, 200
    else:
        return {'message': 'Invalid credentials'}, 401
