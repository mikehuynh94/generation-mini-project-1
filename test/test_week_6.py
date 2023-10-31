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


    if orders_list != []:

        orders_list = sort_orders(orders_list)


        for index, orders in enumerate(orders_list):
            print (f"======================= Order No. {index + 1} =======================")
            #print(f'Order ID: {orders[0]}')
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
    return orders_list


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
            orders = print_orders_with_index(connect_to_database())

            print("Please select an Order No. from the list above to delete:\n")
            try:
                order_delete = int(input("Enter here:\n"))-1
            except ValueError as e:
                print("Error input was not a number,", e)
                order_delete = -1


            if order_delete >= 0 and order_delete <= len(orders):
                print("\nCurrently selected for deletion:\nRecord from orders database:")

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
            else:
                print("Error: invalid order number Selected\nPlease Try again!")


def update_order_status(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM orders')
            orders = cursor.fetchall()
            orders = print_orders_with_index(connect_to_database())

            print("Please select an Order No. from the list above to update the status:\n")
            try:
                order_status_update = int(input("Enter here:\n"))-1
            except ValueError as e:
                print("Error input was not a number,", e)
                order_status_update = -1

            if order_status_update >= 0 and order_status_update <= len(orders):
                print("\nCurrently selected for status update:\nRecord from orders database:")

                print(f'Customer Name: {orders[order_status_update][1]}')
                print(f'Customer Address: {orders[order_status_update][2]}')
                print(f'Phone Number: {orders[order_status_update][3]}')
                print(f'Courier: {orders[order_status_update][4]}')
                print(f'Order Status: {orders[order_status_update][5]}')
                print(f'Items: {orders[order_status_update][6]}\n')


            cursor.execute('SELECT * FROM order_status')
            order_status = cursor.fetchall()
            for status in order_status:
                print(f'{status[0]}: {status[1]}')

            chosen_status = input("\nPlease select the new status ID:\n")
            try:
                chosen_status = int(chosen_status)
            except TypeError:
                chosen_status = -1
            except ValueError:
                chosen_status = -1


            if chosen_status > 0 and chosen_status <= len(order_status):
                print()
                #update order status
                sql = f"UPDATE orders SET status_id = {chosen_status} WHERE order_id = {orders[order_status_update][0]}"
                cursor.execute(sql, ())
                connection.commit()
                print(f"Successfully updated {orders[order_status_update][1]}'s order to {chosen_status}")
            else:
                print('\nError invalid selection\nPlease try again!')



def update_order(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM couriers')
            couriers = cursor.fetchall()

            cursor.execute('SELECT * FROM products')
            products_list = cursor.fetchall()

            cursor.execute('SELECT * FROM orders')
            orders = cursor.fetchall()
            orders = print_orders_with_index(connect_to_database())

            print("Please select an ID number from the list above to update:\n")
            try:
                order_update_index = int(input("Enter here:\n"))-1
            except ValueError as e:
                print("Error input was not a number,", e)
                order_update_index = -1

            if order_update_index >= 0 and order_update_index <= len(orders):
                print("\nCurrently selected for update:\nRecord from orders database:")

                print(f'Order ID: {orders[order_update_index][0]}')
                print(f'Customer Name: {orders[order_update_index][1]}')
                print(f'Customer Address: {orders[order_update_index][2]}')
                print(f'Phone Number: {orders[order_update_index][3]}')
                print(f'Courier: {orders[order_update_index][4]}')
                print(f'Order Status: {orders[order_update_index][5]}')
                print(f'Items: {orders[order_update_index][6]}\n')

            new_customer_name = input(f"Please enter the new value for\ncustomer name: {orders[order_update_index][1]}:\n")
            if new_customer_name != "":
                sql = f"UPDATE orders SET customer_name = '{new_customer_name}' WHERE order_id = {orders[order_update_index][0]}"
                cursor.execute(sql)
                connection.commit()
                print(f"Successfully updated customer name to: {new_customer_name}")
            else:
                print("Customer name has not been updated")

            new_customer_address = input(f"Please enter the new value for\naddress: {orders[order_update_index][2]}:\n")
            if new_customer_address != "":
                sql = f'UPDATE orders SET customer_address = "{new_customer_address}" WHERE order_id = {orders[order_update_index][0]}'
                cursor.execute(sql)
                connection.commit()
                print(f"Successfully updated customer address to: {new_customer_address}")
            else:
                print("Customer address has not been updated")

            new_customer_phone = input(f"Please enter the new value for\ncontact number: {orders[order_update_index][3]}:\n")
            if new_customer_phone != "":
                sql = f"UPDATE orders SET phone_number = '{new_customer_phone}' WHERE order_id = {orders[order_update_index][0]}"
                cursor.execute(sql)
                connection.commit()
                print(f"Successfully updated contact number to: {new_customer_phone}")
            else:
                print("Customer name has not been updated")


            show_index_couriers(couriers)

            while True:
                print(f'Currently updating Courier: {orders[order_update_index][4]}')
                chosen_courier = input("Please choose the ID Number of the courier:\n")
                if chosen_courier != "":
                    try:
                        chosen_courier = int(chosen_courier)
                    except ValueError as e:
                        print("Error: You did not enter a number")
                        chosen_courier = -1

                    if chosen_courier >=  0 and chosen_courier <= len(couriers):
                        sql = f"UPDATE orders SET courier_id = {chosen_courier} WHERE order_id = {orders[order_update_index][0]}"
                        cursor.execute(sql)
                        connection.commit()
                        print(f"Successfully updated courier to: {chosen_courier}")
                        break
                    else:
                        print("Error: Courier ID number was not in range please try again")


                else:
                    print("Courier was not updated")
                    break



            cursor.execute('SELECT * FROM order_status')
            order_status = cursor.fetchall()
            for status in order_status:
                print(f'{status[0]}: {status[1]}')
            print(f'\nCurrently updating order status: {orders[order_update_index][5]}')
            chosen_status = input("\nPlease select the new status ID:\n")
            try:
                chosen_status = int(chosen_status)
            except TypeError:
                chosen_status = -1
            except ValueError:
                chosen_status = -1


            if chosen_status > 0 and chosen_status <= len(order_status):
                sql = f"UPDATE orders SET status_id = {chosen_status} WHERE order_id = {orders[order_update_index][0]}"
                cursor.execute(sql)
                connection.commit()
                print(f"Successfully updated order status to {chosen_status}")
            else:
                print('Order status was not updated!\n')



            print(f'Currently updating selected items: {orders[order_update_index][6]}\n')

            change_items = input("Please enter 'YES' if you would like to choose a new list of items:\n")
            if change_items == "YES":
                print("Please select your items")
                new_products = selecting_product_items(products_list)
                sql = f"UPDATE orders SET items = '{new_products}' WHERE order_id = {orders[order_update_index][0]}"
                cursor.execute(sql)
                connection.commit()
                print(f"Successfully updated items to: {new_products}")
            else:
                print(f"You have chosen to keep your previously selected items!")





############ TESTING Orders fuctions with database ####################

# add_new_order(connect_to_database())

# delete_order(connect_to_database())

#update_order_status(connect_to_database())

update_order(connect_to_database())