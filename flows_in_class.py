import threading
import time

class Knight(threading.Thread):
    enemies = 100
    lock = threading.Lock()
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.local_enemies = Knight.enemies
    def run(self):
        print(f"{self.name}, на нас напали!")
        time.sleep(1)
        while self.local_enemies > 0:
            time.sleep(1)
            self.days += 1
            self.local_enemies -= self.power
            remaining_enemies = max(self.local_enemies, 0)
            print(f"{self.name} сражался {self.days}..., осталось {remaining_enemies} воинов.")
            if remaining_enemies == 0:
                print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")
                break


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
