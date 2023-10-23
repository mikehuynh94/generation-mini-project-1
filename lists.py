import csv
#Function to read from products csv file and save the products to a list
def load_products():
    # products_list = []
    # filepath = ("products.txt")
    # contents = open(filepath, "r")
    # lines = contents.readlines()

    # for product in lines:
    #     products_list.append(product.strip())
    # contents.close()
    # return products_list
    products = []
    with open("products.csv", 'r') as file:
        products_data = csv.reader(file, delimiter=",")
        for product, price in products_data:
            #print(f"{product}: {float(price)}")
            products.append({"Name":product,"Price":float(price)})

    print(products)
    return products

#Function to read from couriers text file and save the couriers to a list
def load_couriers():
    courier_list = []

    filepath = ("couriers.txt")

    contents = open(filepath, "r")

    lines = contents.readlines()

    for courier in lines:
        courier_list.append(courier.strip())
    contents.close()
    return courier_list


# Function that takes the products list as an argument
# and writes over the products csv file with the products from the list
# to update and save the changes
def save_products(products):
    # filepath = ("products.txt")
    # save_products_file = open(filepath, "w")
    # for product in products:
    #     save_products_file.write(product + "\n")
    # save_products_file.close()

    with open("products.csv", 'w', newline='') as file:
        writer = csv.writer(file)

        for product_items in products:

            # print(product_items['Name'])
            # print(product_items['Price'])
            data = product_items['Name'], product_items['Price']
            writer.writerow(data)

# Function that takes the couriers list as an argument
# and writes over the couriers text file with the couriers from the list
# to update and save the changes
def save_couriers(couriers):
    filepath = ("couriers.txt")
    save_couriers_file = open(filepath, "w")
    for courier in couriers:
        save_couriers_file.write(courier + "\n")
    save_couriers_file.close()