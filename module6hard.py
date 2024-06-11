class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.filled = False
        if len(sides) != self.sides_count:
            self.sides = [1] * self.sides_count
        else:
            self.set_sides(*sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.sides = list(sides)

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def __len__(self):
        return sum(self.sides)
    def get_sides(self):
        return self.sides 

import math


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2

    def set_sides(self, *sides):
        super().set_sides(*sides)
        self.__radius = self.sides[0] / (2 * math.pi)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.calculate_height()

    def calculate_height(self):
        s = sum(self.sides) / 2
        return (2 / self.sides[0]) * (s * (s - self.sides[0]) * (s - self.sides[1]) * (s - self.sides[2])) ** 0.5

    def get_square(self):
        return 0.5 * self.sides[0] * self.__height

    def set_sides(self, *sides):
        super().set_sides(*sides)
        self.__height = self.calculate_height()


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * 12
        super().__init__(color, *sides)

    def get_volume(self):
        side_length = self.sides[0]
        return side_length ** 3

    def set_sides(self, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * 12
        super().set_sides(*sides)


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Выходные данные (консоль):
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216
