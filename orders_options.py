#Function to check if user enters a number
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

def sort_orders(orders_list):
    sort_choice = input("Please choose if you would like to sort orders by 'Status' or 'Courier':\n")
    if sort_choice == "Status":
        print("")
        orders_list.sort(key=lambda o: o['Order Status'])
        print("Sorted orders by: Order Status\n")
    elif sort_choice == 'Courier':
        print("")
        orders_list.sort(key=lambda o: int(o['Courier']))
        print("Sorted orders by: Courier\n")
    else:
        print("Error with sort choice")
        print("Printing all orders list unsorted!\n")
    return orders_list

#Function to print all orders and sort by status or couriers
def print_all_orders(orders_list):
    print()

    orders_list = sort_orders(orders_list)

    for orders in orders_list:
        for key, values in orders.items():
            print(f"{key}: {values}")
        print("\n")

#Function to print all existing orders
def print_orders_with_index(orders_list):
    print("Printing all existing orders!\n")
    if orders_list != []:

        orders_list = sort_orders(orders_list)

        for index, orders in enumerate(orders_list):
            print (f"======================= Order No. {index+1} =======================")
            for key, values in orders.items():
                print(key, ":", values)
        print("===========================================================")
        print("\n")
    else:
        print("There are no more orders left!")

# function to take users input and turn it into an integer
def input_order():
    while True:
        try:
            chosen_order = input("Please select the ID of the displayed orders above:\n")
            check_input(chosen_order)
            chosen_order = int(chosen_order) - 1
            break
        except ValueError as e:
            print("Error invalid input")
            print("Please try again!")
    return chosen_order

# Function to add a new order
def add_new_order(couriers_list, products_list):

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

#Function that prints the index of items and allows user to selects multiple items to add
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
            if input("Do you wish to add another product to your list, Please enter 'YES' to continue:\n") != "YES":
                chosen_products = chosen_products[:len(chosen_products)-1]
                return chosen_products
            else:
                continue
        else:
            print("Error you have selected an invalid option!")
            print("Please try again!")
            continue

# Function to update an existing order
def update_order(orders, couriers_list, products_list):
    new_order = []
    chosen_order = input_order()

    for key, value in orders[chosen_order].items():

        print(f"The current {key} is: {value}")
        if key == 'Courier':
            for index, courier in enumerate(couriers_list):
                print(f"{index + 1}. {courier['Name']}")
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

# Function to update just the status of an existing order
def update_order_status(orders):
    chosen_order = input_order()
    print("You have chosen the following order:")

    for key in orders[chosen_order]:
        print(orders[chosen_order][key])
    print("\n")

    status_update = input("Please enter the new status below:\n")

    orders[chosen_order]['Order Status'] = status_update
    print(orders[chosen_order])

# Function to delete an existing order
def delete_order(orders):
    print("")
    chosen_order = input_order()
    print("You have chosen the following order:")

    for key in orders[chosen_order]:
        print(orders[chosen_order][key])
    print("\n")

    confirmation = input("Please confirm if you wish to delete this order by typing 'DELETE' below:\n")
    if confirmation == "DELETE":
        orders.pop(chosen_order)
        print(orders)
    else:
        print("Deletion of order has been cancelled!")
        print("Returning to previous menu!")