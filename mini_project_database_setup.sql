DROP DATABASE IF EXISTS Mini_Project;
CREATE DATABASE Mini_Project;

USE Mini_Project;

CREATE TABLE products (
  product_id INT NOT NULL AUTO_INCREMENT,
  product_name VARCHAR(25) NOT NULL,
  product_price FLOAT NOT NULL,
  PRIMARY KEY(product_id)
);
CREATE TABLE couriers (
  courier_id INT NOT NULL AUTO_INCREMENT,
  courier_name VARCHAR(25) NOT NULL,
  phone_number VARCHAR(30) NOT NULL,
  PRIMARY KEY(courier_id)
);

CREATE TABLE order_status (
  order_status_id INT NOT NULL AUTO_INCREMENT,
  order_status VARCHAR(25) NOT NULL,
  PRIMARY KEY(order_status_id)
);

INSERT INTO products (product_name, product_price) VALUES ('Apples', 0.55);
INSERT INTO products (product_name, product_price) VALUES ('Oranges', 0.3);
INSERT INTO products (product_name, product_price) VALUES ('Doughnuts', 1);
INSERT INTO products (product_name, product_price) VALUES ('Cherry Bakewells', 2);
INSERT INTO products (product_name, product_price) VALUES ('Biscuits', 1.5);
INSERT INTO products (product_name, product_price) VALUES ('Lucozade', 0.75);
INSERT INTO products (product_name, product_price) VALUES ('Matcha Green Tea Powder', 5.5);

INSERT INTO couriers (courier_name, phone_number) VALUES ('John', '012301230123');
INSERT INTO couriers (courier_name, phone_number) VALUES ('Claire', '1234567890');
INSERT INTO couriers (courier_name, phone_number) VALUES ('Michael', '171717171717');
INSERT INTO couriers (courier_name, phone_number) VALUES ('April', '191919191919');

INSERT INTO order_status (order_status) VALUES ('Preparing');
INSERT INTO order_status (order_status) VALUES ('Ready for Dispatch');
INSERT INTO order_status (order_status) VALUES ('Dispatched');
INSERT INTO order_status (order_status) VALUES ('In Transit');
INSERT INTO order_status (order_status) VALUES ('Delivered');

CREATE TABLE orders (
  order_id INT NOT NULL AUTO_INCREMENT,
  customer_name VARCHAR(25) NOT NULL,
  customer_address VARCHAR(50) NOT NULL,
  phone_number VARCHAR(30) NOT NULL,
  courier_id INT NOT NULL,
  status_id INT NOT NULL,
  items VARCHAR(25) NOT NULL,
  PRIMARY KEY(order_id),
  FOREIGN KEY(courier_id) REFERENCES couriers(courier_id)
  FOREIGN KEY(status_id) REFERENCES order_status(order_status_id)
);

INSERT INTO orders (customer_name, customer_address, phone_number, courier_id, status_id, items) VALUES ('John', 'Unit 2, 12 Main Street, LONDON, WH1 2ER', '876567865', 2, 1, '1,3,4');
INSERT INTO orders (customer_name, customer_address, phone_number, courier_id, status_id, items) VALUES ('Michael', 'My address123123, LONDON, ABC 123', '1717171717', 4, 3, '2,5');
INSERT INTO orders (customer_name, customer_address, phone_number, courier_id, status_id, items) VALUES ('Tim', 'New address 123 abc', '3456764567', 1, 4, '1,4,7');


SELECT * FROM products;
SELECT * FROM couriers;