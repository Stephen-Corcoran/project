DROP TABLE IF EXISTS manufacturers;
DROP TABLE IF EXISTS products;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    description VARCHAR (255),
    quantity INT,
    buy_price INT,
    sell_price INT
);