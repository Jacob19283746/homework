result = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']

for i in range(len(students)):
    avg_grade = sum(grades[i]) / len(grades[i])
    result[students[i]] = avg_grade

print(result)
