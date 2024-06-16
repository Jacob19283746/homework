team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    result = 'Победа команды "Волшебники Данных"!'
else:
    result = 'Ничья!'

# форматирование с использованием %
# 1.Кол-во участников первой команды
team1_num_string = "В команде 'Мастера кода' участников: %d!" % team1_num
print(team1_num_string)

# 2.Кол-во участников в обеих командах
teams_num_string = "Итого сегодня в команде участников: %d и %d!" % (team1_num, team2_num)
print(teams_num_string)

# форматирование строк с использованием format()
# 1.Кол-во задач решенных командой 2
score_2_string = "Команда 'Волшебники данных' решила задач: {}!".format(score_2)
print(score_2_string)

# 2.Время за которое команда 2 решила задачи
team2_time_string = "'Волшебники данных' решили задачи за: {:.1f}c!".format(team2_time)
print(team2_time_string)

# Форматирование строк с использованием f-строк
# 1.Кол-во решённых задач по командам
score_string = f"Команды решили {score_1} и {score_2} задач!"
print(score_string)

# 2.Исход соревнования
result_string = f"Результат битвы: {result}"
print(result_string)

# 3. Кол-во задач и среднее время решения
tasks_time_string = f"Сегодня было решено {tasks_total} задачи, в среднем по {time_avg:.1f} секунды на задачу!"
print(tasks_time_string)