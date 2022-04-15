# TODO Дано трехзначное число. Определить: а) является ли сумма его цифр двузначным числом; б) является ли произведение его цифр трехзначным числом.
user_number = input('Enter number: ')


def sum_digit(number: str) -> int:
    return sum([int(i) for i in number])


def len_sum_digit(number: int) -> int:
    return len(str((sum_digit(number))))


def len_mult_digit(number: int) -> int:
    return [int * i for i in number]
    pass


if len_sum_digit(user_number) == 2:
    print('Сумма цифр числа - двузначное число')
else:
    print('Сумма цифр числа - НЕ двузначное число')
