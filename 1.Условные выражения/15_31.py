# Записать логические выражения, которые имеют значение «истина» только при выполнении указанных условий - неверно, что x>0 и x<5.
x = int(input('Enter x: '))

if 0 < x < 5:
    print(True)
else:
    print(False)