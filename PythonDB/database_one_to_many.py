import sqlite3


# EXAMPLE Of 1-to-Many Database

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


def create_table_transactions():
    query = """CREATE TABLE Transactions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount FLOAT,
                send_to_account TEXT,
                sender_id INTEGER,
                FOREIGN KEY (sender_id) REFERENCES Accounts(id)
                )"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_table_account():
    query = """CREATE TABLE Accounts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                balance FLOAT,
                credit_rating INTEGER)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_transaction(amount: float, send_to_account: str, sender: int):
    query = """INSERT INTO Transactions(amount, send_to_account, sender_id) VALUES(?,?,?)"""
    parameters = [amount, send_to_account, sender]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def create_account(balance: int, credit_rating: int):
    query = """INSERT INTO Accounts(balance, credit_rating) VALUES(?,?)"""
    parameters = [balance, credit_rating]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_transactions():
    query = """SELECT * FROM Transactions"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)
    print("--------------------------------------------------------")


def get_accounts():
    query = """SELECT * FROM Accounts"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        db.lastrowid
        for row in db.fetchall():
            print(row)
    print("------------------------------------------------------------")


def update_transaction(amount: float, id: int):
    query = """UPDATE Transactions
                SET amount = ?
                WHERE id = ?"""
    parameters = [amount, id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def update_accounts(balance: float, id: int):
    query = """UPDATE Transactions
                SET balance = ?
                WHERE id = ?"""
    parameters = [balance, id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_account_transcations():
    query = """SELECT * FROM Transactions
                JOIN Accounts
                    ON Transactions.sender_id = Accounts.id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)
