import pymysql
from connection import view_items, retrieve_result, insert_or_update


def add_new_product():
    item_name = input("Type the name of the product you would like to add: ").title().strip()
    item_price = input (f"Type the price of {item_name}: ")
    if len(item_name) == 0 or len(item_price) == 0:
        print(f"Error: input cannot be blank")
        return

    sql = f"INSERT INTO products (name, price) VALUES (\"{item_name}\", {item_price})"
    insert_or_update(query=sql)
    print(f"{item_name} has been added to the products menu.")


def update_products():
    view_items("products")
    product_id = int(input("Please specify the id of the product you want to update: "))
    sql = f"SELECT name, price FROM products WHERE product_id = {product_id}"
    original_product_name, original_product_price = retrieve_result(query=sql)
    new_product_name = input("What is the name of your new product? Leave blank if you don't want to update the name: ")        
    new_product_price = input(f"What is the price? Leave blank if you don't want to change the price: ")

    if len(new_product_name.strip()) == 0:
        new_product_name = original_product_name
    
    if len(new_product_price) == 0:
        new_product_price = original_product_price

    sql = f"""UPDATE products SET 
    name=\"{new_product_name}\", 
    price={new_product_price} 
    WHERE product_id={product_id}"""

    insert_or_update(query=sql)

    print("record updated")


def delete_product():

    view_items("products")
    item_id = input("Type the id of the product you would like to delete: ")
    if len(item_id) == 0:
        print(f"Error: input cannot be blank")
        return
    try:
        sql = f"DELETE FROM products WHERE product_id = {item_id}"
        insert_or_update(query = sql)
        print("record deleted")
    except pymysql.OperationalError:
        print("Insert a correct order ID")
        return

    