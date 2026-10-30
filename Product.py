import sqlite3
from Database import get_connection

class Product:
    def __init__(self, product_name, price, stock):
        self.product_name = product_name
        self.price = price
        self.stock = stock

    def add_stock(self):
        conn = get_connection() 
        cursor = conn.cursor()

        query = "INSERT INTO Product (product_name, price, stock) VALUES (?, ?, ?)"

        cursor.execute(query,(self.product_name, self.price, self.stock))

        conn.commit()
        conn.close()

    def check_stock(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Product")

        result  = cursor.fetchall()

        print("\nID | Product Name | Price | Stock")
        print ("-" * 40)
        for row in result:
            print (f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

        conn.close()

    def update_stock(self, product_id, new_stock):
        conn = get_connection()
        cursor = conn.cursor()

        query = "UPDATE Product SET stock = ? WHERE id = ?"

        cursor.execute(query, (new_stock, product_id))

        conn.commit()
        conn.close()
        print (f"product's stock with ID : {product_id}, successfully updated")

    def delete_product(self, product_id):
        conn = get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM Product WHERE id = ?"

        cursor.execute(query,(product_id,))

        conn.commit()
        conn.close()
        print(f"Product with id :{product_id}, successfully removed")

    def tidyup_id(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, product_name, price, stock FROM Product ORDER BY id")
        data = cursor.fetchall()
        
        cursor.execute("DELETE FROM Product")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='Product'") 
        
        for index, item in enumerate(data, start=1):

            cursor.execute(
                "INSERT INTO Product (id, product_name, price, stock) VALUES (?, ?, ?, ?)", 
                (index, item[1], item[2], item[3])
            )
            
        conn.commit()
        conn.close()
