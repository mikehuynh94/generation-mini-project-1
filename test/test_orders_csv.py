import csv
from test_couriers_csv import test_load_couriers
from test_products_csv import test_load_products

#sample structure
# orders_list = [{
#     "Customer Name": "John",
#     "Customer Address": "Unit 2, 12 Main Street, London, WH1 2ER",
#     "Phone Number": "0789887334",
#     "Courier": 2,
#     "Order Status": "Preparing Order",
#     #"Items":"1, 3, 4"
# }]

#Load orders.csv file
def test_load_orders():
    orders = []
    with open("test_orders.csv", 'r') as file:
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
def test_save_orders(orders):
    with open("test_save_orders.csv", 'w', newline='') as file:
        writer = csv.writer(file)

        for order in orders:
            data = [order['Customer Name'], order['Customer Address'], order["Phone Number"], order['Courier'], order['Order Status'], order['Items']]
            writer.writerow(data)

#Testing loading from test_orders.csv
orders = test_load_orders()

#Testing saving into test_save_orders.csv
#test_save_orders(orders)

def check_input(user_input):

        if user_input.isdigit(): # Confirms if user input is a string that is a number
        # if the option is valid then this will change user input
        # # that was a string into a integer and store it
            user_input = int(user_input)
            return user_input

        else:   # If user enters anything other than a number then outputs
        # the below error message and resends the user back to the main menu
            print("Error: Invalid input, a number was not entered!")
            print("\n")
            return -1

def print_all_orders(orders_list):
    print()
    for orders in orders_list:
        for key, values in orders.items():
            print(f"{key}: {values}")
        print("\n")


def print_all_orders_numbered_list(orders_list):
    print("Printing all existing orders!\n")
    if orders_list != []:
        for index, orders in enumerate(orders_list):
            print (f"======================= Order No. {index+1} =======================")
            for key, values in orders.items():
                print(key, ":", values)
        print("===========================================================")
        print("\n")
    else:
        print("There are no more orders left!")


def test_add_new_order(couriers_list, products_list):
    print("Creatinging a new order\n")
    customer_name = input("Please enter your name:\n")
    print("")
    customer_address =input("Please enter your address:\n")
    print("")
    customer_number = input("Please enter your phone number:\n")
    print("")
    for index, courier in enumerate(couriers_list):
        print(f"{index + 1}. {courier['Name']}")
    print("")
    chosen_courier = int(input("Please choose the ID Number of the courier:\n"))
    chosen_products = selecting_product_items(products_list)

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
            print(f"{index + 1}. {item['Name']}")
        print("")
        add_product = check_input(input("Please enter the ID number of the item to add to your order:\n"))

        if (add_product - 1) >= 0 and (add_product - 1) <= len(products_list):
            add_product = str(add_product)
            result = add_product in chosen_products
            if result != True:
                chosen_products += add_product + ","
            else:
                print("This product has already been added to your order!")
                print("Please choose another product")
            if input("Do you wish to add another product to your list (Y/N):\n") != "Y":
                chosen_products = chosen_products[:len(chosen_products)-1]
                return chosen_products
            else:
                continue
        else:
            print("Error you have selected an invalid option!")
            print("Please try again!")
            continue

def test_update_order(orders, couriers_list, products_list):
    new_order = []
    #chosen_order = input_order()
    chosen_order = input("Please select the ID of the displayed orders above:\n")
    check_input(chosen_order)
    chosen_order = int(chosen_order) - 1
    #return chosen_order

    for key, value in orders[chosen_order].items():

        print(f"The current {key} is: {value}")
        if key == 'Courier':
            for index, courier in enumerate(couriers_list):
                print(f"{index + 1}. {courier['Name']}")
            print("")
            new_value = int(input("Please choose the ID Number of the courier:\n"))
            new_order.append({key:new_value})
            orders[chosen_order].update({key:new_value})

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

#Testing printing all orders
#print_all_orders(orders)

#Testing print orders with index
#print_all_orders_numbered_list(orders)

#Testing add new order
#First will need to load products and couriers list
products_list = test_load_products()
couriers = test_load_couriers()
# orders.append(test_add_new_order(couriers, products_list))
# print(orders)

#Testing updating an existing order
print_all_orders_numbered_list(orders)
orders = test_update_order(orders, couriers, products_list)
print(orders)