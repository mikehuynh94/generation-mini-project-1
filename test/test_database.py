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
def load_products_table(connection):
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
def print_couriers_table(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM couriers')
            couriers = cursor.fetchall()
            print('Displaying all records...\n')
            print("Couriers:")
            for courier in couriers:
                print(f"{courier[1]}, Phone: {courier[2]}")
            print()

# def load_couriers_table(connection):
#     with connection:
#         with connection.cursor() as cursor:
#             couriers_list = []
#             cursor.execute('SELECT * FROM couriers')
#             couriers = cursor.fetchall()
#             print('Displaying all records...\n')
#             print("Couriers:")
#             for courier in couriers:
#                 print(f"{courier[1]}, Phone: {courier[2]}")
#                 temp = {
#                     'Name'
#                 }
#             print()

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

    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM couriers')
            couriers = cursor.fetchall()
            show_index_couriers(couriers)


    chosen_courier = int(input("Please choose the ID Number of the courier:\n")) - 1

    check_courier = couriers[chosen_courier] in couriers
    
    #chosen_products = selecting_product_items(products_list)

    new_order = {
        "Customer Name": customer_name,
        "Customer Address": customer_address,
        "Phone Number": customer_number,
        "Courier": chosen_courier,
        #"Items": chosen_products,
        "Order Status": "Preparing Order"}
    return new_order

add_new_order(connect_to_database())