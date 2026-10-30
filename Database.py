import sqlite3
import os

def get_connection():
    this_folder = os.path.dirname(os.path.abspath(__file__))
    path_db = os.path.join(this_folder, "DB.db")

    return sqlite3.connect(path_db)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        price REAL,
        stock INTEGER)
""")

    conn.commit()
    conn.close()