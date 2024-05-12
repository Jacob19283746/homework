def print_params(a: object = 1, b: object = 'строка', c: object = True):
    print(a, b, c)


# Вызов функции с разным количеством аргументов


print_params()
print_params(10)
print_params(b=25)
print_params(c=[1, 2, 3])

# Распаковка параметров
values_list = [100, 'hello', False]
values_dict = {'a': 50, 'b': 'world', 'c': True}
print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры
values_list_2 = [7, 'test']
print_params(*values_list_2, 42)
