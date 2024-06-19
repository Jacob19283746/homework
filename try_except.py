def add_everything_up(a, b):              # функция сложения разных типов данных
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))  #обрабатывается except
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up(3, 3))              # обрабатывается try
