import sqlite3
conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

def close_connection():
    conn.commit()
    conn.close()

    def create_table():
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_title TEXT NOT NULL,
                price REAL NOT NULL DEFAULT 0.0,
                quantity INTEGER NOT NULL DEFAULT 0
            )
        ''')
        print("The products table has been created or already exists..")

    def add_products():
        products = [
            ("Жидкое мыло с запахом ванили", 50.0, 10),
            ("Мыло детское", 30.0, 20),
            ("Шампунь для волос", 100.0, 5),
            ("Гель для душа", 150.0, 3),
            ("Пена для ванн", 80.0, 15),
            ("Зубная паста", 40.0, 25),
            ("Зубная щетка", 20.0, 50),
            ("Шариковая ручка", 5.0, 100),
            ("Тетрадь в клетку", 10.0, 200),
            ("Ручка-роллер", 12.0, 30),
            ("Карандаш для глаз", 45.0, 10),
            ("Молоко", 60.0, 50),
            ("Хлеб", 25.0, 100),
            ("Масло растительное", 80.0, 30),
            ("Чай черный", 40.0, 70)
        ]

        cursor.executemany('''
            INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)
        ''', products)

        print("15 товаров успешно добавлены.")


def update_quantity(product_id, new_quantity):
    cursor.execute('''
        UPDATE products SET quantity = ? WHERE id = ?
    ''', (new_quantity, product_id))
    print(f"Quantity of goods with id {product_id} обновлено.")

def update_price(product_id, new_price):
    cursor.execute('''
        UPDATE products SET price = ? WHERE id = ?
    ''', (new_price, product_id))
    print(f"Цена товара с id {product_id} обновлена.")

def delete_product(product_id):
     cursor.execute('''
        DELETE FROM products WHERE id = ?
     ''', (product_id,))
     print(f"Товар с id {product_id} удален.")

def print_all_products():
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def print_products_by_price_and_quantity(price_limit, quantity_limit):
    cursor.execute('''
        SELECT * FROM products WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
def search_product_by_name(search_term):
    cursor.execute('''
        SELECT * FROM products WHERE product_title LIKE ?
    ''', ('%' + search_term + '%',))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

