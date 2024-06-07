class Vehicle:  # базовый класс
    vehicle_type = "none"


class Car:  # базовый класс
    price = 1000000

    def horse_powers(self):
        return 110


class Nissan(Vehicle, Car):  # наследование класса с переобразованием
    vehicle_type = "sedan"
    price = 900000

    def horse_powers(self):
        return 100


nis = Nissan()
print(f"Тип транспортного средства: {nis.vehicle_type}")
print(f"Цена транспортного средства: {nis.price}")
