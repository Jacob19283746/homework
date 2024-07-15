import threading
import time
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Customer(threading.Thread):
    def __init__(self, number, cafe):
        threading.Thread.__init__(self)
        self.number = number
        self.cafe = cafe

    def run(self):
        while True:
            table = self.cafe.get_free_table()
            if table:
                print(f"Посетитель номер {self.number} сел за стол {table.number}")
                time.sleep(5) 
                print(f"Посетитель номер {self.number} покушал и ушёл.")
                self.cafe.release_table(table)
                break
            else:
                print(f"Посетитель номер {self.number} ожидает свободный стол")
                self.cafe.queue.put(self)
                break


class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = queue.Queue()

    def customer_arrival(self):
        for i in range(1, 21):
            print(f"Посетитель номер {i} прибыл")
            customer = Customer(i, self)
            self.serve_customer(customer)
            time.sleep(1)

    def serve_customer(self, customer):
        table = self.get_free_table()
        if table:
            customer.start()
        else:
            print(f"Посетитель номер {customer.number} ожидает свободный стол")
            self.queue.put(customer)

    def get_free_table(self):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                return table
        return None

    def release_table(self, table):
        table.is_busy = False
        if not self.queue.empty():
            next_customer = self.queue.get()
            new_customer = Customer(next_customer.number, self)
            new_customer.start()


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()

