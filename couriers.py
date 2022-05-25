import pymysql
import connection
from connection import view_items, retrieve_result, insert_or_update


def add_new_courier():
    courier_name = input("Type the name of the courier you would like to add: ").title().strip()
    courier_number = input (f"Type the number of {courier_name}: ")
    if len(courier_name) == 0 or len(courier_number) == 0:
        print(f"Error: input cannot be blank")
        return

    sql = f"INSERT INTO couriers (name, phone) VALUES (\"{courier_name}\", \"{courier_number}\")"

    insert_or_update(query = sql)
    print(f"{courier_name} has been added to the couriers menu.")


def update_courier():

    view_items("couriers")
    courier_id = int(input("Please specify the id of the courier you want to update: "))
    if len(courier_id) == 0:
        print(f"Error: input cannot be blank")
        return

    sql = f"SELECT name, phone FROM couriers WHERE courier_id = {courier_id}"
    original_courier_name, original_courier_phone = retrieve_result(query=sql)
 
    new_courier_name = input("What is the name of the courier? Leave blank if you don't want to update the name: ")        
    new_courier_phone = input(f"What is the phone number of {new_courier_name}? Leave blank if you don't want to change the phone number: ")

    if len(new_courier_name.strip()) == 0:
        new_courier_name = original_courier_name
    
    if len(new_courier_phone.strip()) == 0:
        new_courier_phone = original_courier_phone

    sql = f"UPDATE couriers SET name=\"{new_courier_name}\", phone=\"{new_courier_phone}\" WHERE courier_id={courier_id} "
    insert_or_update(query=sql)
    print("record updated")


def delete_courier():

    view_items("couriers")

    courier_id = input("Type the id of the courier you would like to delete: ")
    if len(courier_id) == 0:
        print(f"Error: input cannot be blank")
        return
    try:
        sql = f"DELETE FROM couriers WHERE courier_id = {courier_id}"
        insert_or_update(query = sql)
        print("record deleted")

    except pymysql.IntegrityError:
        print("Can not delete a courier, please delete the order he is assigned to first.")
    
   
