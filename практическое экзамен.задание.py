CREATE TABLE categories (
    code VARCHAR(2) PRIMARY KEY,
    title VARCHAR(150)
);

INSERT INTO categories (code, title) VALUES
    ('FD', 'Food products'),
    ('DR', 'Drinks'),
    ('EL', 'Electronics'),
    ('CL', 'Clothes');

CREATE TABLE stores (
    store_id INTEGER PRIMARY KEY,
    title VARCHAR(100)
);

INSERT INTO stores (store_id, title) VALUES
    (1, 'Asia'),
    (2, 'Globus'),
    (3, 'Spar');

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    title VARCHAR(250),
    category_code VARCHAR(2),
    unit_price FLOAT,
    stock_quantity INTEGER,
    store_id INTEGER,
    FOREIGN KEY (category_code) REFERENCES categories(code),
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

INSERT INTO products (title, category_code, unit_price, stock_quantity, store_id) VALUES
    ('Chocolate', 'FD', 10.5, 129, 1),
    ('Orange Juice', 'DR', 3.50, 50, 2),
    ('Laptop', 'EL', 799.99, 30, 3),
    ('T-shirt', 'CL', 19.99, 200, 1),
    ('Milk', 'DR', 2.50, 100, 2),
    ('Bread', 'FD', 1.80, 80, 3);


import sqlite3

def display_products_by_store(store_id):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT products.title, categories.title, products.unit_price, products.stock_quantity
        FROM products
        JOIN categories ON products.category_code = categories.code
        WHERE products.store_id = ?
    ''', (store_id,))

    products = cursor.fetchall()

    if products:
        for product in products:
            print(f"name of product: {product[0]}")
            print(f"category: {product[1]}")
            print(f"prace: {product[2]}")
            print(f"Quantity in stock: {product[3]}\n")
    else:
        print("There are no products in this store.")

    conn.close()

def display_stores():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT store_id, title FROM stores')
    stores = cursor.fetchall()

    for store in stores:
        print(f"{store[0]}. {store[1]}")

    conn.close()

def main():
    print("You can display a list of products by the selected store id from the list of stores below, to exit the program enter the number 0:")
    display_stores()

    while True:
        try:
            store_id = int(input("input  id of store (0 для выхода): "))
            if store_id == 0:
                break
            display_products_by_store(store_id)
        except ValueError:
            print("Incorrect input. Please enter a number.")
        except sqlite3.OperationalError:
            print("Database error. Check your connection and the existence of tables.")

if __name__ == "__main__":
    main()