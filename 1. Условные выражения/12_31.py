#  Записать условие, которое является истинным, когда каждое из чисел А,В,С кратно трем.
A = int(input('Enter A: '))
B = int(input('Enter B: '))
C = int(input('Enter C: '))

if A % 3 == 0 and B % 3 == 0 and C % 3 == 0:
    print(True)
else:
    print(False)