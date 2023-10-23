import orders_options as option
import couriers_options
import products_options
import lists

#   Loading lists from csv files
products = lists.load_products()
# TODO change from loading txt to load from csv
couriers = lists.load_couriers()

orders_list = [{
    "Customer Name": "John",
    "Customer Address": "Unit 2, 12 Main Street, London, WH1 2ER",
    "Phone Number": "0789887334",
    "Courier": 2,
    "Order Status": "Preparing Order",
    #"Items":"1, 3, 4"
}]


print("Welcome to Mike's Online Supermarket!")
print("=====================================")


main_menu_options = """
===================
==== Main Menu ====
===================

1. Products Menu
2. Couriers Menu
3. Orders Menu
0. Exit Application
"""

product_menu_options = """
=====================
=== Products Menu ===
=====================

1. Show all products
2. Add a new product
3. Update an existing product
4. Delete an existing product
0. Return to main menu
"""

courier_menu_options = """
=====================
=== Couriers Menu ===
=====================

1. Show all couriers
2. Add new courier
3. Update an existing courier
4. Delete Courier
0. Return to main menu
"""

order_menu_options = """
===================
=== Orders Menu ===
===================

1. Print order history
2. Create a new order
3. Update an existing order status
4. Update an existing order
5. Delete an order
0. Return to main menu
"""

menu = True
p_menu = True
o_menu = True
c_menu = True

while menu == True:

    print(main_menu_options)
    # Takes the users input and adds it into a variable

    user_option = input("Please enter a number option from the list above:\n")

    # Function to check user input if it can be turned into an integer
    user_option = option.check_input(user_option)

    if user_option == 0:    # If user selects 0 then the program will terminate
        print("Leaving Mike's Online Supermarket")
        menu = False
        lists.save_products(products)
        lists.save_couriers(couriers)
        exit()

    elif user_option == 1: # Option for products menu
        p_menu = True

        while p_menu == True: # loops back to product menu whilst p_menu is true

            print(product_menu_options) # Prints out the product menu options for the user

            user_option  = input("Please enter a number option from the list above:\n")
            # Confirms if user input is a string that is a number
            if user_option.isdigit():
                # if the option is valid then this will change user input
                # that was a string into a number
                user_option = int(user_option)

                if user_option == 0:
                    print("Returning to main menu please wait!")
                    p_menu = False # Upon selecting option 0 to return to the main menu then p_menu becomes false to end the loop
                    #break
                    continue

                elif user_option == 1: # Upon selecting option 1 the system will print all the items in products

                    products_options.print_products(products)

                elif user_option == 2: # Upon selecting option 2 this will prompt the user
                                       # to enter a name of a product they wish to add

                    products.append(products_options.add_new_product())

                elif user_option == 3: # Upon selecting option 3

                    products = products_options.update_product(products)

                elif user_option == 4: # Upon selecting option 4
                    remove_product = products_options.delete_product(products)
                    if remove_product != False:
                        products.pop(remove_product)

                # if the user enters an option that is not within the selected range
                # # then print the error and loop
                else:
                #elif user_option > 4 or user_option < 0:
                    print("This option is not valid please try again!\n")
                    #break
                    continue

            else: # If user enters anything other than a number then outputs
                # the below error message and resends the user back to the main menu
                print("Error: Invalid input, Please enter a valid number from the list!\n")
                #break
                continue

    elif user_option == 2: # Option of couriers menu
        c_menu = True
        while c_menu == True:
            print(courier_menu_options)
            user_option  = input("Please enter a number option from the list above:\n")
            if user_option.isdigit(): # Confirms if user input is a string that is a number
                # Confirms if user input is a string that is a number
                user_option = int(user_option)

                # Option to return to main menu
                if user_option == 0:
                    print("Returning to main menu please wait!\n")
                    # Upon selecting option 0 to return to the
                    # main menu then o_menu becomes false to end the loop
                    c_menu = False

                elif user_option == 1: # Option to print all couriers
                    print("Printing all available couriers!")
                    for person in couriers:
                        print(person)

                elif user_option == 2: # Option to add a new courier
                    print("Creating a new courier!")
                    couriers.append(couriers_options.add_couriers())

                elif user_option == 3: # Option to update an existing courier
                    print("Updating an existing courier!")
                    couriers = couriers_options.update_courier(couriers)

                elif user_option == 4: # Option to delete an existing courier
                    print("Deleting an existing courier")
                    couriers = couriers_options.delete_courier(couriers)

                else:
                # if the user enters an option that is not within the selected range
                # # then print the error and loop
                    print("This option is not valid please try again!\n")

            else:
                print("This option is not valid please try again!\n")
                #continue
                #break


    elif user_option == 3: # Option for orders menu
        o_menu = True

        while o_menu == True:
            print(order_menu_options)

            user_option  = input("Please enter a number option from the list above:\n")
            if user_option.isdigit(): # Confirms if user input is a string that is a number
                # Confirms if user input is a string that is a number
                user_option = int(user_option)

                # Option to return to main menu
                if user_option == 0:
                    print("Returning to main menu please wait!\n")
                    # Upon selecting option 0 to return to the
                    # main menu then o_menu becomes false to end the loop
                    o_menu = False


                elif user_option == 1: # Option to print all orders
                    print()
                    for orders in orders_list:
                        for key, values in orders.items():
                            print(key, ":", values)

                        print("\n")

                elif user_option == 2: # Option to add an order
                    print("Creating a new order!")

                    orders_list.append(option.add_new_order(couriers))

                elif user_option == 3: # Option to update an existing order's status
                    print("Updating Status")

                    print("choose an order to update the status of below:")

                    option.print_orders(orders_list)
                    option.update_order_status(orders_list)



                elif user_option == 4: # Option to update an existing order
                    print("Update an order")

                    option.print_orders(orders_list)
                    option.update_order(orders_list)


                elif user_option == 5: # Option to delete an existing order
                    print("Delete an existing order!")
                    option.print_orders(orders_list)
                    option.delete_order(orders_list)

                else:
                # if the user enters an option that is not within the selected range
                # # then print the error and loop
                    print("This option is not valid please try again!\n")

            else:
                print("This option is not valid please try again!\n")
                #continue
                #break

    # if the user enters an option that is not within the selected range
    # # print the error and loop back
    else:
    # elif user_option > 3 or user_option < 0:
        print("This option is not valid please try again!\n")
        #break
        continue
