#  Записать условие, которое является истинным, когда только одно из чисел А, В и С меньше 45.
A = int(input('Enter A: '))
B = int(input('Enter B: '))
C = int(input('Enter C: '))

if A < 45 and B >= 45 and C >= 45:
    print(True)
elif B < 45 and A >= 45 and C >= 45:
    print(True)
elif C < 45 and A >= 45 and B >= 45:
    print(True)
else:
    print(False)