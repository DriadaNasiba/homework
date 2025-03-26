CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
);

INSERT INTO countries (title) VALUES ('Киргизия');
INSERT INTO countries (title) VALUES ('Германия');
INSERT INTO countries (title) VALUES ('Китай');


CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    area REAL DEFAULT 0,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries(id)
);

INSERT INTO cities (title, area, country_id) VALUES ('Бишкек', 200, 1);  -- Киргизия
INSERT INTO cities (title, area, country_id) VALUES ('Ош', 150, 1);  -- Киргизия
INSERT INTO cities (title, area, country_id) VALUES ('Берлин', 891, 2);  -- Германия
INSERT INTO cities (title, area, country_id) VALUES ('Мюнхен', 310, 2);  -- Германия
INSERT INTO cities (title, area, country_id) VALUES ('Пекин', 1650, 3);  -- Китай
INSERT INTO cities (title, area, country_id) VALUES ('Шанхай', 6340, 3);  -- Китай
INSERT INTO cities (title, area, country_id) VALUES ('Гуанчжоу', 7434, 3);  -- Китай


CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES cities(id)
);

INSERT INTO students (first_name, last_name, city_id) VALUES ('Александр', 'Иванов', 1);  -- Бишкек
INSERT INTO students (first_name, last_name, city_id) VALUES ('Елена', 'Петрова', 2);  -- Ош
INSERT INTO students (first_name, last_name, city_id) VALUES ('Михаил', 'Смирнов', 3);  -- Берлин
INSERT INTO students (first_name, last_name, city_id) VALUES ('Мария', 'Кузнецова', 4);  -- Мюнхен
INSERT INTO students (first_name, last_name, city_id) VALUES ('Виктор', 'Михайлов', 5);  -- Пекин
INSERT INTO students (first_name, last_name, city_id) VALUES ('Анна', 'Васильева', 6);  -- Шанхай
INSERT INTO students (first_name, last_name, city_id) VALUES ('Дмитрий', 'Попов', 7);  -- Гуанчжоу
INSERT INTO students (first_name, last_name, city_id) VALUES ('Ольга', 'Соколова', 1);  -- Бишкек
INSERT INTO students (first_name, last_name, city_id) VALUES ('Иван', 'Павлов', 2);  -- Ош
INSERT INTO students (first_name, last_name, city_id) VALUES ('Светлана', 'Горшкова', 3);  -- Берлин
INSERT INTO students (first_name, last_name, city_id) VALUES ('Роман', 'Крылов', 4);  -- Мюнхен
INSERT INTO students (first_name, last_name, city_id) VALUES ('Юлия', 'Медведева', 5);  -- Пекин
INSERT INTO students (first_name, last_name, city_id) VALUES ('Ирина', 'Лебедева', 6);  -- Шанхай
INSERT INTO students (first_name, last_name, city_id) VALUES ('Артем', 'Николаев', 7);  -- Гуанчжоу
INSERT INTO students (first_name, last_name, city_id) VALUES ('Наталья', 'Федорова', 3);  -- Берлин

import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()


def show_cities():
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    print(
        "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    for city in cities:
        print(f"{city[0]}. {city[1]}")

def show_students_by_city(city_id):
    cursor.execute("""
        SELECT s.first_name, s.last_name, c.title AS city, co.title AS country, ci.area 
        FROM students s
        JOIN cities c ON s.city_id = c.id
        JOIN countries co ON c.country_id = co.id
        WHERE s.city_id = ?
    """, (city_id,))
    students = cursor.fetchall()

    if students:
        for student in students:
            print(
                f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[3]}, Город: {student[2]}, Площадь города: {student[4]}")
    else:
        print("Учеников в этом городе нет.")

while True:
    show_cities()
    user_input = input("Введите id города (или 0 для выхода): ")

    if user_input == "0":
        break

    try:
        city_id = int(user_input)
        if city_id > 0:
            show_students_by_city(city_id)
        else:
            print("Неверный id города. Попробуйте снова.")
    except ValueError:
        print("Пожалуйста, введите числовое значение.")

