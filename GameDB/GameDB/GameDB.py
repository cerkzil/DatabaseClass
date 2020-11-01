import sqlite3


# -------------------Context Manager-------------------
class DatabaseContextManager(object):

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


# ------------------------Table Creation------------------------
def create_table_studios():
    query = """CREATE TABLE IF NOT EXISTS Studios(
    studio_id INTEGER PRIMARY KEY AUTOINCREMENT,
    studio_name TEXT,
    employee_count INTEGER)"""
    with DatabaseContextManager("Db.db") as db:
        db.execute(query)


def create_table_publishers():
    query = """CREATE TABLE IF NOT EXISTS Publishers(
    publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    publisher_name TEXT,
    games_published INTEGER)"""
    with DatabaseContextManager("Db.db") as db:
        db.execute(query)


def create_table_games():
    query = """CREATE TABLE IF NOT EXISTS Games(
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    publisher_id INTEGER,
    studio_id INTEGER,
    game_name TEXT,
    genre TEXT,
    FOREIGN KEY (publisher_id) REFERENCES Publishers(publisher_id),
    FOREIGN KEY (studio_id) REFERENCES Studios(studio_id))"""
    with DatabaseContextManager("Db.db") as db:
        db.execute(query)


def create_table_wallets():
    query = """CREATE TABLE IF NOT EXISTS Wallets(
    wallet_id INTEGER PRIMARY KEY AUTOINCREMENT,
    payment_method TEXT,
    balance INTEGER)"""
    with DatabaseContextManager("Db.db") as db:
        db.execute(query)


def create_table_users():
    query = """CREATE TABLE IF NOT EXISTS Users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    wallet_id INTEGER,
    user_name TEXT,
    user_level INTEGER,
    games_owned INTEGER,
    FOREIGN KEY (wallet_id) REFERENCES Wallets(wallet_id))"""
    with DatabaseContextManager("Db.db") as db:
        db.execute(query)


def create_table_orders():
    query = """CREATE TABLE IF NOT EXISTS Orders(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    game_id INTEGER,
    user_id INTEGER,
    discount BOOLEAN,
    price INTEGER,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (game_id) REFERENCES Games(game_id))"""
    with DatabaseContextManager("Db.db") as db:
        db.execute(query)


# ------------------------CRUD------------------------
# -----------------------Studios----------------------
def create_studio(studio_name: str, employee_count: int):
    query = """INSERT INTO Studios(studio_name, employee_count) VALUES(?,?)"""
    params = [studio_name, employee_count]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)


def get_studios():
    query = """SELECT * FROM Studios"""
    with DatabaseContextManager("Db.db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
            print("------------------------------------------------------")


def update_studio(old_employee_count, new_employee_count):
    query = """UPDATE Studios
                SET employee_count = ?
                WHERE employee_count = ?"""
    params = [new_employee_count, old_employee_count]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)


def delete_studio(studio_id: int):
    query = """DELETE FROM Studios
                WHERE studio_id = ?"""
    params = [studio_id]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)


# ---------------------Publishers---------------------
def create_publisher(publisher_name: str, games_published: int):
    query = """INSERT INTO Publishers(publisher_name, games_published) VALUES(?,?)"""
    params = [publisher_name, games_published]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)


def get_publishers():
    query = """SELECT * FROM Publishers"""
    with DatabaseContextManager("Db.db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
            print("------------------------------------------------------")


def update_publisher(old_games_published, new_games_published):
    query = """UPDATE Publishers
                SET games_published = ?
                WHERE games_published = ?"""
    params = [new_games_published, old_games_published]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)


def delete_publisher(publisher_id: int):
    query = """DELETE FROM Publishers
                WHERE publisher_id = ?"""
    params = [publisher_id]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)


# -----------------------Games-----------------------
def create_game(publisher_id: int, studio_id: int, game_name: str, genre: str):
    query = """INSERT INTO Games(publisher_id, studio_id, game_name, genre) VALUES(?,?,?,?)"""
    params = [publisher_id, studio_id, game_name, genre]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)


def get_games():
    query = """SELECT * FROM Games"""
    with DatabaseContextManager("Db.db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
            print("------------------------------------------------------")


def update_game(old_game_name, new_game_name):
    query = """UPDATE Games
                SET game_name = ?
                WHERE game_name = ?"""
    params = [new_game_name, old_game_name]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)


def delete_game(game_id: int):
    query = """DELETE FROM Games
                WHERE game_id = ?"""
    params = [game_id]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)


def get_full_games(game_id):
    query = """SELECT game_id, game_name, genre, studio_name, employee_count, publisher_name, games_published FROM Games
    JOIN Publishers
    ON Games.publisher_id = Publishers.publisher_id
    JOIN Studios
    ON Games.studio_id = Studios.studio_id
    WHERE game_id=?"""
    params = [game_id]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)
        for record in db.fetchall():
            print(record)
            print("------------------------------------------------------")


# -----------------------Wallets----------------------
def create_wallet(payment_method: str, balance: int):
    query = """INSERT INTO Wallets(payment_method, balance) VALUES(?,?)"""
    params = [payment_method, balance]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)


