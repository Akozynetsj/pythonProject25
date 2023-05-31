def get_odd_numbers(*args):
    odd_numbers = [num for num in args if num % 2 != 0]
    return odd_numbers
result = get_odd_numbers(1, 2, 3, 4, 5, 6)
print(f'Список непарних чисел: {result}')
