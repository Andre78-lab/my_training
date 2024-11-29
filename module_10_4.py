import threading
import random
import time
from queue import Queue


class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        sec = random.randint(3, 10)
        time.sleep(sec)


class Cafe:

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        list_guests = list(guests)
        list_t = []
        for i in self.tables:
            if i.guest is None:
                list_t.append(i)
        for i in range(min(len(list_guests), len(list_t))):
            list_t[i].guest = list_guests[i]
            th_g = list_guests[i]
            th_g.start()
            print(f"{list_guests[i].name} сел(-а) за стол номер {list_t[i].number}")
        if len(list_guests) > len(list_t):
            for j in range(len(list_t), len(list_guests)):
                self.queue.put(list_guests[j])
                print(f'{list_guests[j].name} в очереди')

    def __None_table(self):
        for tab in self.tables:
            if not tab.guest is None:
                return True
        return False

    def discuss_guests(self):
        while not self.queue.empty() or Cafe.__None_table(self):
            for table in self.tables:
                if not table.guest is None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    thr = table.guest
                    thr.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests(),

print("Всех накормили!")
