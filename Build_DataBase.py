import sqlite3

def Build_DataBase():
    connection = sqlite3.connect("Cars_DataBase.db")  
    cursor = connection.cursor()
    
    schema = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        model TEXT NOT NULL,
        price REAL NOT NULL,
        color TEXT NOT NULL,
        image_path TEXT
    );

    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        car_id INTEGER NOT NULL,
        buyer_name TEXT NOT NULL,
        buyer_phone TEXT NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY (car_id) REFERENCES cars(id)
    );
    """
    
    cursor.executescript(schema)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    Build_DataBase()
