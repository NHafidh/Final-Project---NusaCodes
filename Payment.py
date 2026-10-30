import sqlite3
import csv
import os
from datetime import datetime
from Database import get_connection 
from Product import Product

def payment():
    conn = get_connection()
    cursor = conn.cursor()

    print("\n=== Payment menu ===")
    product_name = input("Input the product name: ")

    cursor.execute("SELECT id, price, stock FROM Product WHERE product_name = ?", (product_name,))
    result = cursor.fetchone() 

    if result is None:
        print(f"Item '{product_name}' not found in database!")
        conn.close()
        return 

    product_id = result[0]
    price = result[1]
    stock = result[2]

    print(f"Item found: {product_name} | Price: Rp {price:,.0f} | Stock: {stock}")

    try:
        total_buy = int(input("Input how many do you wanna buy: "))
    except ValueError:
        print("Input must be Numbers")
        conn.close()
        return

    if total_buy <= 0:
        print("You can't buy nothing fellas")
    elif total_buy > stock:
        print(f"No Product in stock : {stock}.")
    else:
        total_payment = price * total_buy
        print(f"\n Total payment: Rp {total_payment:,.0f}")

        new_stock = stock - total_buy
        cursor.execute("UPDATE Product SET stock = ? WHERE id = ?", (new_stock, product_id))
        conn.commit()  

        print(f"Payment Successfull!")
        print(f"Remaining {product_name}: {new_stock}")

        file_exists = os.path.isfile("TransactionHistory.csv")
        with open("TransactionHistory.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            
            if not file_exists:
                writer.writerow(["Date", "Items_Name", "Total_Buy", "Price_Total"])
            
            today_date = datetime.now().strftime("%Y-%m-%d")
            writer.writerow([today_date, product_name, total_buy, total_payment])
            
        print("Transaction saved to history!\n")

    conn.close()