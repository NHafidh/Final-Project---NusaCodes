import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def show_analysis():
    file_path = "TransactionHistory.csv"
    if not os.path.exists(file_path):
        print("\nNo transaction data found. Please make a payment first.")
        return

    df = pd.read_csv(file_path)

    print("\n" + "="*40)
    print("    SALES ANALYTICS & PREDICTION")
    print("="*40)

    total_revenue = df["Price_Total"].sum()
    print(f"Total Revenue      : Rp {total_revenue:,.0f}")

    total_items = df["Total_Buy"].sum()
    print(f"Total Items Sold   : {total_items} pcs")
    
    best_sellers = df.groupby("Items_Name")["Total_Buy"].sum().sort_values(ascending=False)
    print("\nTop Selling Products:")
    print(best_sellers.head(3).to_string())

    plt.figure(figsize=(8, 5))
    plt.bar(best_sellers.index, best_sellers.values, color="skyblue")
    plt.title("Best Selling Products")
    plt.xlabel("Product Name")
    plt.ylabel("Quantity Sold")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    unique_days = df["Date"].nunique() 
    if unique_days > 0:
        avg_daily_sales = total_items / unique_days
        predicted_next_week = np.ceil(avg_daily_sales * 7)
        print("\n--- PREDICTION ---")
        print(f"Average daily sales : {avg_daily_sales:.2f} pcs/day")
        print(f"Predicted stock needed for next 7 days: {int(predicted_next_week)} pcs")
        print("Note: Make sure your stock is above this number to avoid running out!")
    
    print("="*40 + "\n")