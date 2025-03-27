# import sqlite3
# conn = sqlite3.connect('hw.db')
# cursor = conn.cursor()
#
# def close_connection():
#     conn.commit()
#     conn.close()
#
#     def create_table():
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS products (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 product_title TEXT NOT NULL,
#                 price REAL NOT NULL DEFAULT 0.0,
#                 quantity INTEGER NOT NULL DEFAULT 0
#             )
#         ''')
#         print("The products table has been created or already exists..")
#
#     def add_products():
#         products = [
#             ("Жидкое мыло с запахом ванили", 50.0, 10),
#             ("Мыло детское", 30.0, 20),
#             ("Шампунь для волос", 100.0, 5),
#             ("Гель для душа", 150.0, 3),
#             ("Пена для ванн", 80.0, 15),
#             ("Зубная паста", 40.0, 25),
#             ("Зубная щетка", 20.0, 50),
#             ("Шариковая ручка", 5.0, 100),
#             ("Тетрадь в клетку", 10.0, 200),
#             ("Ручка-роллер", 12.0, 30),
#             ("Карандаш для глаз", 45.0, 10),
#             ("Молоко", 60.0, 50),
#             ("Хлеб", 25.0, 100),
#             ("Масло растительное", 80.0, 30),
#             ("Чай черный", 40.0, 70)
#         ]
#
#         cursor.executemany('''
#             INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)
#         ''', products)
#
#         print("15 товаров успешно добавлены.")
#
#
# def update_quantity(product_id, new_quantity):
#     cursor.execute('''
#         UPDATE products SET quantity = ? WHERE id = ?
#     ''', (new_quantity, product_id))
#     print(f"Quantity of goods with id {product_id} обновлено.")
#
# def update_price(product_id, new_price):
#     cursor.execute('''
#         UPDATE products SET price = ? WHERE id = ?
#     ''', (new_price, product_id))
#     print(f"Цена товара с id {product_id} обновлена.")
#
# def delete_product(product_id):
#      cursor.execute('''
#         DELETE FROM products WHERE id = ?
#      ''', (product_id,))
#      print(f"Товар с id {product_id} удален.")
#
# def print_all_products():
#     cursor.execute('SELECT * FROM products')
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
#
# def print_products_by_price_and_quantity(price_limit, quantity_limit):
#     cursor.execute('''
#         SELECT * FROM products WHERE price < ? AND quantity > ?
#     ''', (price_limit, quantity_limit))
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
# def search_product_by_name(search_term):
#     cursor.execute('''
#         SELECT * FROM products WHERE product_title LIKE ?
#     ''', ('%' + search_term + '%',))
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
#

import sqlite3

def create_connection():
    try:
        conn = sqlite3.connect('hw.db')
        return conn
    except sqlite3.Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return None

def close_connection(conn):
    if conn:
        try:
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Ошибка при закрытии соединения: {e}")

def create_table(conn):
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_title TEXT NOT NULL,
                    price REAL NOT NULL DEFAULT 0.0,
                    quantity INTEGER NOT NULL DEFAULT 0
                )
            ''')
            print("Таблица products создана или уже существует.")
        except sqlite3.Error as e:
            print(f"Ошибка при создании таблицы: {e}")

def add_products(conn):
    if conn:
        try:
            cursor = conn.cursor()
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
        except sqlite3.Error as e:
            print(f"Ошибка при добавлении товаров: {e}")

def update_quantity(conn, product_id, new_quantity):
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE products SET quantity = ? WHERE id = ?
            ''', (new_quantity, product_id))
            print(f"Количество товара с id {product_id} обновлено.")
        except sqlite3.Error as e:
            print(f"Ошибка при обновлении количества: {e}")

def update_price(conn, product_id, new_price):
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE products SET price = ? WHERE id = ?
            ''', (new_price, product_id))
            print(f"Цена товара с id {product_id} обновлена.")
        except sqlite3.Error as e:
            print(f"Ошибка при обновлении цены: {e}")

def delete_product(conn, product_id):
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM products WHERE id = ?
            ''', (product_id,))
            print(f"Товар с id {product_id} удален.")
        except sqlite3.Error as e:
            print(f"Ошибка при удалении товара: {e}")

def print_all_products(conn):
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM products')
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"Ошибка при выводе товаров: {e}")

def print_products_by_price_and_quantity(conn, price_limit, quantity_limit):
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM products WHERE price < ? AND quantity > ?
            ''', (price_limit, quantity_limit))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"Ошибка при выводе товаров по цене и количеству: {e}")

def search_product_by_name(conn, search_term):
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM products WHERE product_title LIKE ?
            ''', ('%' + search_term + '%',))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"Ошибка при поиске товаров: {e}")


conn = create_connection()
if conn:
    create_table(conn)
    add_products(conn)
    print_all_products(conn)
    update_quantity(conn, 1, 100)
    update_price(conn, 2, 50)
    delete_product(conn, 3)
    print_products_by_price_and_quantity(conn, 100, 10)
    search_product_by_name(conn, "мыло")
    close_connection(conn)