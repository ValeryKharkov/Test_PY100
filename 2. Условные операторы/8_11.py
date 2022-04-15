# Дано четырехзначное число. Определить: а) кратно ли произведение его цифр трем; б) кратно ли числу а произведение его цифр.
number_4 = input('Enter four-digit number: ')
a = int(input('Enter a: '))

list_ = [int(i) for i in number_4]

mult_element_list_ = 1

for i in list_:
    mult_element_list_ *= i
print(mult_element_list_)

if mult_element_list_ % 3 == 0:
    print('Произведение цифр числа кратна 3-м')
else:
    print('Произведение цифр числа НЕ кратна 3-м')

if mult_element_list_ % a == 0:
    print('Произведение цифр числа кратна числу "а"')
else:
    print('Произведение цифр числа НЕ кратна числу "а"')