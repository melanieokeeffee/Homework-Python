# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

a = int(input('input first number: '))
b = int(input('input second number: '))
c = int(input('Divided by...'))
# ноль можно делить на любое число, а на ноль делить нельзя
# исходя из этого составляю функцию
if c == 0:
    print('do no divided by 0')
else:
    print(f'{a}/{c}={a / c}; {b}/{c}={b / c}')

