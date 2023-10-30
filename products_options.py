# Function to print all products and their prices
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

# Function to allow user to add a new product and the price
def add_new_product(connection):
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO products (product_name, product_price) VALUES (%s,%s)"
            product_name = input("Enter the product name for the new record:\n")
            product_price = float(input(f"Enter the price for {product_name}:\n"))
            cursor.execute(sql, (product_name, product_price))
            connection.commit()

# Function to allow user to edit an existing product
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



# Function to allow user to remove an existing product
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