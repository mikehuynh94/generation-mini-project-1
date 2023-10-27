import csv

#Function to read from products.csv file and save the products to a list
def load_products():
    products = []
    with open("products.csv", 'r') as file:
        products_data = csv.reader(file, delimiter=",")
        for product, price in products_data:
            products.append({"Name":product,"Price":float(price)})
    return products

#Function to read from couriers.csv file and save the couriers to a list
def load_couriers():
    couriers = []
    with open("couriers.csv", 'r') as file:
        couriers_data = csv.reader(file, delimiter=",")
        for courier, phone_number in couriers_data:
            couriers.append({"Name":courier,"Phone":phone_number})
    return couriers


# Function that takes the products list as an argument
# and writes over the products csv file with the products from the list
# to update and save the changes
def save_products(products):
    with open("products.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for product_items in products:
            data = product_items['Name'], product_items['Price']
            writer.writerow(data)


# Function that takes the couriers list as an argument
# and writes over the couriers text file with the couriers from the list
# to update and save the changes
def save_couriers(couriers):
    with open("couriers.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for courier in couriers:
            data = courier['Name'], courier['Phone']
            writer.writerow(data)

#Load orders.csv file
def load_orders():
    orders = []
    with open("orders.csv", 'r') as file:
        orders_data = csv.reader(file, delimiter=",")
        for order in orders_data:
            temp = {
                'Customer Name':order[0],
                'Customer Address':order[1],
                'Phone Number':order[2],
                'Courier':order[3],
                'Order Status':order[4],
                'Items':order[5]}
            orders.append(temp)
    #print(orders)
    return orders

#Save into orders csv file
def save_orders(orders):
    with open("orders.csv", 'w', newline='') as file:
        writer = csv.writer(file)

        for order in orders:
            data = [order['Customer Name'], order['Customer Address'], order["Phone Number"], order['Courier'], order['Order Status'], order['Items']]
            writer.writerow(data)