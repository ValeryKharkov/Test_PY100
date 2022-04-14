# TODO Дан одномерный массив. Переставить в обратном порядке элементы массива,
#  расположенные между минимальным и максимальным элементами.
numbers = [-1, 2, 8, -6, -4, -1, 0, 3, 7, -7]

min_number = min(numbers)
max_number = max(numbers)


max_index = [i for i, j in enumerate(numbers) if j == max_number]
print(max_index)

min_index = [i for i, j in enumerate(numbers) if j == min_number]
print(min_index)

