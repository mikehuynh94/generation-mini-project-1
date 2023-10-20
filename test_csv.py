#import my_project_w1
import csv

def test_load_products():
    products = []
    with open("products.csv", 'r') as file:
        products_data = csv.reader(file, delimiter=",")
        for product, price in products_data:
            #print(f"{product}: {float(price)}")
            products.append({"Name":product,"Price":float(price)})

    print(products)
    return products

def test_load_couriers():
    couriers = []
    with open("couriers.csv", 'r') as file:
        couriers_data = csv.reader(file, delimiter=",")
        for courier, phone_number in couriers_data:
            #print(f"{courier}: {float(phone_number)}")
            couriers.append({"Name":courier,"Phone":phone_number})
    print(couriers)

def test_save_products(products):
    with open("test_save_products.csv", 'w', newline='') as file:
        writer = csv.writer(file)

        for product_items in products:
            # print(product_items)
            #for key in product_items:
            print(product_items['Name'])
            print(product_items['Price'])
            data = product_items['Name'], product_items['Price']
            writer.writerow(data)
    return

#test_load_products()

#test_load_couriers()
test_save_products(test_load_products())