import sqlite3

DB_NAME = "zomato.db"

def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

def create_tables():
    conn = get_connection()
    c = conn.cursor()

    # Restaurants
    c.execute('''CREATE TABLE IF NOT EXISTS restaurants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )''')

    # Menu items
    c.execute('''CREATE TABLE IF NOT EXISTS menu_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    restaurant_id INTEGER,
                    name TEXT NOT NULL,
                    price REAL,
                    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
                )''')

    # Reviews
    c.execute('''CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    restaurant_id INTEGER,
                    user_name TEXT,
                    review_text TEXT,
                    fraud BOOLEAN,
                    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
                )''')

    conn.commit()
    conn.close()

def fetch_all(query, params=()):
    conn = get_connection()
    c = conn.cursor()
    c.execute(query, params)
    data = c.fetchall()
    conn.close()
    return data

def execute_query(query, params=()):
    conn = get_connection()
    c = conn.cursor()
    c.execute(query, params)
    conn.commit()
    conn.close()
