# TODO Определить, сколько в введенном пользователем числе четных цифр, а сколько нечетных.
number = input('Введите число: ')
x_1 = 0
x_2 = 0
list_ = [int(i) for i in number]
print(list_)

for i in list_:
    if i % 2 == 0:
        x_2 += 1
    else:
        x_1 += 1
print('Кол-во четных цифр в вашем числе: ', x_2)
print('Кол-во НЕ четных цифр в вашем числе: ', x_1)