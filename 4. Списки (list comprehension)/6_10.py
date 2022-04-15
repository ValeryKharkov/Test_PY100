# Дан одномерный массив. Переставить в обратном порядке элементы массива,
#  расположенные между минимальным и максимальным элементами.
numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]



min_number = min(numbers)
max_number = max(numbers)

min_index = [i for i, j in enumerate(numbers) if j == min_number]
for i in min_index:
    min_index = i
print(min_index)

max_index = [i for i, j in enumerate(numbers) if j == max_number]
for i in max_index:
    max_index = i
print(max_index)

if min_index > max_index:
    result = numbers[max_index + 1:min_index]
else:
    result = numbers[min_index + 1:max_index]

print(result[::-1])