# Записать условие, которое является истинным, когда каждое из чисел А и В нечетное.
A = int(input('Enter A: '))
B = int(input('Enter B: '))

if A % 2 != 0 and B % 2 != 0:
    print(True)
else:
    print(False)