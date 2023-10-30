import pymysql

# Connecting to database
def connect_to_database():
    connection = pymysql.connect(
                host='localhost', database='Mini_Project',
                user='root', password='password'
            )
    return connection

####################### PRODUCTS ###############################

# Print all records from products table
def print_all_products(connection):
    with connection:
        with connection.cursor() as cursor:

            cursor.execute('SELECT * FROM products')
            products = cursor.fetchall()
            print('Displaying all records...\n')
            print("Products")
            for item in products:
                print(f"{item[1]}, Price: £{item[2]}")
            print()

def show_index_products(products):
    print('Displaying all records...\n')
    print("Products")
    for index, item in enumerate(products):
        print(f"{index + 1}. {item[1]}, Price: £{item[2]}")
    print()

def test_add_new_product(connection):
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO products (product_name, product_price) VALUES (%s,%s)"
            product_name = input("Enter the product name for the new record:\n")
            product_price = float(input(f"Enter the price for {product_name}:\n"))
            cursor.execute(sql, (product_name, product_price))
            connection.commit()

def update_product(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM products')
            products = cursor.fetchall()
            show_index_products(products)

            print("Please select an ID number from the list above to update:\n")
            try:
                product_edit = int(input("Enter here:\n"))-1
            except ValueError as e:
                print("Error input was not a number,", e)
                product_edit = -1


            if product_edit >= 0 and product_edit <= len(products):
                print(f"\nCurrently editing: {products[product_edit][1]}")
                update_product_name = input("Please enter the new product name:\n")
                if update_product_name != "":

                    sql = f"UPDATE products SET product_name = '{update_product_name}' WHERE product_id = {products[product_edit][0]}"
                    cursor.execute(sql)
                    print()
                update_product_price = input(f"Please enter the new price for {products[product_edit][2]}:\n")
                if update_product_price != "":
                    try:
                        update_product_price = float(update_product_price)

                    except ValueError:
                        print("Error the value was not a price that could be added")
                        print("Please try again!")

                    sql = f"UPDATE products SET product_price = {update_product_price} WHERE product_id = {products[product_edit][0]}"
                    cursor.execute(sql)
            else:
                print("Error invalid ID number selected")
                print("Please try again!")
                return False

            connection.commit()


def delete_product(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM products')
            products = cursor.fetchall()
            show_index_products(products)

            print("Please select an ID number from the list above to delete:\n")
            try:
                product_delete = int(input("Enter here:\n"))-1
            except ValueError as e:
                print("Error input was not a number,", e)
                product_delete = -1


            if product_delete >= 0 and product_delete <= len(products):
                print("\nCurrently selected for deletion:\nRecord from products database:")
                print(f"{products[product_delete][0]}. {products[product_delete][1]}: £{products[product_delete][2]}\n")
                confirmation = input("Please enter DELETE if you would like to continue:\n")
                if confirmation == "DELETE":
                    print("Deleted:", products[product_delete])
                    sql = f"DELETE FROM products where product_id = {products[product_delete][0]}"
                    cursor.execute(sql)
                    connection.commit()
                else:
                    print(f"Canceled the deletion of {products[product_delete]}")


##################### Function call to test products table ########################

#Function to test print all product records from database
#load_products_table(connect_to_database())


#Test add new product and store it inside the database
#test_add_new_product(connect_to_database())

#Test update a product from database
#update_product(connect_to_database())

#Test deleting a product record from database
#delete_product(connect_to_database())

########################### COURIERS ##############################################

# Print all records from couriers table
def print_couriers(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM couriers')
            couriers = cursor.fetchall()
            print('Displaying all records...\n')
            print("Couriers:")
            for courier in couriers:
                print(f"{courier[1]}, Phone: {courier[2]}")
            print()


def show_index_couriers(couriers):
    print('Displaying all records...\n')
    print("Couriers")
    for index, courier in enumerate(couriers):
        print(f"{index + 1}. {courier[1]}, Phone: {courier[2]}")
    print()

def test_add_new_courier(connection):
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO couriers (courier_name, phone_number) VALUES (%s,%s)"
            courier_name = input("Enter the courier name for the new record:\n")
            phone_number = (input(f"Enter the contact number for {courier_name}:\n"))
            cursor.execute(sql, (courier_name, phone_number))
            connection.commit()

def test_update_courier(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM couriers')
            couriers = cursor.fetchall()
            show_index_couriers(couriers)

            print("Please select an ID number from the list above to update:\n")
            try:
                courier_edit = int(input("Enter here:\n"))-1
            except ValueError as e:
                print("Error input was not a number,", e)
                courier_edit = -1


            if courier_edit >= 0 and courier_edit <= len(couriers):
                print(f"\nCurrently editing: {couriers[courier_edit][1]}")
                update_courier_name = input("Please enter the new courier name:\n")
                if update_courier_name != "":

                    sql = f"UPDATE couriers SET courier_name = '{update_courier_name}' WHERE courier_id = {couriers[courier_edit][0]}"
                    cursor.execute(sql)
                    print()
                update_phone_number = input(f"Please enter the new price for {couriers[courier_edit][2]}:\n")
                if update_phone_number != "":
                    sql = f"UPDATE couriers SET phone_number = {update_phone_number} WHERE courier_id = {couriers[courier_edit][0]}"
                    cursor.execute(sql)
            else:
                print("Error invalid ID number selected")
                print("Please try again!")
                return False
            connection.commit()

def delete_courier(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM couriers')
            couriers = cursor.fetchall()
            show_index_couriers(couriers)

            print("Please select an ID number from the list above to delete:\n")
            try:
                courier_delete = int(input("Enter here:\n"))-1
            except ValueError as e:
                print("Error input was not a number,", e)
                courier_delete = -1


            if courier_delete >= 0 and courier_delete <= len(couriers):
                print("\nCurrently selected for deletion:\nRecord from couriers database:")
                print(f"{couriers[courier_delete][0]}. {couriers[courier_delete][1]}, Phone: {couriers[courier_delete][2]}\n")
                confirmation = input("Please enter DELETE if you would like to continue:\n")
                if confirmation == "DELETE":
                    print("Deleted:", couriers[courier_delete])
                    sql = f"DELETE FROM couriers where courier_id = {couriers[courier_delete][0]}"
                    cursor.execute(sql)
                    connection.commit()
                else:
                    print(f"Canceled the deletion of {couriers[courier_delete]}")

##################### Function call to test couriers table ########################

#Function to test print all courier records from database
#load_couriers_table(connect_to_database())

#Function to add new courier into database
#test_add_new_courier(connect_to_database())

#Function to update an existing courier from the database
#test_update_courier(connect_to_database())

#Function to dlete an existing courier from the database
#delete_courier(connect_to_database())

########################### WEEK 5 Update to Orders ###############################

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
            #show_index_products(products)
            chosen_products = selecting_product_items(products)
        new_order = {
            "Customer Name": customer_name,
            "Customer Address": customer_address,
            "Phone Number": customer_number,
            "Courier": chosen_courier,
            "Items": chosen_products,
            "Order Status": "Preparing Order"}

    return new_order


def selecting_product_items(products_list):
    chosen_products = ""
    while True:
        print("")
        for index, item in enumerate(products_list):
            print(f"{index + 1}. {item[1]}")
        print("")
        add_product = int(input("Please enter the ID number of the item to add to your order:\n"))

        if (add_product - 1) >= 0 and (add_product - 1) <= len(products_list):
            add_product = str(add_product)
            result = add_product in chosen_products
            if result != True:
                chosen_products += add_product + ","
            else:
                print("This product has already been added to your order!")
                print("Please choose another product")
            if input("Do you wish to add another product to your list, Please enter 'YES' to continue:\n") != "YES":
                chosen_products = chosen_products[:len(chosen_products)-1]
                return chosen_products
            else:
                continue
        else:
            print("Error you have selected an invalid option!")
            print("Please try again!")
            continue


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


order = []
order.append(add_new_order(connect_to_database()))

update_order(order, connect_to_database())