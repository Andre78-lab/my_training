import random
import sqlite3
from itertools import count

# создаем соединение с базой
connection = sqlite3.connect('not_telegram_1.db')
# Создаем курсор
cursor = connection.cursor()

# Создание таблицы Users
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY kEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
"""
               )

# Создание инденкса по email
cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Заполнение таблицы
#for i in range(10):
#   cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                  (f"Новый пользователь {i+1}", f"example{i+1}@gmail.com", f"{(i+1)*10}", str(1000)))

# Обновление balance у каждой 2ой записи начиная с 1ой на 500
#cursor.execute(" UPDATE Users SET balance = ? WHERE id % 2 = 1", (500,))

# Удаление каждой 3ей записи в таблице начиная с 1ой
#cursor.execute(" DELETE FROM Users WHERE id % 3 = 1")

# Выборка, где возраст не равен 60
cursor.execute(" SELECT username, email, age, balance FROM Users WHERE age <> ?", (60,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

# Удалите из базы данных not_telegram.db запись с id = 6
cursor.execute(" DELETE FROM Users WHERE id = 6")

# Подсчитать общее количество записей.
cursor.execute(" SELECT COUNT(*) FROM Users")
count_users = cursor.fetchone()[0]
print(f'Общее количество записей - {count_users}')

#Посчитать сумму всех балансов
cursor.execute(" SELECT SUM(balance) FROM Users")
sum_balans_all = cursor.fetchone()[0]
print(f'Сумма всех балансов - {sum_balans_all}')

#Вывести в консоль средний баланс всех пользователей
print(f'Средний баланс (расчетный): {sum_balans_all/count_users}')

cursor.execute(" SELECT AVG(balance) FROM Users")
balance_avg = cursor.fetchone()[0]
print(f'Средний баланс (через AVG): {balance_avg}')







# !сохранение изменения в базе данных
connection.commit()
# !закрыть соединение
connection.close()
