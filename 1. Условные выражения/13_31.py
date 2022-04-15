# Записать условие, которое является истинным, когда целое N кратно четырем или семи.
N = int(input('Enter N: '))

if N % 4 == 0 or N % 7 == 0:
    print(True)
else:
    print(False)
