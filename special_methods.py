class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f"Количество этажей установленно на: {self.numberOfFloors}")


my_house = House()
print(f"Изначальное количество этажей: {my_house.numberOfFloors}")


my_house.setNewNumberOfFloors(input("Введите количество:"))

