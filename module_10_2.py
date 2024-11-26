import threading
import time


class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def battle(self, name, power, num_warriors):
        count_day = 0
        while num_warriors:
            time.sleep(1)
            count_day += 1
            num_warriors -= power
            print(f"{name} сражается {count_day}..., осталось {num_warriors} воинов.")
        print(f"{name} одержал победу спустя {count_day} дней(дня)!")

    def run(self):
        print(f"{self.name}, на нас напали!")
        self.battle(self.name, self.power, 100)

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")