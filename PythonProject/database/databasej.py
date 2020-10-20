import sqlite3

class DB(object):
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()

def create_table_books():
    query = """CREATE TABLE IF NOT EXISTS Books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                pages INTEGER)"""
    with DB("db") as db:
        db.execute(query)

def create_book(title: str, author: str, pages: int):
    query = f"""INSERT INTO Books(title, author, pages) VALUES('{title}', '{author}', '{pages}')"""
    with DB("db") as db:
        db.execute(query)

def get_book():
    query = """SELECT * FROM Books"""
    with DB("db") as db:
        db.execute(query)
        data = db.fetchall()
        for row in data:
            print(row)

create_table_books()
create_book("Eragon", "R.T", 450)
get_book()