from bs4 import BeautifulSoup
import requests

# Запрос данных с сайта
url = 'https://git-scm.com/download/win'
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Обработка HTML-ответа
    soup = BeautifulSoup(response.text, 'html.parser')

    # Получение заголовка страницы
    title = soup.title.string
    print(f"Title: {title}\n")

    # Получение первых нескольких абзацев текста
    paragraphs = soup.find_all('p')

    print("First few paragraphs:\n")
    for paragraph in paragraphs[:3]:
        print(paragraph.get_text(), "\n")
else:
    print("Failed to retrieve data")

# import pandas as pd
#
# df = pd.read_csv('sample_data.csv')
# average_age = df['age'].mean()
# print(f"Средний возраст: {average_age}")
#
# # файл CSV доступен в PyCharm Professional

import numpy as np

# cоздание массива чисел
arr = np.array([1, 2, 3])

# выполнение математических операций
arr_squared = np.square(arr)
arr_sum = np.sum(arr)
arr_mean = np.mean(arr)

# вывод результатов
print(f"Массив: {arr}")
print(f"Квадраты элементов: {arr_squared}")
print(f"Сумма элементов: {arr_sum}")
print(f"Среднее значение элементов: {arr_mean}")
