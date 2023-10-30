import pymysql
from test_database import show_index_couriers
from test_database import selecting_product_items

# Connecting to database
def connect_to_database():
    connection = pymysql.connect(
                host='localhost', database='Mini_Project',
                user='root', password='password'
            )
    return connection

#function to sort orders
def sort_orders(orders_list):
    print(orders_list)
    sort_choice = input("Please choose if you would like to sort orders by 'Status' or 'Courier':\n")
    if sort_choice == "Status":
        print("")
        #orders_list.sort(key=lambda x: x[5])
        orders_list = sorted(orders_list, key=lambda o: o[5])
        print("Sorted orders by: Order Status\n")
    elif sort_choice == 'Courier':
        print("")
        #orders_list.sort(key= orders_list[4])
        orders_list = sorted(orders_list, key=lambda o: o[4])
        print("Sorted orders by: Courier\n")
    else:
        print("Error with sort choice")
        print("Printing all orders list unsorted!\n")
    return orders_list

#Function to print all orders and sort by status or couriers
def print_all_orders(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM orders')
            orders_list = cursor.fetchall()
    print()

    orders_list = sort_orders(orders_list)

    for orders in orders_list:
        print(f'\nCustomer Name: {orders[1]}')
        print(f'Customer Address: {orders[2]}')
        print(f'Phone Number: {orders[3]}')
        print(f'Courier: {orders[4]}')
        print(f'Order Status: {orders[5]}')
        print(f'Items: {orders[6]}\n')

#Function to print all existing orders in numbered list
def print_orders_with_index(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM orders')
            orders_list = cursor.fetchall()

    print("Printing all existing orders!\n")
    if orders_list != []:

        orders_list = sort_orders(orders_list)

        for orders in orders_list:
            print (f"======================= Order ID {orders[0]} =======================")

            print(f'\nCustomer Name: {orders[1]}')
            print(f'Customer Address: {orders[2]}')
            print(f'Phone Number: {orders[3]}')
            print(f'Courier: {orders[4]}')
            print(f'Order Status: {orders[5]}')
            print(f'Items: {orders[6]}\n')
        print("===========================================================")
        print("\n")
    else:
        print("There are no more orders left!")


################### Testing printing functions ################################

#print_all_orders(connect_to_database())

#print_orders_with_index(connect_to_database())


######################## Updated for week 6 Requirements #############################

def add_new_order(connection):

    customer_name = input("Please enter your name:\n")
    print("")
    customer_address =input("Please enter your address:\n")
    print("")
    customer_number = input("Please enter your phone number:\n")
    print("")
    #new_order = {}
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM couriers')
            couriers = cursor.fetchall()
            show_index_couriers(couriers)

        while True:
            try:
                chosen_courier = int(input("Please choose the ID Number of the courier:\n"))
            except ValueError as e:
                print("Error: You did not enter a number")
                chosen_courier = -1
            try:
                courier_check = couriers[chosen_courier - 1] in couriers
            except IndexError as e:
                print("Error: ID number was not in range")
                courier_check = False
            if courier_check  == True:
                break
            else:
                print("Please try again!")


        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM products')
            products = cursor.fetchall()
            chosen_products = selecting_product_items(products)


            sql = "INSERT INTO orders (customer_name, customer_address, phone_number, courier_id, status_id, items) VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (customer_name, customer_address, customer_number, chosen_courier, 1, chosen_products))
            connection.commit()


def delete_order(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM orders')
            orders = cursor.fetchall()

            orders = sort_orders(orders)

            for order in (orders):
                print (f"======================= Order ID {order[0]} =======================")

                print(f'\nCustomer Name: {order[1]}')
                print(f'Customer Address: {order[2]}')
                print(f'Phone Number: {order[3]}')
                print(f'Courier: {order[4]}')
                print(f'Order Status: {order[5]}')
                print(f'Items: {order[6]}\n')
            print("===========================================================")
            print("\n")

            print("Please select an ID number from the list above to delete:\n")
            try:
                order_delete = int(input("Enter here:\n"))-1
            except ValueError as e:
                print("Error input was not a number,", e)
                order_delete = -1


            if order_delete >= 0 and order_delete <= len(orders):
                print("\nCurrently selected for deletion:\nRecord from orders database:")

                print(f'Order ID: {orders[order_delete][0]}')
                print(f'Customer Name: {orders[order_delete][1]}')
                print(f'Customer Address: {orders[order_delete][2]}')
                print(f'Phone Number: {orders[order_delete][3]}')
                print(f'Courier: {orders[order_delete][4]}')
                print(f'Order Status: {orders[order_delete][5]}')
                print(f'Items: {orders[order_delete][6]}\n')

                confirmation = input("Please enter DELETE if you would like to continue:\n")
                if confirmation == "DELETE":
                    print("Deleted:", orders[order_delete])
                    sql = f"DELETE FROM orders where order_id = {orders[order_delete][0]}"
                    cursor.execute(sql)
                    connection.commit()
                else:
                    print(f"Canceled the deletion of {orders[order_delete]}")


#################### WORK IN PROGRESS ##########################
def update_order(orders, connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM couriers')
            couriers_list = cursor.fetchall()

            cursor.execute('SELECT * FROM products')
            products_list = cursor.fetchall()
    new_order = []

    #chosen_order = input_order()
    chosen_order = int(input("Testing range:\n"))-1

    for key, value in orders[chosen_order].items():

        print(f"The current {key} is: {value}")
        if key == 'Courier':
            for index, courier in enumerate(couriers_list):
                print(f"{index + 1}. {courier[1]}")
            print("")
            while True:
                try:
                    new_value = int(input("Please choose the ID Number of the courier:\n"))

                except ValueError as e:
                    print("Error: invalid input\nPlease try again")
                    new_value = -1
                if new_value > 0 and new_value <= len(couriers_list):
                    new_order.append({key:new_value})
                    orders[chosen_order].update({key:new_value})
                    break
                else:
                    print("Error invalid courier ID has been selected")
                    print("Please try again!")


        elif key == 'Items':
            change_items = input("Please enter 'YES' if you would like to choose a new list of items:\n")
            if change_items == "YES":
                print("Removing previous items")
                new_value = selecting_product_items(products_list)
                new_order.append({key:new_value})
                orders[chosen_order].update({key:new_value})
            else:
                print(f"You have chosen to keep {key}: {value}")
        else:
            new_value = input(f"Please enter the new value for {key}:\n")
            if new_value != "":
                new_order.append({key:new_value})
                orders[chosen_order].update({key:new_value})
            else:
                continue
    return orders

############ TESTING Orders fuctions with database ####################

#add_new_order(connect_to_database())

#delete_order(connect_to_database())

#update_order()