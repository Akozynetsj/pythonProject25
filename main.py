def join_parameters(*args):
    return ', '.join(str(arg) for arg in args)
result = join_parameters('apple', 'banana', 'cherry', 'date')
print(f'Рядок з об\'єднаними параметрами: {result}')

