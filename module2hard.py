def find_password(n):
    if n < 3 or n > 20:
        return "Число должно быть от 3 до 20"

    password = ""
    for i in range(1, n):
        pairs = []
        for j in range(1, 21):
            if (i != j) and ((i + j) <= n) and ((n % (i + j)) == 0):
                pairs.append(j)

        if pairs:
            for pair in pairs:
                password += str(i) + str(pair)

    return password


# Ввод числа и вывод пароля
n = int(input("Введите число от 3 до 20: "))
result = find_password(n)
print(result)
