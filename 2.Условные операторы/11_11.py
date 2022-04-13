# Дано натуральное четырехзначное число. Выяснить, являются ли все его числа уникальными.
number_4 = input('Enter four-digit number: ')

list_ = [int(i) for i in number_4]
print(len(list_))
print(len(set(list_)))
if len(list_) == len(set(list_)):
    print('Числа заданного числа - уникальные')
else:
    print('Числа заданного числа - НЕ уникальные')