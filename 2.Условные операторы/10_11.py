# TODO Даны значения трех сторон треугольника a, b, и c.
#  Наименьшая из сторон треугольника является стороной квадрата. Определить, площадь какой из фигур больше.

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

list_ = [i for i in (a, b, c)]
print(list_)
min_num = list_[0]
for i in list_:
    if i < min_num:
        min_num = i
print(min_num)

p = int((a + b + c) / 2)
print(p, type(p))
area_triangle = int((p * (p - a) * (p - b) * (p - c)) ** 0.5)
print(area_triangle, ' :площадь треугольника', type(area_triangle))
area_square = min_num ** 2
print(area_square, ' :площадь квадрата', type(area_square))

if area_triangle > area_square:
    print('Площадь треугольниа больше площади квадрата')
elif area_triangle < area_square:
    print('Площадь треугольниа меньше площади квадрата')
else:
    print('Площадь треугольниа РАВНА площади квадрата')
# TODO комплексные числа и работа с ними
