def find_min_max(*args):
    if len(args) == 0:
        return None

    min_value = min(args)
    max_value = max(args)
    return min_value, max_value
result = find_min_max(10, 5, 8, 12, 3)
print(f'Найменше та найбільше значення: {result}')

result = find_min_max(7, 2, 9, 1, 6, 4)
print(f'Найменше та найбільше значення: {result}')

