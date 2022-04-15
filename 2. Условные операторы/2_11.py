# Дано двузначное число. Определить: а) входят ли в него цифры 3 и 7; б) входят ли в него цифры (4 и 8) или цифра 9
number = list(input('Enter number: '))

if ('3' in number and '7' in number) or ('4' in number and '8' in number) or ('9' in number):
    print(True)
else:
    print(False)