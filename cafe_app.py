import pymysql
import pandas as pd

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="mini_project"
)

cursor = connection.cursor()
cursor.close()


def view_items(table_name):
    # possible to use pandas instead

    cursor = connection.cursor()
    sql = f"SELECT * FROM {table_name}"

        # Gets all rows from the result
        # rows = cursor.fetchall()
        # for row in rows:
        # print(f'First Name: {str(row[0])}, Last Name: {row[1]}, Age: {row[2]}')
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    cursor.close()
    return results


def add_new_product():
    item_name = input("Type the name of the product you would like to add: ").title().strip()
    item_price = float(input (f"Type the price of {item_name}: "))
    cursor = connection.cursor()
    sql = f"INSERT INTO products (name, price) VALUES (\"{item_name}\", {item_price})"
    cursor.execute(sql)
    connection.commit()
    cursor.close()


def update_products():
    view_items(table_name="products")
    product_id = int(input("Please specify the id of the product you want to update: "))
    
    # get current name and price associated with the product_id above
    sql = f"SELECT name, price FROM products WHERE product_id = {product_id}"
    original_product_name, original_product_price = retrieve_result(sql)
    
    # specify the updated name and price
    new_product_name = input("What is the name of your new product? Leave blank if you don't want to update the name: ")        
    new_product_price = input(f"What is the price? Leave blank if you don't want to change the price")

    if len(new_product_name.strip()) == 0:
        new_product_name = original_product_name
    
    if len(new_product_price.strip()) == 0:
        new_product_price = original_product_price

    sql = f"UPDATE products SET name=\"{new_product_name}\", price={new_product_price} WHERE product_id={product_id} "
    insert_or_update(query=sql)


def add_new_courier():
    courier_name = input("Type the name of the courier you would like to add: ").title().strip()
    courier_number = input (f"Type the number of {courier_name}: ")
    cursor = connection.cursor()
    sql = f"INSERT INTO couriers (name, phone) VALUES (\"{courier_name}\", \"{courier_number}\")"
    cursor.execute(sql)
    connection.commit()
    cursor.close()


def update_courier():
    return


def delete_courier():
    return


def create_order():
    customer_name = input("Type the customer name: ").title().strip()
    customer_address = float(input (f"Type the price of {item_name}: "))
    cursor = connection.cursor()
    sql = f"INSERT INTO products (name, price) VALUES (\"{item_name}\", {item_price})"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    return


def update_order_status():
    return

def update_order():
    return

def delete_order():




while True:
    # see main menu
    print("The main menu: press 0 to exit the app, 1 to see the products menu, 2 to see the courier menu, 3 to see orders menu")
    main_menu_option = int(input("Please select your choice from the main menu: "))

    if main_menu_option == 0:
        connection.close()
        break

    elif main_menu_option == 1:
        print(""""press 0 to return to main menu,
        1 to see the products, 
        2 to add a new product, 
        3 to update a product 
        and 4 to delete a prodcut""")

        product_menu_input = int(input("Please select an option from the products menu: "))
        if product_menu_input == 0:
            continue

        elif product_menu_input == 1:
            view_items(table_name = "products")
        elif product_menu_input == 2:
            add_new_product()
        elif product_menu_input == 3:
            update_products()
        elif product_menu_input == 4:
            delete_product()
    
    elif main_menu_option == 2:
        print(""""press 0 to return to main menu,
        1 to see the couriers, 
        2 to add a new courier, 
        3 to update a courier 
        and 4 to delete a courier""")
        
        courier_menu_input = int(input("Please select an option from the courier menu: "))
        if courier_menu_input == 0:
            continue

        elif courier_menu_input == 1:
            view_items(table_name = "couriers")
        elif courier_menu_input == 2:
            add_new_courier()
        elif courier_menu_input == 3:
            update_courier()
        elif courier_menu_input == 4:
            delete_courier()

    elif main_menu_option == 3:
        print(""""press 0 to return to main menu,
        1 to see the orders, 
        2 to add a new order, 
        3 to update order status 
        4 to update existing order
        5 to delete order""")


        order_menu_input = int(input("Please select an option from the orders menu: "))
        if order_menu_input == 0:
            continue

        elif order_menu_input == 1:
            view_items(table_name = "orders")
        elif order_menu_input == 2:
            add_new_order()
        elif order_menu_input == 3:
            update_order_status()
        elif order_menu_input == 4:
            update_order()
        elif order_menu_input == 5:
            delete_order()

