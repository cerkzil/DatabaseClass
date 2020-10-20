import sqlite3


# EXAMPLE Of 1-to-1 Database


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


def create_table_Person():
    query = """CREATE TABLE Person(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                last_name TEXT,
                SSN_ID INTEGER,
                FOREIGN KEY (SSN_ID) REFERENCES SSN(id))"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_table_SSN():
    query = """CREATE TABLE SSN(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                number INTEGER,
                person_id INTEGER,
                FOREIGN KEY (person_id) REFERENCES Person(id))"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def update_person(db, ssn_id, id):
    query = """UPDATE Person
                SET SSN_ID = ?
                WHERE id = ?"""
    parameters = [ssn_id, id]
    db.execute(query, parameters)


def create_one_to_one(name: str, last_name: str, number: int):
    query = """INSERT INTO Person(name,last_name,SSN_ID) VALUES(?,?,?)"""
    parameters = [name, last_name, None]
    query1 = """INSERT INTO SSN(number, person_id) VALUES(?,?)"""
    parameters1 = [number]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)
        last_person_id = db.lastrowid
        parameters1.append(last_person_id)
        db.execute(query1, parameters1)
        ssn_id = db.lastrowid
        update_person(db, ssn_id, last_person_id)


def get_table_person():
    query = """SELECT * FROM Person"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)
    print("-------------------------------------------")


def get_table_SSN():
    query = """SELECT * FROM SSN"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)


def get_person_ssn():
    query = """SELECT * FROM SSN
                JOIN Person
                    ON SSN.id = Person.id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)
