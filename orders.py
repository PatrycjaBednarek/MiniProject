import pymysql
import connection
from connection import view_items, retrieve_result, insert_or_update

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="mini_project"
)

cursor = connection.cursor()
cursor.close()

def view_orders():
    cursor = connection.cursor()
    sql = f"SELECT * FROM orders"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(f"""Order ID: {(row[0])}, 
        Customer name: {row[1]}, 
        Customer address: {row[2]}, 
        Phone number: {row[3]}, 
        Courier ID: {row[4]}, 
        Order status: {row[5]},
        Items ordered: {row[6]}'
        """)
    cursor.close()
    return results


def create_new_order():

    customer_name = input("Type the customer name: ").title().strip()
    customer_address = input (f"Type the address of {customer_name}: ").title().strip()
    customer_phone_number = input(f"Type the phone number of {customer_name}: ").title().strip()
    if len(customer_name) == 0 or len(customer_address) == 0 or len(customer_phone_number) == 0:
        print(f"Error: input cannot be blank")
        return

    view_items("products")
    items = input("Please add a coma separated lis of product ids e.g. 1,2,3: ").title().strip()
    if len(items) == 0:
        print(f"Error: input cannot be blank")
        return

    view_items("couriers")
    courier_id = input(f"Please select a courier from the courier table displayed above: ")
    if len(courier_id) == 0:
        print(f"Error: input cannot be blank")
        return

    order_status = 1
    sql = f"""INSERT INTO orders 
    (customer_name, customer_address, customer_phone_number, courier_id, status, items) 
    VALUES (\"{customer_name}\", \"{customer_address}\", \"{customer_phone_number}\", 
    {courier_id}, \"{order_status}\", \"{items}\")"""
    
    insert_or_update(query = sql)
    print("You have correctly placed the order!")
    

def update_order_status():

    view_orders()
    order_id = input("Please specify the id of the order you want to update: ")
    if len(order_id) == 0:
        print(f"Error: input cannot be blank")
        return

    view_items("orderstatus")

    sql = f"SELECT status FROM orders WHERE order_id = {order_id}"

    original_order_status = retrieve_result(query=sql)
   
    new_order_status = input("What is the new order status? Leave blank if you don't want to update the status: ") 

    if len(new_order_status.strip()) == 0:
        new_order_status = original_order_status

    try:
        sql = f"UPDATE orders SET status=\"{new_order_status}\""
        insert_or_update(query=sql)
        print("record updated")
    except pymysql.IntegrityError:
        print("Make sure you input correct id of order status: 1 - preparing, 2 - out for delivery or 3 - delivered ")


def update_order():

    view_orders()

    order_id = input("Please specify the id of the order you want to update: ")
    if len(order_id) == 0:
        print(f"Error: input cannot be blank")
        return

    sql = f"SELECT customer_name, customer_address, customer_phone_number, courier_id, items FROM orders WHERE order_id = {order_id}"

    original_customer_name, original_customer_address, original_phone_number, original_courier, original_items = retrieve_result(query=sql)
 
    new_customer_name = input("""What is the name of your customer? Leave blank if you don't want to update the name: """).title().strip()      

    new_customer_address = input(f"""What is the new address? Leave blank if you don't want to change the address: """).title().strip()

    new_customer_phone = input(f"""What is the new phone number? Leave blank if you don't want to change the phone number: """).title().strip()

    view_items("products")

    new_items = input("Please add a coma separated list of product IDs you would like to update e.g. 1,2,3: ").title().strip()

    view_items("couriers")

    new_courier = input("Please input a new courier ID, leave blank if you don't want to change the courier: ")

    if len(new_customer_name.strip()) == 0:
        new_customer_name = original_customer_name
    
    if len(new_customer_address.strip()) == 0:
        new_customer_address = original_customer_address

    if len(new_customer_phone.strip()) == 0:
        new_customer_phone = original_phone_number
    
    if len(new_items.strip()) == 0:
        new_items = original_items

    if len(new_courier) == 0:
        new_courier = original_courier

    try:
        sql = f"""UPDATE orders SET 
        customer_name = \"{new_customer_name}\", 
        customer_address = \"{new_customer_address}\", 
        customer_phone_number=\"{new_customer_phone}\",
        courier_id = {new_courier},
        items = \"{new_items}\"
        WHERE order_id={order_id}"""
        insert_or_update(query=sql)
        print("record updated")

    except pymysql.IntegrityError or pymysql.OperationalError:
        print("Make sure you input an existing courier ID")
   

def delete_order():

    view_orders()

    order_id = input("Type the id of the order you would like to delete: ")
    if len(order_id) == 0:
        print(f"Error: input cannot be blank")
        return
    try:
        sql = f"DELETE FROM orders WHERE order_id = {order_id}"
        insert_or_update(query = sql)
        print("record deleted")

    except pymysql.ProgrammingError:
        print("Please enter a valid order ID")
