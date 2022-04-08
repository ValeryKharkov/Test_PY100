#  Записать условие, которое является истинным , когда целое А кратно двум или трем.
A = int(input('Enter A: '))
if A % 2 == 0 and A % 3 == 0:
    print(True)
else:
    print(False)