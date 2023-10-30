#Function to print all couriers from list
def print_couriers(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM couriers')
            couriers = cursor.fetchall()
            print('Displaying all records...\n')
            print("Couriers:")
            for courier in couriers:
                print(f"{courier[1]}, Phone: {courier[2]}")
            print()


def show_index_couriers(couriers):
    print('Displaying all records...\n')
    print("Couriers")
    for index, courier in enumerate(couriers):
        print(f"{index + 1}. {courier[1]}, Phone: {courier[2]}")
    print()

#Function to add a new courier to the list
def add_new_courier(connection):
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO couriers (courier_name, phone_number) VALUES (%s,%s)"
            courier_name = input("Enter the courier name for the new record:\n")
            phone_number = (input(f"Enter the contact number for {courier_name}:\n"))
            cursor.execute(sql, (courier_name, phone_number))
            connection.commit()

#Function to update an existing courier
def update_courier(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM couriers')
            couriers = cursor.fetchall()
            show_index_couriers(couriers)

            print("Please select an ID number from the list above to update:\n")
            try:
                courier_edit = int(input("Enter here:\n"))-1
            except ValueError as e:
                print("Error input was not a number,", e)
                courier_edit = -1


            if courier_edit >= 0 and courier_edit <= len(couriers):
                print(f"\nCurrently editing: {couriers[courier_edit][1]}")
                update_courier_name = input("Please enter the new courier name:\n")
                if update_courier_name != "":

                    sql = f"UPDATE couriers SET courier_name = '{update_courier_name}' WHERE courier_id = {couriers[courier_edit][0]}"
                    cursor.execute(sql)
                    print()
                update_phone_number = input(f"Please enter the new price for {couriers[courier_edit][2]}:\n")
                if update_phone_number != "":
                    sql = f"UPDATE couriers SET phone_number = {update_phone_number} WHERE courier_id = {couriers[courier_edit][0]}"
                    cursor.execute(sql)
            else:
                print("Error invalid ID number selected")
                print("Please try again!")
                return False
            connection.commit()

#Function to delete a courier from the couriers list
def delete_courier(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM couriers')
            couriers = cursor.fetchall()
            show_index_couriers(couriers)

            print("Please select an ID number from the list above to delete:\n")
            try:
                courier_delete = int(input("Enter here:\n"))-1
            except ValueError as e:
                print("Error input was not a number,", e)
                courier_delete = -1


            if courier_delete >= 0 and courier_delete <= len(couriers):
                print("\nCurrently selected for deletion:\nRecord from couriers database:")
                print(f"{couriers[courier_delete][0]}. {couriers[courier_delete][1]}, Phone: {couriers[courier_delete][2]}\n")
                confirmation = input("Please enter DELETE if you would like to continue:\n")
                if confirmation == "DELETE":
                    print("Deleted:", couriers[courier_delete])
                    sql = f"DELETE FROM couriers where courier_id = {couriers[courier_delete][0]}"
                    cursor.execute(sql)
                    connection.commit()
                else:
                    print(f"Canceled the deletion of {couriers[courier_delete]}")