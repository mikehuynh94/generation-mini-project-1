

def load_products():
    products_list = []
    filepath = (r"C:\Users\Mike\Desktop\Python\Data Engineering Python Practice\project\\generation-mini-project-1\\products.txt")
    contents = open(filepath, "r")
    lines = contents.readlines()

    for product in lines:
        products_list.append(product.strip())
    contents.close()
    return products_list


def load_couriers():
    courier_list = []

    filepath = (r"C:\Users\Mike\Desktop\Python\Data Engineering Python Practice\project\\generation-mini-project-1\\couriers.txt")

    contents = open(filepath, "r")

    lines = contents.readlines()

    for courier in lines:
        courier_list.append(courier.strip())
    contents.close()
    return courier_list


def save_products(products):
    filepath = (r"C:\Users\Mike\Desktop\Python\Data Engineering Python Practice\project\\generation-mini-project-1\\products.txt")
    save_products_file = open(filepath, "w")
    for product in products:
        save_products_file.write(product + "\n")
    save_products_file.close()

def save_couriers(couriers):
    filepath = (r"C:\Users\Mike\Desktop\Python\Data Engineering Python Practice\project\\generation-mini-project-1\\couriers.txt")
    save_couriers_file = open(filepath, "w")
    for courier in couriers:
        save_couriers_file.write(courier + "\n")
    save_couriers_file.close()