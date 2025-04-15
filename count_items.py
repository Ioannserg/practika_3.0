def count_items(*args):
    print(f'Количество переданных элементов: {len(args)}')

args = input('ggg').split(', ')
count_items(*args)