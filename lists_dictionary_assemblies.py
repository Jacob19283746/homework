numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]


def remain(num):
    return num % 2 != 0


def square(num):
    return num ** 2


remain_numbers = filter(remain, numbers)
squared_remain_numbers = map(square, remain_numbers)
result = list(squared_remain_numbers)
print(result)