def get_wallets():
    query = """SELECT * FROM Wallets"""
    with DatabaseContextManager("Db.db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
            print("------------------------------------------------------")


def update_wallet(old_balance, new_balance):
    query = """UPDATE Wallets
                SET balance = ?
                WHERE balance = ?"""
    params = [new_balance, old_balance]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)


def delete_wallet(wallet_id: int):
    query = """DELETE FROM Wallets
                WHERE wallet_id = ?"""
    params = [wallet_id]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)

# -----------------------Users-----------------------
def create_user(wallet_id: int, user_name: str, user_level: int, games_owned: int):
    query = """INSERT INTO Users(wallet_id, user_name, user_level, games_owned) VALUES(?,?,?,?)"""
    params = [wallet_id, user_name, user_level, games_owned]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)


def get_users():
    query = """SELECT * FROM Users"""
    with DatabaseContextManager("Db.db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
            print("------------------------------------------------------")


def update_user(old_user_level, new_user_level):
    query = """UPDATE Users
                SET user_level = ?
                WHERE user_level = ?"""
    params = [new_user_level, old_user_level]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)


def delete_user(user_id: int):
    query = """DELETE FROM Users
                WHERE user_id = ?"""
    params = [user_id]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)


def get_full_users(user_id):
    query = """SELECT user_id, payment_method, balance, user_name, user_level, games_owned FROM Users
    JOIN Wallets
    ON Users.wallet_id = Wallets.wallet_id
    WHERE user_id=?"""
    params = [user_id]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)
        for record in db.fetchall():
            print(record)
            print("------------------------------------------------------")

# ----------------------Orders-----------------------
def create_order(game_id: int, user_id: int, discount: int, price: int):
    query = """INSERT INTO Orders(game_id, user_id, discount, price) VALUES(?,?,?,?)"""
    params = [game_id, user_id, discount, price]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)


def get_orders():
    query = """SELECT * FROM Orders"""
    with DatabaseContextManager("Db.db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
            print("------------------------------------------------------")


def update_order(old_discount, new_discount):
    query = """UPDATE Orders
                SET discount = ?
                WHERE discount = ?"""
    params = [new_discount, old_discount]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)


def delete_order(order_id: int):
    query = """DELETE FROM Orders
                WHERE order_id = ?"""
    params = [user_id]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)


def get_full_orders(order_id):
    query = """SELECT order_id, game_name, genre, studio_name, employee_count, publisher_name, games_published, payment_method, balance, user_name, user_level, games_owned, discount, price FROM Orders
    JOIN Games
    ON Orders.game_id = Games.game_id
    JOIN Users
    ON Orders.user_id = Users.user_id
    JOIN Wallets
    ON Users.wallet_id = Wallets.wallet_id
    JOIN Publishers
    ON Games.publisher_id = Publishers.publisher_id
    JOIN Studios
    ON Games.studio_id = Studios.studio_id
    WHERE order_id=?"""
    params = [order_id]
    with DatabaseContextManager("Db.db") as db:
        db.execute(query, params)
        for record in db.fetchall():
            print(record)
            print("------------------------------------------------------")


#Creating All Tables In Specific Order:
create_table_studios()
create_table_publishers()
create_table_games()
create_table_wallets()
create_table_users()
create_table_orders()

def insert_dummy_data(x: bool):
    if (x == True):
        create_studio("Gearbox", 300)
        create_publisher("2K Games", 393)
        create_game(1, 1, "Borderlands 3", "FPS-Looter")
        create_studio("Raven Software", 239)
        create_publisher("Activision", 1430)
        create_game(2, 2, "COD: Modern Warfare", "FPS")
        create_studio("Visceral Games", 80)
        create_publisher("Electronic Arts", 2687)
        create_game(3, 3, "Battlefield 1", "FPS")
        create_studio("Valve", 360)
        create_publisher("Sierra Ent.", 591)
        create_game(4, 4, "Half-Life", "Action")
        create_wallet("Paypal", 200)
        create_user(1, "Milly", 22, 350)
        create_wallet("BTC", 350)
        create_user(2, "Dylan", 14, 200)
        create_wallet("Paypal", 3000)
        create_user(3, "Haley", 7, 100)
        create_wallet("VISA", 750)
        create_user(4, "Gabe", 47, 860)
        create_order(1, 1, 50, 8)
        create_order(2, 2, 10, 120)
        create_order(3, 3, 15, 90)
        create_order(4, 4, 5, 25)


#If there's no data change to True else keep it False:
insert_dummy_data(False)



#Printing Everything to Console:
print("////////////////////////Studios///////////////////////")
get_studios()
print("///////////////////////Publishers/////////////////////")
get_publishers()
print("/////////////////////////Games////////////////////////")
get_games()
print("///////////////////////Full_Games/////////////////////")
get_full_games(4)
print("////////////////////////Wallets///////////////////////")
get_wallets()
print("/////////////////////////Users////////////////////////")
get_users()
print("///////////////////////Full_Users/////////////////////")
get_full_users(4)
print("////////////////////////Orders////////////////////////")
get_orders()
print("//////////////////////Full_Orders/////////////////////")
get_full_orders(4)
