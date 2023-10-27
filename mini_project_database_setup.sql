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

SELECT * FROM products;
SELECT * FROM couriers;