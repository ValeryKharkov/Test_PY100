# Дан массив целых чисел. Все элементы, оканчивающиеся цифрой 4, уменьшить вдвое.
import random

numbers = [random.randint(1, 100) for i in range(20)]

result = [int(i / 2) for i in numbers if i % 10 == 4]
print(result)