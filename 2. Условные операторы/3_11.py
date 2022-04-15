# Дано натуральное четырехзначное число. Выяснить, является ли оно палиндромом (читается одинаково слева направо и справа налево).
number = input('Enter number: ')
# print(number[::-1])
if number == number[::-1]:
    print(True)
else:
    print(False)