# Записать условие, которое является истинным, когда целое N кратно пяти и не оканчивается нулем
N = int(input('Enter N: '))

if N % 5 == 0 and N % 10 != 0:
    print(True)
else:
    print(False)