x = 38
print('дратути!')
if x < 0:
    print('Меньше нуля')
print('датвидания!')

# примеры
a, b = 10, 5
if a > b:
    print('a > b')
if a > b and a > 0:
    print('успех')
if (a > b) and (a > 0 or b < 1000):
    print('успex')
if 5 < b and b < 10:
    print('успех')

# можно сравнивать - числа, строки, списки, вообще -

if '34' > '123':
    print('ycпex')

if '123' > '12':
    print('успех')

if [1, 2] > [1, 1]:
    print('yспex')


# что нельзя сравнивать - разные типы
if '6' > 2:
    print("успex")
if [5, 6] > 5:
    print('успex')

# HO

if '6' != 5:
    print('успех')