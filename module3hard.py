def calculate_structure_sum(data):
    total_sum = 0

    for i in data:
        if isinstance(i, int):
            total_sum += i
        elif isinstance(i, str):
            total_sum += len(i)
        elif isinstance(i, (list, tuple)):
            total_sum += calculate_structure_sum(i)
        elif isinstance(i, dict):
            total_sum += sum([calculate_structure_sum([key, value]) for key, value in i.items()])
        elif isinstance(i, (set, frozenset)):
            total_sum += calculate_structure_sum(list(i))

    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
