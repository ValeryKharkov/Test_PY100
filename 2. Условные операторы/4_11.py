# Определить, является ли шестизначное число "счастливым" (сумма первых трех цифр равна сумме последних трех цифр).
number = (input('Enter number: '))
# print(number, type(number))
# print(number[0:3], type(number[0:3]))
# print(number[3:6])

list_ = [int(i) for i in number]
if sum(list_[0:3]) == sum(list_[3:6]):
    print('Число счастливое')
else:
    print('Число не счастливое')
