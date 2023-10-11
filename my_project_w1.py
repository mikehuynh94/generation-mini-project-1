
products = ['Coke Zero', 'Apples', 'Oranges', 'Doughnuts']


print("Welcome to Mike's Online Supermarket!")
print("=====================================")


main_menu = """
1. Products Menu
0. Exit Application
"""

product_menu = """
1. Show all products
2. Add a new product
3. Update an existing product
4. Delete an existing product
0. Return to main menu
"""


menu = True
p_menu = True

while menu == True:

    print(main_menu)
    # Takes the users input and adds it into a variable
    user_option  = input("Please enter a number option from the list above:\n")

    if user_option.isdigit(): # Confirms if user input is a string that is a number
        # if the option is valid then this will change user input
        # # that was a string into a integer and store it
        user_option = int(user_option)

    else:   # If user enters anything other than a number then outputs
        # the below error message and resends the user back to the main menu
        print("Error: Invalid input, Please enter a valid number from the list!")
        print("\n")
        continue

    if user_option == 0:    # If user selects 0 then the program will terminate
        print("Leaving Mike's Online Supermarket")
        menu = False
        exit()

    elif user_option == 1: # Option for products menu
        p_menu = True
                        # To keep the product menu up
        while p_menu == True: # loops back to product menu whilst p_menu is true

            print(product_menu) # Prints out the product menu options for the user

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
                    print("Printing list of all products in the shop:\n")
                    for a in products:
                        print(a)

                elif user_option == 2: # Upon selecting option 2 this will prompt the user
                                       # to enter a name of a product they wish to add
                    print("Adding a new product to the list")
                    new_product = input("Please enter the name of the product you wish to add:\n")
                    products.append(new_product) # adds the new product to the end of the list

                elif user_option == 3: # Upon selecting option 3
                    print("Please select from the list below the product you want to update:\n")

                    # Prints all the products and their index for the user to choose from
                    for a in products:
                        # adds 1 to the index as the list starts from 0
                        print(str(products.index(a) + 1) + ".", a)

                    # Takes users input and -1 to find the product to update

                    product_edit = int(input("Enter here:\n"))-1

                    print(f"Currently editing: {products[product_edit]}")
                    # Takes users input to replace the product in the list
                    products[product_edit] = input("Please enter the new product name:\n")


                elif user_option == 4: # Upon selecting option 4
                    print("Please select an ID number from the list below to remove:\n")
                    # Prints all the products and their index for the user to choose from
                    for a in products:
                        # adds 1 to the index as the list starts from 0
                        print(str(products.index(a) + 1) + ".", a)
                    # Takes users input and -1 to find the product to delete
                    product_delete = int(input("Enter here:\n")) - 1
                    print(f"Deleting the product: {products[product_delete]}")
                    # Removes the product from the list
                    products.pop(product_delete)

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


    # if the user enters an option that is not within the selected range
    # # then print the error and loop back
    else:
    #elif user_option > 2 or user_option < 0:
        print("This option is not valid please try again!\n")
        #break
        continue