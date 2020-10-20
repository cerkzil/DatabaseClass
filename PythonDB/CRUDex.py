from database import DatabaseContextManager


# ------------------------Table Creation------------------------
def create_table_customers():
    query = """CREATE TABLE IF NOT EXISTS Customers(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    second_name TEXT,
    age INTEGER,
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES Companies(company_id))"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_table_companies():
    query = """CREATE TABLE IF NOT EXISTS Companies(
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    employee_count INTEGER)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


# ------------------------CRUD------------------------
def create_customers(first_name: str, second_name: str, age: int, company_id: int):
    query = """INSERT INTO Customers(first_name, second_name, age, company_id) VALUES(?,?,?,?)"""
    params = [first_name, second_name, age, company_id]
    with DatabaseContextManager("db") as db:
        db.execute(query, params)


def get_customers():
    query = """SELECT * FROM Customers"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
            print("------------------------------------------------------")


def update_customer(old_name, new_name):
    query = """UPDATE Customers
                SET first_name = ?
                WHERE first_name = ?"""
    params = [new_name, old_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, params)


def delete_customer(customer_id: int):
    query = """DELETE FROM Customers
                WHERE customer_id = ?"""
    params = [customer_id]
    with DatabaseContextManager("db") as db:
        db.execute(query, params)


def create_company(company_name: str, employee_count: int):
    query = """INSERT INTO Companies(company_name, employee_count) VALUES(?,?)"""
    params = [company_name, employee_count]
    with DatabaseContextManager("db") as db:
        db.execute(query, params)


def get_companies():
    query = """SELECT * FROM Companies"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
            print("------------------------------------------------------")


def update_company(old_employee_count: int, new_employee_count: int):
    query = """UPDATE Companies
                SET company_name = ?
                WHERE company_name = ?"""
    params = [new_employee_count, old_employee_count]
    with DatabaseContextManager("db") as db:
        db.execute(query, params)


def delete_company(company_id: int):
    query = """DELETE FROM Companies
                WHERE company_id = ?"""
    params = [company_id]
    with DatabaseContextManager("db") as db:
        db.execute(query, params)


def get_customers_employer(customer_id):
    query = """SELECT company_name 
    FROM Companies
    INNER JOIN Customers ON Customers.customer_id = Companies.company_id
    WHERE customer_id = ?
    """
    params = [customer_id]
    with DatabaseContextManager("db") as db:
        db.execute(query, params)
        for record in db.fetchall():
            print(record)
            print("------------------------------------------------------")


create_table_companies()
create_company("Alphabet", 3999)
create_company("Microsoft", 6500)
create_company("Valve", 10)
create_table_customers()
create_customers("Milly", "Tomson", 21, 1)
create_customers("Dylan", "Ether", 24, 2)
create_customers("Gabe", "Newell", 57, 3)
update_customer("Dylan", "Dylanson")
delete_customer(5)
delete_customer(7)
get_customers()
get_companies()
get_customers_employer(3)
