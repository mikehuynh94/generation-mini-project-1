import csv

#sample structure
# orders_list = [{
#     "Customer Name": "John",
#     "Customer Address": "Unit 2, 12 Main Street, London, WH1 2ER",
#     "Phone Number": "0789887334",
#     "Courier": 2,
#     "Order Status": "Preparing Order",
#     #"Items":"1, 3, 4"
# }]

#Load orders.csv file
def test_load_orders():
    orders = []
    with open("test_orders.csv", 'r') as file:
        orders_data = csv.reader(file, delimiter=",")
        for order in orders_data:
            temp = {
                'Customer Name':order[0],
                'Customer Address':order[1],
                'Phone Number':order[2],
                'Courier':order[3],
                'Order Status':order[4],
                'Items':order[5]}
            orders.append(temp)
    #print(orders)
    return orders

#Save into couriers csv file
def test_save_orders(orders):
    with open("test_save_orders.csv", 'w', newline='') as file:
        writer = csv.writer(file)

        for order in orders:
            data = [order['Customer Name'], order['Customer Address'], order["Phone Number"], order['Courier'], order['Order Status'], order['Items']]

            writer.writerow(data)

#Testing loading from test_orders.csv
orders = test_load_orders()

#Testing saving into test_save_orders.csv
test_save_orders(orders)