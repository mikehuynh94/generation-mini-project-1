
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

def print_orders(orders_list):
    print("Printing all existing orders!\n")
    if orders_list != []:
        count = 0
        for orders in orders_list:
            count += 1
            # print("Orders is:", orders)
            print (f"======== Order No. {count} ========")
            #temp_list.append({count:orders})
            for key, values in orders.items():
                print(key, ":", values)

        print("=============================")
        print("\n")
    else:
        print("There are no more orders left!")

def input_order():
    chosen_order = input("Please select the ID of the displayed orders above:\n")
    chosen_order = int(chosen_order) - 1
    return chosen_order

def add_new_order():
    print()
    customer_name = input("Please enter your name:\n")
    customer_address =input("Please enter your address:\n")
    customer_number = input("Please enter your phone number:\n")
    new_order = {
        "Customer Name": customer_name,
        "Customer Address": customer_address,
        "Phone Number": customer_number,
        "Order Status": "Preparing Order"}
    return new_order

#def update_order(orders, items):
def update_order(orders):
    new_order = []
    chosen_order = input_order()

    for key, value in orders[chosen_order].items():
        #print(f"This orders key is: {key}\nThis orders Value is: {value}")
        print(f"The current {key} is: {value}")
        new_value = input(f"Please enter the new value for {key}:\n")
        if new_value != "":

            new_order.append({key:new_value})
            #print(new_order)
            #update_order = {key:new_value}
            orders[chosen_order].update({key:new_value})
            #print(orders)
            #orders[chosen_order - 1] = new_order
            #orders.update(new_order)
            #orders[chosen_order] = new_order
        else:
            continue

    #print(orders)
    return orders

def update_order_status(orders):
    chosen_order = input_order()
    print("You have chosen the following order:")

    for key in orders[chosen_order]:
        print(orders[chosen_order][key])
    print("\n")

    status_update = input("Please enter the new status below:\n")

    orders[chosen_order]['Order Status'] = status_update
    print(orders[chosen_order])

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