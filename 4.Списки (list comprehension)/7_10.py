# TODO Используя датчик случайных чисел, заполнить массив из двадцати элементов неповторяющимися числами.
import random

random_numbers = [i for i in range(10000)]
random.shuffle(random_numbers)
print(random_numbers[:20])

