class Car:
    price = 1000000

    def horse_powers(self):
        return 120


class Nissan(Car):
    price = 900000

    def horse_powers(self):
        return 100


class Kia(Car):
    price = 800000

    def horse_powers(self):
        return 110


car = Car()
car.horse_powers()

nissan = Nissan()
nissan.horse_powers()

kia = Kia()
kia.horse_powers()
