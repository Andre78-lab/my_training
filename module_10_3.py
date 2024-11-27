import threading
import random
import time


class Bank():
    look = threading.Lock()

    def __init__(self):

        self.balance = 0

    def deposit(self):
        for _ in range(100):
            bal = random.randint(50, 500)
            self.balance += bal
            if self.balance >= 500 and self.look.locked():
                self.look.release()
            print(f'Пополнение: {bal}. Баланс: {self.balance}.')
            time.sleep(0.01)

    def take(self):
        for _ in range(100):
            bal = random.randint(50, 500)
            print(f'Запрос на {bal}')
            if bal <= self.balance:
                self.balance -= bal
                print(f'Снятие: {bal}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.look.acquire()
            time.sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
