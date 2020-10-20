from database import DatabaseContextManager


# ------------------------Table Creation------------------------
def create_table_customers():
    query = """CREATE TABLE IF NOT EXISTS Customers(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    second_name TEXT,
    amount_spend INTEGER)"""
    with DatabaseContextManager("db2") as db:
        db.execute(query)


def create_table_products():
    query = """CREATE TABLE IF NOT EXISTS Products(
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price INTEGER,
    description TEXT)"""
    with DatabaseContextManager("db2") as db:
        db.execute(query)


def create_table_orders():
    query = """CREATE TABLE IF NOT EXISTS Orders(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    product_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id))"""
    with DatabaseContextManager("db2") as db:
        db.execute(query)


# ------------------------CRUD------------------------
# ----------------------Customers---------------------
def create_customers(first_name: str, second_name: str, amount_spend: int):
    query = """INSERT INTO Customers(first_name, second_name, amount_spend) VALUES(?,?,?)"""
    params = [first_name, second_name, amount_spend]
    with DatabaseContextManager("db2") as db:
        db.execute(query, params)


def get_customers():
    query = """SELECT * FROM Customers"""
    with DatabaseContextManager("db2") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
            print("------------------------------------------------------")


def update_customer(old_name, new_name):
    query = """UPDATE Customers
                SET first_name = ?
                WHERE first_name = ?"""
    params = [new_name, old_name]
    with DatabaseContextManager("db2") as db:
        db.execute(query, params)


def delete_customer(customer_id: int):
    query = """DELETE FROM Customers
                WHERE customer_id = ?"""
    params = [customer_id]
    with DatabaseContextManager("db2") as db:
        db.execute(query, params)


# ----------------------Products---------------------
def create_product(name: str, price: int, description: str):
    query = """INSERT INTO Products(name, price, description) VALUES(?,?,?)"""
    params = [name, price, description]
    with DatabaseContextManager("db2") as db:
        db.execute(query, params)


def get_products():
    query = """SELECT * FROM Products"""
    with DatabaseContextManager("db2") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
            print("------------------------------------------------------")


def update_product(old_name: str, new_name: str):
    query = """UPDATE Products
                SET name = ?
                WHERE name = ?"""
    params = [new_name, old_name]
    with DatabaseContextManager("db2") as db:
        db.execute(query, params)


def delete_product(product_id: int):
    query = """DELETE FROM Products
                WHERE product_id = ?"""
    params = [product_id]
    with DatabaseContextManager("db2") as db:
        db.execute(query, params)


# -----------------------Orders----------------------
def create_order(customer_id: int, product_id):
    query = """INSERT INTO Orders(customer_id, product_id) VALUES(?,?)"""
    params = [customer_id, product_id]
    with DatabaseContextManager("db2") as db:
        db.execute(query, params)


def get_orders():
    query = """SELECT * FROM Orders"""
    with DatabaseContextManager("db2") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
            print("------------------------------------------------------")


def update_order(old_product_id, new_product_id):
    query = """UPDATE Orders
                SET product_id = ?
                WHERE product_id = ?"""
    params = [new_product_id, old_product_id]
    with DatabaseContextManager("db2") as db:
        db.execute(query, params)


def delete_order(customer_id: int):
    query = """DELETE FROM Orders
                WHERE customer_id = ?"""
    params = [customer_id]
    with DatabaseContextManager("db2") as db:
        db.execute(query, params)


def get_full_order(order_id):
    query = """SELECT order_id, first_name, second_name amount_spend, name, price, description FROM Orders
    JOIN Customers
    ON Orders.customer_id = Customers.customer_id
    JOIN Products
    ON Orders.product_id = Products.product_id
    WHERE order_id=?"""
    params = [order_id]
    with DatabaseContextManager("db2") as db:
        db.execute(query, params)
        for record in db.fetchall():
            print(record)
            print("------------------------------------------------------")


create_table_customers()
create_customers("Milly", "Tomson", 221)
create_customers("Dylan", "Ether", 24)
create_customers("Gabe", "Newell", 570)

create_table_products()
create_product("Pc", 2000, "Gaming Pc")
create_product("Cat", 100, "Living cat")
create_product("Wheels", 20, "Wheels 4 u")

create_table_orders()

create_order(1, 2)
create_order(2, 3)
create_order(3, 1)


print("-----------------------Customers-------------------")
get_customers()
print("-----------------------Products--------------------")
get_products()
print("-----------------------Orders----------------------")
get_orders()
print("---------------------Full_Orders-------------------")
get_full_order(5)
