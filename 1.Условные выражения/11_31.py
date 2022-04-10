#  Записать условие, которое является истинным, когда только одно из чисел А и В четное.
A = int(input('Enter A: '))
B = int(input('Enter B: '))

if (A % 2 == 0 and B % 2 != 0) or (A % 2 != 0 and B % 2 == 0):
    print(True)
else:
    print(False)