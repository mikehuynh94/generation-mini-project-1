

def load_products():
    products_list = []
    filepath = ("products.txt")
    contents = open(filepath, "r")
    lines = contents.readlines()

    for product in lines:
        products_list.append(product.strip())
    contents.close()
    return products_list


def load_couriers():
    courier_list = []

    filepath = ("couriers.txt")

    contents = open(filepath, "r")

    lines = contents.readlines()

    for courier in lines:
        courier_list.append(courier.strip())
    contents.close()
    return courier_list


def save_products(products):
    filepath = ("products.txt")
    save_products_file = open(filepath, "w")
    for product in products:
        save_products_file.write(product + "\n")
    save_products_file.close()

def save_couriers(couriers):
    filepath = ("couriers.txt")
    save_couriers_file = open(filepath, "w")
    for courier in couriers:
        save_couriers_file.write(courier + "\n")
    save_couriers_file.close()