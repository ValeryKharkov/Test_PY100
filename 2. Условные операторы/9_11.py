# Дано трехзначное число а. Определить: а) является ли произведение его цифр меньше числа а; б) кратна ли 5 сумма его цифр.
number_3 = input('Enter three-digit number: ')
a = int(input('Enter a: '))

list_ = [int(i) for i in number_3]

mult_element_list_ = 1

for i in list_:
    mult_element_list_ *= i
print(mult_element_list_)

if mult_element_list_ < a:
    print('Произведение цифр числа МЕНЬШЕ числа "а"')
else:
    print('Произведение цифр числа БОЛЬШЕ ЛИБО РАВНО числа "а"')

if sum(list_) % 5 == 0:
    print('Сумма цифр числа кратна 5-ти')
else:
    print('Сумма цифр числа НЕ кратна 5-ти')