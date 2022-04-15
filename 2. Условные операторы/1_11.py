#  Дано двузначное число. Определить: а) входит ли в него цифра 5; б) входит ли в него цифра 3
number = list(input('Enter number: '))

if '5' in number or '3' in number:
    print(True)
else:
    print(False)