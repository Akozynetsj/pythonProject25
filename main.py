def create_squared_dict(**kwargs):
    squared_dict = {}
    for key, value in kwargs.items():
        squared_dict[key] = value ** 2
    return squared_dict
result = create_squared_dict(a=2, b=3, c=4)
print(f'Словник з квадратами значень: {result}')
