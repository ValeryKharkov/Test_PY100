# Задано натуральные числа от 10 до N. Вывести нечетные кратные пяти числа.
N = int(input('Enter N: '))
print([i for i in range(10, N + 1) if i % 2 != 0 and i % 5 == 0])