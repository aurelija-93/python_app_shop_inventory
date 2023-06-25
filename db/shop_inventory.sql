DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS suppliers;

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    stock INT,
    purchase_price INT,
    selling_price INT,
    margin INT,
    supplier_id INT NOT NULL REFERENCES suppliers(id) ON DELETE CASCADE
);