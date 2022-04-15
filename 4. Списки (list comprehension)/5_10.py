# Найти количество и произведение отрицательных элементов, а также сумму нечетных элементов.
list_ = [-1, 2, 8, -6, -4, -1, 0, 3, 7, -7]

len_ = len([i for i in list_ if i < 0])
# print(len_)

list_mult = [i for i in list_ if i < 0]
print(list_mult)
mult_ = 1
for i in list_mult:
    # print(i)
    mult_ *= i
    # print(mult_)
print(mult_)

odd_ = [i for i in list_ if i % 2 != 0]
print(sum(odd_))