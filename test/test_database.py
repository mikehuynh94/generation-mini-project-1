import pymysql

products_list = []
couriers_list = []


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
                # temp = {
                #     'Name':item[1],
                #     'Price':item[2]
                # }
                # products_list.append(temp)
            print()

def add_new_product(connection):
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO products (product_name, product_price) VALUES (%s,%s)"
            product_name = input("Enter the product name for the new record:\n")
            product_price = float(input(f"Enter the price for {product_name}:\n"))
            cursor.execute(sql, (product_name, product_price))
            connection.commit()
########################### COURIERS ###################################

# Print all records from couriers table
def load_couriers_table(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM couriers')
            couriers = cursor.fetchall()
            print('Displaying all records...\n')
            print("Couriers:")
            for courier in couriers:
                print(f"{courier[1]}, Phone: {courier[2]}")
                # temp = {
                #     'Name':courier[1],
                #     'Phone':courier[2]
                # }
                # couriers_list.append(temp)
            print()



load_products_table(connect_to_database())
load_couriers_table(connect_to_database())
add_new_product(connect_to_database())