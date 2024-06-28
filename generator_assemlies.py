# Задание №1 Обычные функции

def function_factory(res):
    if res == 'addit':
        return lambda x, y: x + y
    elif res == 'sub':
        return lambda x, y: x - y
    elif res == 'multi':
        return lambda x, y: y * y
    elif res == 'divis':
        return lambda x, y: x / y if y != 0 else "You can't divide by zero"
    else:
        return None


# Пример использования

addit = function_factory('addit')
print(addit(5, 6))

sub = function_factory('sub')
print(sub(3, 2))

multi = function_factory('multi')
print(multi(7, 9))

divis = function_factory('divis')
print(divis(8, 3))
print(divis(4, 0))

# Задание №2 Лямбда функции

square_lambda = lambda x: x ** 2


def square_def(x):
    return x ** 2


# Пример использования

print(f'Задание №2 {square_lambda(6)}')
print(f'Задание №2 {square_def(95)}')


# Задание №3 Вызываемые объекты

class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

# Пример использования


rect = Rect(3, 4)
print(f'Задание №3 {rect()}')

