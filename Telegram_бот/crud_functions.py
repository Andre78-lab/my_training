import sqlite3
import random

# создадим соединение с базой
connection = sqlite3.connect('not_telegram_14_4.db')

# Создаем курсор
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY kEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL);
''')


#for i in range(1, 40):
#    cursor.execute(" INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                   (f"Продукт {i}", f"Описание продукта {i}", str(random.randint(200, 7000))))



def get_all_products():
    cursor.execute(" SELECT * FROM Products")
    check_products = cursor.fetchall()
    connection.commit()
    return check_products


# !сохранение изменения в базе данных
connection.commit()
# !После сохранения необходимо закрыть соединение






