#Function to check if user enters a number
def check_input(user_input):

        if user_input.isdigit(): # Confirms if user input is a string that is a number
        # if the option is valid then this will change user input
        # # that was a string into a integer and store it
            user_input = int(user_input)
            return user_input

        else:   # If user enters anything other than a number then outputs
        # the below error message and resends the user back to the main menu
            print("Error: Invalid input, Please enter a valid number from the list!")
            print("\n")

#Function to print all existing orders
def print_orders(orders_list):
    print("Printing all existing orders!\n")
    if orders_list != []:
        for index, orders in enumerate(orders_list):
            print (f"======== Order No. {index+1} ========")
            for key, values in orders.items():
                print(key, ":", values)
        print("=============================")
        print("\n")
    else:
        print("There are no more orders left!")

# function to take users input and turn it into an integer
def input_order():
    chosen_order = input("Please select the ID of the displayed orders above:\n")
    check_input(chosen_order)
    chosen_order = int(chosen_order) - 1
    return chosen_order

# Function to add a new order
def add_new_order(couriers_list):
    print()
    customer_name = input("Please enter your name:\n")
    customer_address =input("Please enter your address:\n")
    customer_number = input("Please enter your phone number:\n")
    for index, courier in enumerate(couriers_list):
        print(index + 1, courier)
    chosen_courier = int(input("Please choose the ID Number of the courier:\n"))
    new_order = {
        "Customer Name": customer_name,
        "Customer Address": customer_address,
        "Phone Number": customer_number,
        "Courier": chosen_courier,
        "Order Status": "Preparing Order"}
    return new_order

# Function to update an existing order
def update_order(orders):
    new_order = []
    chosen_order = input_order()

    for key, value in orders[chosen_order].items():

        print(f"The current {key} is: {value}")
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