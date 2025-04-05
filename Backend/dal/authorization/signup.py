from .. import db
from dal.models.customer import Customer
from dal.models.restaurant_owner import RestaurantOwner
from dal.models.restaurant import Restaurant

def signup_dal(args):
    email = args.get('email')
    role = args.get('role')
    name = args.get('name')
    phone = args.get('phone')
    password = args.get('password')

    # Check if the email already exists in either table
    existing_customer = Customer.query.filter_by(email=email).first()
    existing_owner = RestaurantOwner.query.filter_by(email=email).first()

    if existing_customer or existing_owner:
        return {'message': 'Email already in use'}, 400

    if role == 'customer':
        # ✅ Create Customer object and add to DB
        new_customer = Customer(
            name=name,
            email=email,
            phone=phone,
            password=password,
            role=role
        )
        db.session.add(new_customer)

    elif role == 'restaurantowner':
        # ✅ Create RestaurantOwner object and add to DB
        new_owner = RestaurantOwner(
            name=name,
            email=email,
            phone=phone,
            password=password,
            role=role
        )
        db.session.add(new_owner)
        db.session.flush()  # Make sure new_owner.id is available

        # ✅ Create Restaurant object tied to this owner
        new_restaurant = Restaurant(
            name=args.get('restaurantname'),
            location=args.get('location'),
            cusine=args.get('cusine'),
            owner_id=new_owner.id
        )
        db.session.add(new_restaurant)

    else:
        return {'message': 'Invalid role'}, 400

    # ✅ Commit all changes
    db.session.commit()
    return {'message': 'User signed up successfully'}, 201