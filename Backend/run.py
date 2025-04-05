from app import create_app
from app.seed import seed_data
from dal import db

app = create_app()
db.init_app(app)


if __name__ == '__main__':
    # Activating the application context
    with app.app_context():
        # Creating all database tables
        db.create_all()
        seed_data()
    app.run(debug=True, port=5000)
