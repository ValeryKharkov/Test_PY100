# Дано трехзначное число. Определить: а) является ли произведение его цифр больше числа b; б) кратна ли сумма его цифр трем
number_3 = input('Enter three-digit number: ')
b = int(input('Enter b: '))

list_ = [int(i) for i in number_3]
# print(list_)

mult_element_list_ = 1
for i in list_:
    mult_element_list_ *= i
# print(mult_element_list_)

if mult_element_list_ > b:
    print('Произведение цифр трехзначного числа больше числа b')
elif mult_element_list_ < b:
    print('Произведение цифр трехзначного числа меньше числа b')
else:
    print('Произведение цифр трехзначного числа равно числу b')

if sum(list_) % 3 == 0:
    print('Сумма цифр трехзначного числа кратна 3-м')
else:
    print('Сумма цифр трехзначного числа НЕ кратна 3-м')