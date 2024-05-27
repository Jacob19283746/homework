class Building:
    def __init__(self, numberOfFloors: int, buildingType: str):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        if isinstance(other, Building):
            return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
        return False

# Примеры использования:
building1 = Building(5, "Residential")
building2 = Building(5, "Residential")
building3 = Building(10, "Commercial")

print(building1 == building2)  # True
print(building1 == building3)  # False