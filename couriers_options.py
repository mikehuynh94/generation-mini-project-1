def add_couriers():
    new_courier = input("Please enter the new name of the courier you wish to add:\n")
    return new_courier

def update_courier(couriers):
    for index, courier in enumerate(couriers):
        print(f"{index+1}.", courier)
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
    print(f"You are currently updating {couriers[courier_index]}")
    courier_name = input("Please enter the new name below:\n")
    if courier_name != "":
        couriers[courier_index] = courier_name
    else:
        print("No new name has been chosen!")
        print("Returning to previous menu!")
    return couriers

def delete_courier(couriers):
    for index, courier in enumerate(couriers):
        print(f"{index+1}.", courier)
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
    print(f"You have currently selected to remove {couriers[courier_index]}")
    confirmation = input("Please type DELETE to confirm and remove the selected courier:\n")
    if confirmation == "DELETE":
        print(f"Deleting {courier[courier_index]} from the couriers list!")
        couriers.pop(courier_index)
    else:
        print(f"The removal of {couriers[courier_index]} has been cancelled!")
        print("Returning to previous menu!")
    return couriers