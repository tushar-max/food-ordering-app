# 🍽️ Food Ordering Application

## 📖 Description

This is a full-stack **Food Ordering Application** designed for customers and restaurant owners to interact through a seamless online food platform. It is built with **Angular** (frontend) and **Flask** (backend), with **SQLite** as the database and **JWT** for authentication.

Users can browse restaurants, view menus, place orders, and track them. Restaurant owners can manage their menus and process orders. The application is designed with a clean architecture and responsive UI to deliver an optimal user experience.

---

## 🛠️ Tech Stack

- **Frontend:** Angular  
- **Backend:** Flask  
- **Database:** SQLite  
- **ORM:** SQLAlchemy  
- **Authentication:** JWT  
- **Tools Used:** VS Code / PyCharm, Git, SQLite Browser

---

## 🚀 Setup Instructions

1. **Clone or Download the Repository**  
   Unzip the folder if downloaded as a ZIP.

2. **Backend Setup (Flask)**  
   - Navigate to the `backend/` directory  
   - Install dependencies:  
     ```bash
     pip install -r requirements.txt
     ```
   - Run the backend:  
     ```bash
     python run.py
     ```

3. **Frontend Setup (Angular)**  
   - Navigate to the `frontend/` directory  
   - Start the Angular app:  
     ```bash
     ng serve -o
     ```

4. **Access the App**  
   The application will run at:  
   ```
   http://localhost:4200
   ```

---

## 👥 User Roles

### 🧑‍🍳 Restaurant Owner
- Register and manage their restaurant
- Add, edit, and delete menu items
- Manage customer orders
- View and respond to customer reviews (optional)

### 👨‍🍽️ Customer
- Browse restaurants by location, cuisine, or name
- View menus and dish details
- Add items to cart and place orders
- Track order status and view order history (optional)

---

## 📋 Core Features

- 🔍 Search/filter restaurants by location, cuisine, or name
- 🧾 View restaurant menu with dish descriptions and prices
- 🛒 Add items to cart and place orders
- 📦 Track order status (Placed, Preparing, Ready, Delivered)
- 🏪 Restaurant registration and menu management
- ⭐ Ratings and Reviews (Bonus)
- 🔐 Role-based authorization using JWT
- 📄 Clean code architecture and error handling
- 📱 Responsive and user-friendly UI

---

## ⚠️ Notes

- Signup is **not required**; predefined users may be used.
- Form validations and exception handling are implemented.
- Access control based on user role is enforced.
- Followed Clean Architecture for backend services.

---

## 📬 Contact

For any questions or contributions, feel free to open an issue or contact the maintainer.


