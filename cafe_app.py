import products
import orders
import couriers
import connection
from connection import view_items



while True:
    # see main menu
    print("""The main menu: 
    Press 0 to exit the app, 
    1 to see the products menu, 
    2 to see the courier menu, 
    3 to see orders menu""")

    main_menu_option = int(input("Please select your choice from the main menu: "))

    if main_menu_option == 0:
        connection.close()
        break

    elif main_menu_option == 1:

        print(""""Products menu:
        Press 0 to return to main menu,
        1 to see the products,
        2 to add a new product, 
        3 to update a product 
        and 4 to delete a prodcut""")

        product_menu_input = int(input("Please select an option from the products menu: "))
        if product_menu_input == 0:
            continue

        elif product_menu_input == 1:
            view_items("products")
        elif product_menu_input == 2:
            products.add_new_product()
        elif product_menu_input == 3:
            products.update_products()
        elif product_menu_input == 4:
            products.delete_product()
    
    elif main_menu_option == 2:

        print(""""Couriers menu:
        Press 0 to return to main menu,
        1 to see the couriers, 
        2 to add a new courier, 
        3 to update a courier 
        and 4 to delete a courier""")
        
        courier_menu_input = int(input("Please select an option from the courier menu: "))
        if courier_menu_input == 0:
            continue

        elif courier_menu_input == 1:
            view_items("couriers")
        elif courier_menu_input == 2:
            couriers.add_new_courier()
        elif courier_menu_input == 3:
            couriers.update_courier()
        elif courier_menu_input == 4:
            couriers.delete_courier()

    elif main_menu_option == 3:

        print(""""Orders menu:
        Press 0 to return to main menu,
        1 to see the orders, 
        2 to add a new order, 
        3 to update order status 
        4 to update existing order
        5 to delete order""")


        order_menu_input = int(input("Please select an option from the orders menu: "))
        if order_menu_input == 0:
            continue

        elif order_menu_input == 1:
            orders.view_orders()
        elif order_menu_input == 2:
            orders.create_new_order()
        elif order_menu_input == 3:
            orders.update_order_status()
        elif order_menu_input == 4:
            orders.update_order()
        elif order_menu_input == 5:
            orders.delete_order()


