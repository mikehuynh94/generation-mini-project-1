# Function to print all products and their prices
def print_products(products):
    print("Printing list of all products in the shop:\n")
    for item in products:
        print(f"{item['Name']}: £{item['Price']}")
    print("")

# Function to allow user to add a new product and the price
def add_new_product():
    print("Adding a new product")
    new_product_name = input("Enter a product name:\n")
    new_product_price = float(input("Enter the price of the product:\n"))
    new_product_data = {'Name':new_product_name,'Price':new_product_price}
    return new_product_data

# Function to allow user to edit an existing product
def update_product(products):
    print("Please select an ID number from the list below to update:\n")
    for item in products:
        # adds 1 to the index as the list starts from 0
        print(f"{str(products.index(item) + 1)}. {item['Name']} Price: £{item['Price']}")

    # Takes users input and -1 to find the product to update

    product_edit = int(input("Enter here:\n"))-1

    print(f"Currently editing: {products[product_edit]}")
    # Takes users input to replace the product in the list
    update_product_name = input("Please enter the new product name:\n")
    if update_product_name != "":
        products[product_edit]['Name'] = update_product_name
    update_product_price = input(f"Please enter the new price for {products[product_edit]['Name']}:\n")
    if update_product_price != "":
        try:
            print("working")
            update_product_price = float(update_product_price)
            products[product_edit]['Price'] = update_product_price
        except ValueError:
            print("Error the value was not a price that could be added")
            print("Please try again!")
    return products

# Function to allow user to remove an existing product
def delete_product(products):
    print("Please select an ID number from the list below to remove:\n")
    # Prints all the products and their index for the user to choose from
    for item in products:
        # adds 1 to the index as the list starts from 0
        print(f"{str(products.index(item) + 1)}. {item['Name']} Price: £{item['Price']}")
    # Takes users input and -1 to find the product to delete
    product_delete = int(input("Enter here:\n")) - 1
    if product_delete > 0 and product_delete < len(products):
        print(f"Deleting the product: {products[product_delete]}")
        # Removes the product from the list
        confirmation = input("Please enter DELETE if you would like to continue:\n")
        if confirmation == "DELETE":
            return product_delete
        else:
            print(f"Canceled the deletion of {products[product_delete]}")
            return False
    else:
        print("Error invalid ID number selected")
        print("Please try again!")
        return False