def check_input(user_input):

        if user_input.isdigit(): # Confirms if user input is a string that is a number
        # if the option is valid then this will change user input
        # # that was a string into a integer and store it
            user_input = int(user_input)
            return user_input

        else:   # If user enters anything other than a number then outputs
        # the below error message and resends the user back to the main menu
            # print("Error: Invalid input, a number was not entered!")
            # print("\n")
            return -1

# Function to test for non numeric string
def mock_non_number():
    #Arrange
    data = "ABC"
    expected = -1

    #Act
    actual = check_input(data)

    #Assert
    assert expected == actual

mock_non_number()

# Function to test for numeric string to change to integer
def mock_string_to_int():
    #Arrange
    data = "5"
    expected = 5

    #Act
    actual = check_input(data)

    #Assert
    assert expected == actual

mock_string_to_int()

# Test sorting list

def sort_orders(orders_list, sort):

    #sort_choice = input("Please choose if you would like to sort orders by 'Status' or 'Courier':\n")
    sort_choice = sort
    if sort_choice == "Status":
        #print("")
        orders_list = sorted(orders_list, key=lambda o: o[5])
        #print("Sorted orders by: Order Status\n")
    elif sort_choice == 'Courier':
        #print("")
        orders_list = sorted(orders_list, key=lambda o: o[4])
        #print("Sorted orders by: Courier\n")
    else:
    #     #print("Error with sort choice")
    #     #print("Printing all orders list unsorted!\n")
        print("")

    return orders_list

#Test to sort by status which is the 6th element of the tuples from the list
def sort_by_status():
    #Arrange
    data = [(1,'a','b','c',3,5),(2,'aa','bb','cc',1,6),(3,'aaa','bbb','ccc',2,4)]
    sort = 'Status'
    expected = [(3,'aaa','bbb','ccc',2,4),(1,'a','b','c',3,5),(2,'aa','bb','cc',1,6)]

    #Act
    actual = sort_orders(data, sort)

    #Assert
    assert expected == actual

sort_by_status()

#Test to sort by status which is the 5th element of the tuples from the list
def sort_by_courier():
    #Arrange
    data = [(1,'a','b','c',3,5),(2,'aa','bb','cc',1,6),(3,'aaa','bbb','ccc',2,4)]
    sort = 'Courier'
    expected = [(2,'aa','bb','cc',1,6), (3,'aaa','bbb','ccc',2,4),(1,'a','b','c',3,5)]

    #Act
    actual = sort_orders(data, sort)

    #Assert
    assert expected == actual

sort_by_courier()

#Test to return unsorted list for no empty string
def unsorted_empty():
    #Arrange
    data = [(1,'a','b','c',3,5),(2,'aa','bb','cc',1,6),(3,'aaa','bbb','ccc',2,4)]
    sort = ''
    expected = [(1,'a','b','c',3,5),(2,'aa','bb','cc',1,6),(3,'aaa','bbb','ccc',2,4)]

    #Act
    actual = sort_orders(data, sort)

    #Assert
    assert expected == actual

unsorted_empty()

#Test to return unsorted list for input other than Courier or Status
def unsorted_invalid():
    #Arrange
    data = [(1,'a','b','c',3,5),(2,'aa','bb','cc',1,6),(3,'aaa','bbb','ccc',2,4)]
    sort = 'asdglhsfkgjs'
    expected = [(1,'a','b','c',3,5),(2,'aa','bb','cc',1,6),(3,'aaa','bbb','ccc',2,4)]

    #Act
    actual = sort_orders(data, sort)

    #Assert
    assert expected == actual

unsorted_invalid()