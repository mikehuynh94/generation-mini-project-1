
import csv
#Load products csv file
def test_load_products():
    products = []
    with open("test_products.csv", 'r') as file:
        products_data = csv.reader(file, delimiter=",")
        for product, price in products_data:
            #print(f"{product}: {float(price)}")
            products.append({"Name":product,"Price":float(price)})

    print(products)
    return products

#Save into products csv file
def test_save_products(products):
    with open("test_save_products.csv", 'w', newline='') as file:
        writer = csv.writer(file)

        for product_items in products:

            print(product_items['Name'])
            print(product_items['Price'])
            data = product_items['Name'], product_items['Price']
            writer.writerow(data)


#Testing loading csv files
test_load_products()

#Testing saving csv files
test_save_products(test_load_products())

products = test_load_products()

def test_print_products(products):
    print("Printing list of all products in the shop:\n")
    for item in products:
        print(f"{item['Name']}, Price: £{item['Price']}")
    print("")

def test_add_new_product():
    print("Adding a new product")
    new_product_name = input("Enter a product name:\n")
    new_product_price = float(input("Enter the price of the product:\n"))
    new_product_data = {'Name':new_product_name,'Price':new_product_price}
    return new_product_data

def test_update_product(products):
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

def test_delete_product(products):
    print("Please select an ID number from the list below to remove:\n")
    # Prints all the products and their index for the user to choose from
    for item in products:
        # adds 1 to the index as the list starts from 0
        print(f"{str(products.index(item) + 1)}. {item['Name']} Price: £{item['Price']}")
    # Takes users input and -1 to find the product to delete
    product_delete = int(input("Enter here:\n")) - 1
    print(f"Deleting the product: {products[product_delete]}")
    # Removes the product from the list
    return product_delete


#test_print_products(products)

#Testing adding a new product
#products.append(test_add_new_product())
#test_print_products(products)

#Testing update a product
# products = test_update_product(products)
# print(products)

#Testing deleting a product
# products.pop(test_delete_product(products))
# test_print_products(products)