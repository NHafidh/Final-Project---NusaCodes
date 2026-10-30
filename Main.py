from Database import create_table, get_connection
from Product import Product
from Payment import payment
from Analytics import show_analysis

create_table()

while True:
    print("\n== Cashier ==")
    print("1/. Payment")
    print("2/. Add Product")
    print("3/. Check Stock")
    print("4/. Update stock")
    print("5/. Remove Product")
    print("6/. Analytics & Prediction")
    print("7/. Exit")

    choice = input("\n Pilih 1-7 :")

    if choice == "1":
        payment()

    elif choice == "2":
        product_name = input("\ninput product name :")
        stock = int(input("Add stock :"))
        price = float(input("add Product Price :"))
        new_obj = Product(product_name, price, stock)
        new_obj.add_stock()
        new_obj.check_stock()


    elif choice == "3":
        prod = Product("", 0, 0)
        prod.check_stock()

    elif choice == "4":
        product_id = int(input("\nInput Product's ID :"))
        new_stock = int(input ("Add new stock :"))
        prod = Product("", 0, 0)
        prod.update_stock( product_id, new_stock)
        prod.check_stock()

    elif choice == "5":
        product_id = int(input("\nInput the product id that you want to remove: "))
        prod = Product("", 0, 0)
        prod.delete_product(product_id)
        prod.tidyup_id() 
        prod.check_stock()

    elif choice == "6":
        show_analysis()

    elif choice == "7":
        print("\nExit from the Program....")
        break 

    else:
        print("invalid input")
    