from dal import db
from dal.models.admin import Admin

from dal.models.customer import Customer
from dal.models.menu import Menu
from dal.models.restaurant import Restaurant
from dal.models.restaurant_owner import RestaurantOwner


def seed_data():
    # Seed only if DB is empty
    if not Customer.query.first():
        print("🌱 Seeding initial data...")

        cust = Customer(name="Tushar", email="tushar@example.com", phone="1234567890", password="hashed_pw", role="customer")
        owner = RestaurantOwner(name="Rohit", email="rohit@res.com", phone="1112223333", password="hashed_pw", role="owner")
        res = Restaurant(name="Spicy Bite", location="Delhi", cusine="Indian", owner=owner)
        dish = Menu(resid=1, name="Paneer Butter Masala", price=250, description="Delicious")

        admin = Admin(name="Super Admin", email="admin@site.com", password="admin123", role="admin")

        db.session.add_all([cust, owner, res, dish, admin])
        db.session.commit()
        print("✅ Seeding done!")
    else:
        print("✅ Data already exists. Skipping seeding.")

