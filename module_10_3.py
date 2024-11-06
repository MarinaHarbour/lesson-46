import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for transaction in range(100):
            replenishment = random.randint(50, 500)
            with self.lock:
                self.balance += replenishment
                print(f"Пополнение: {replenishment}. Баланс: {self.balance}")

            time.sleep(0.001)

    def take(self):
        for transaction in range(100):
            withdrawal = random.randint(50, 500)
            print(f"Запрос на {withdrawal}")

            with self.lock:
                if withdrawal <= self.balance:
                    self.balance -= withdrawal
                    print(f"Снятие: {withdrawal}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")

            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
