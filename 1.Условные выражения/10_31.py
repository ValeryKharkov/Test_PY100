# TODO Записать логическое выражение, определяющее, что из четырех чисел A,B,C,D два являются четными
A = int(input('Enter A: '))
B = int(input('Enter B: '))
C = int(input('Enter C: '))
D = int(input('Enter C: '))

list_ = [A, B, C, D]
list_res = [i for i in list_ if i % 2 == 0]
if len(list_res) == 2:
    print("2 из 4 числа являются четными")
else:
    print("2 из 4 числа не являются четными")