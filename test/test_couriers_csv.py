import csv

#Load couriers csv file
def test_load_couriers():
    couriers = []
    with open("test_couriers.csv", 'r') as file:
        couriers_data = csv.reader(file, delimiter=",")
        for courier, phone_number in couriers_data:
            #print(f"{courier}: {float(phone_number)}")
            couriers.append({"Name":courier,"Phone":phone_number})
    print(couriers)
    return couriers

#Save into couriers csv file
def test_save_couriers(couriers):
    with open("test_save_couriers.csv", 'w', newline='') as file:
        writer = csv.writer(file)

        for courier in couriers:

            print(courier['Name'])
            print(courier['Phone'])
            data = courier['Name'], courier['Phone']
            writer.writerow(data)

#Testing loading csv files
#test_load_couriers()

#Testing saving csv files
#test_save_couriers(test_load_couriers())

def test_print_couriers(couriers):
    print("Printing all available couriers!\n")
    for person in couriers:
        print(f"{person['Name']}\nContact Number: {person['Phone']}\n")
    print("")

def test_add_new_courier():
    new_courier_name = input("Please enter the new name of the courier you wish to add:\n")
    new_courier_number = input(f"Please enter the phone number to contact {new_courier_name}:\n")
    new_courier = {
        'Name':new_courier_name,
        'Phone':new_courier_number
    }
    return new_courier

def test_update_courier(couriers):
    for index, courier in enumerate(couriers):
        print(f"{index+1}. {courier['Name']}\nPhone: {courier['Phone']}\n")
    courier_check = False
    courier_index = ""
    while courier_check == False:
        courier_index = input("Please select the ID number of the courier to update:\n")
        if courier_index.isdigit() == True:
            courier_index = int(courier_index) - 1
            if courier_index >= 0 and courier_index <= len(couriers):
                courier_check = True
        else:
            print("Error: Invalid Option has been selected!")
            print("Please try again!")
            continue
    print(f"You are currently updating the name for: {couriers[courier_index]['Name']}")
    new_courier_name = input("Please enter the new name below:\n")
    if new_courier_name != "":
        couriers[courier_index]['Name'] = new_courier_name
        print(f"Courier name has been successfully update to: {new_courier_name}")
    else:
        print("Courier name has not been updated!")

    print(f"You are currently updating the contact number for: {couriers[courier_index]['Name']}")
    new_courier_number = input("Please enter the new contact number below:\n")
    if new_courier_number != "":
        couriers[courier_index]['Phone'] = new_courier_number
        print(f"Courier's phone number has been successfully update to: {new_courier_number}")
    else:
        print("Contact number has not been updated!")
    return couriers

def test_delete_courier(couriers):
    for index, courier in enumerate(couriers):
        print(f"{index+1}. {courier['Name']}\nPhone: {courier['Phone']}\n")
    courier_check = False
    courier_index = ""
    while courier_check == False:
        courier_index = input("Please select the ID number of the courier to delete:\n")
        if courier_index.isdigit() == True:
            courier_index = int(courier_index) - 1
            if courier_index >= 0 and courier_index <= len(couriers):
                courier_check = True
        else:
            print("Error: Invalid Option has been selected!")
            print("Please try again!")
            continue

    print(f"You have currently selected to remove {couriers[courier_index]['Name']}: {couriers[courier_index]['Phone']}")
    confirmation = input("Please type DELETE to confirm and remove the selected courier:\n")
    if confirmation == "DELETE":
        print(f"Deleting {couriers[courier_index]['Name']} from the couriers list!")
        couriers.pop(courier_index)
    else:
        print(f"The removal of {couriers[courier_index]['Name']} has been cancelled!")
        print("Returning to previous menu!")
    return couriers

couriers = test_load_couriers()

#Testing to print all couriers from CSV file
#test_print_couriers(couriers)

#Testing to add a new courier to the list
#couriers.append(test_add_new_courier())
#print(couriers)

#Testing to update an existing courier
# couriers = test_update_courier(couriers)
# print(couriers)

#Testing to delete an existing courier
#test_delete_courier(couriers)
#print(couriers)