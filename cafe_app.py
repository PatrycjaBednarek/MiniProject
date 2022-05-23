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
    for row in results:
        print(row)
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


def retrieve_result(query):
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchone()
    cursor.close()
    return results

def insert_or_update(query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


def update_products():
    view_items("products")
    product_id = int(input("Please specify the id of the product you want to update: "))
    
    # get current name and price associated with the product_id above
    sql = f"SELECT name, price FROM products WHERE product_id = {product_id}"
    original_product_name, original_product_price = retrieve_result(query=sql)
    # can do try and excet to check if product id is correct
    # specify the updated name and price
    new_product_name = input("What is the name of your new product? Leave blank if you don't want to update the name: ")        
    new_product_price = input(f"What is the price? Leave blank if you don't want to change the price: ")

    if len(new_product_name.strip()) == 0:
        new_product_name = original_product_name
    
    if len(new_product_price.strip()) == 0:
        new_product_price = original_product_price

    sql = f"UPDATE products SET name=\"{new_product_name}\", price={new_product_price} WHERE product_id={product_id} "
    insert_or_update(query=sql)

def delete_product():
    view_items("products")
    item_id = int(input("Type the id of the product you would like to delete: "))
    cursor = connection.cursor()
    sql = f"DELETE FROM products WHERE product_id = {item_id}"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    print(cursor.rowcount, "record(s) deleted")


def add_new_courier():
    courier_name = input("Type the name of the courier you would like to add: ").title().strip()
    courier_number = input (f"Type the number of {courier_name}: ")
    cursor = connection.cursor()
    sql = f"INSERT INTO couriers (name, phone) VALUES (\"{courier_name}\", \"{courier_number}\")"
    cursor.execute(sql)
    connection.commit()
    cursor.close()


def update_courier():
    view_items("couriers")
    courier_id = int(input("Please specify the id of the product you want to update: "))
    
    # get current name and phone associated with the courier_id above
    sql = f"SELECT name, phone FROM couriers WHERE courier_id = {courier_id}"
    original_courier_name, original_courier_phone = retrieve_result(query=sql)
    # can do try and execute to check if product id is correct
    # specify the updated name and price
    new_courier_name = input("What is the name of the courier? Leave blank if you don't want to update the name: ")        
    new_courier_phone = input(f"What is the phone number of {new_courier_name}? Leave blank if you don't want to change the phone number: ")

    if len(new_courier_name.strip()) == 0:
        new_courier_name = original_courier_name
    
    if len(new_courier_phone.strip()) == 0:
        new_courier_phone = original_courier_phone

    sql = f"UPDATE couriers SET name=\"{new_courier_name}\", phone={new_courier_phone} WHERE courier_id={courier_id} "
    insert_or_update(query=sql)


def delete_courier():
    view_items("couriers")
    courier_id = int(input("Type the id of the courier you would like to delete: "))
    cursor = connection.cursor()
    try:
        sql = f"DELETE FROM couriers WHERE courier_id = {courier_id}"
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        print(cursor.rowcount, "record(s) deleted")
    except: pymysql.IntegrityError
    print("Can not delete a courier, please delete the order he is assigned to first")


def create_new_order():
    customer_name = input("Type the customer name: ").title().strip()
    customer_address = input (f"Type the address of {customer_name}: ").title().strip()
    customer_phone_number = input(f"Type the phone number of {customer_name}: ").title().strip()
    
    view_items("products")
    items = input("Please add a coma separated lis of product ids e.g. 1,2,3: ").title().strip()
    # may want to do some checks above
    view_items("couriers")
    courier_id = int(input(f"Please select a courier from the courier table displayed above: "))
    order_status = 1
    sql = f"INSERT INTO orders (customer_name, customer_address, customer_phone_number, courier_id, order_status, items) VALUES (\"{customer_name}\", \"{customer_address}\", \"{customer_phone_number}\", {courier_id}, \"{order_status}\", \"{items}\")"
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    print("You have correctly placed the order!")


def update_order_status():
    view_items("orders")
    order_id = int(input("Please specify the id of the order you want to update: "))
    view_items("orderstatus")
    # get current name and phone associated with the courier_id above
    sql = f"SELECT status FROM orders WHERE order_id = {order_id}"
    original_order_status = retrieve_result(query=sql)
    # can do try and execute to check if product id is correct
    # specify the updated name and price
    new_order_status = input("What is the new order status? Leave blank if you don't want to update the status: ")        
    if len(new_order_status.strip()) == 0:
        new_order_status = original_order_status

    sql = f"UPDATE orders SET status=\"{new_order_status}\""
    insert_or_update(query=sql)
    print(cursor.rowcount, "record(s) updated")


def update_order():
    view_items("orders")
    order_id = int(input("Please specify the id of the order you want to update: "))
    

    # get current name and price associated with the product_id above
    sql = f"SELECT customer_name, customer_address, customer_phone_number FROM orders WHERE order_id = {order_id}"
    original_customer_name, original_customer_address, original_phone_number = retrieve_result(query=sql)
    # can do try and excet to check if product id is correct
    # specify the updated name and price
    new_customer_name = input("What is the name of your customer? Leave blank if you don't want to update the name: ").title().strip()      
    new_customer_address = input(f"What is the new address? Leave blank if you don't want to change the address: ").title().strip()
    new_customer_phone = input(f"What is the new phone number? Leave blank if you don't want to change the phone number: ").title().strip()
    if len(new_customer_name.strip()) == 0:
        new_customer_name = original_customer_name
    
    if len(new_customer_address.strip()) == 0:
        new_customer_address = original_customer_address

    if len(new_customer_phone.strip()) == 0:
        new_customer_phone = original_phone_number

    sql = f"UPDATE orders SET customer_name=\"{new_customer_name}\", customer_address=\"{new_customer_address}\", customer_phone_number=\"{new_customer_phone}\" WHERE order_id={order_id} "
    insert_or_update(query=sql)
        print(cursor.rowcount, "record(s) updated")

def delete_order():
    view_items("orders")
    order_id = int(input("Type the id of the order you would like to delete: "))
    cursor = connection.cursor()
    #try:
    sql = f"DELETE FROM orders WHERE order_id = {order_id}"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    print(cursor.rowcount, "record(s) deleted")
    #except: pymysql.IntegrityError
    #print("Can not delete a courier, please delete the order he is assigned to first")
    



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
            create_new_order()
        elif order_menu_input == 3:
            update_order_status()
        elif order_menu_input == 4:
            update_order()
        elif order_menu_input == 5:
            delete_order()


