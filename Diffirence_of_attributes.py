class Building:
    total = 0
    def __init__(self):
        Building.total += 1


buildings = []
for _ in range(40):
    building = Building()
    buildings.append(building)
    print(building)
print(f"Dсего создано обЪектов класса Building: {Building.total}")



