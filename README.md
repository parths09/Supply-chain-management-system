# 📦 Supply Chain Management System (DBMS Project)

A database-driven Supply Chain Management System designed to streamline procurement, inventory tracking, order processing, and logistics using PostgreSQL and Django ORM. This project demonstrates real-world automation using database triggers, views, and normalized schema design.

---

## 🚀 Features

- **Inventory Automation**: Automatically updates stock levels upon procurement delivery.
- **Order Fulfillment Tracking**: Tracks order status and shipment progress dynamically.
- **Role-Based Notifications**: Sends alerts to customers, suppliers, and managers via trigger-based notifications.
- **Views for Reporting**: Simplified data access with views for customer orders and role-specific notifications.
- **Django Admin Integration**: Manage and view models via Django’s powerful admin interface.
- **Simulation**: Simulate the process flow. The date increases and the shipments reach their destinations through optimized path.

---

## 🛠️ Technologies Used

| Technology     | Role                                      |
|----------------|-------------------------------------------|
| PostgreSQL     | Primary relational database with triggers |
| Django ORM     | Backend model handling and schema mapping |
| Python         | Business logic and scripting              |
| PL/pgSQL       | Queries,trigger functions and contraints  |
| HTML/CSS       | Django Admin Interface for UI             |

---

## 🏗️ Database Schema Highlights 

- **Products, Suppliers, Warehouses**: Core entities representing inventory sources.
- **Inventory**: Tracks stock levels by product-supplier-warehouse combination.
- **Procurements & Orders**: Handles incoming and outgoing stock.
- **Shippings & ShippingDetails**: Tracks item delivery across warehouses.
- **Notifications**: Stores messages for stakeholders triggered by system events.
- and much more..

---

## 🖥️ Getting Started

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/parths09/Supply-chain-management-system.git
   cd Supply-chain-management-system/SCM_webapp
   
2. **Set Up Virtual Environment**
    ```bash
    `python -m venv env source env/bin/activate  # or env\Scripts\activate on Windows pip install -r requirements.txt`
    
3. **Configure PostgreSQL**
    -   Set up your DB user and database.
    -   Update `settings.py` with your DB credentials.
        
4. **Run Migrations and Server**
    ```bash
    `python manage.py makemigrations python manage.py migrate python manage.py runserver`
  
  
