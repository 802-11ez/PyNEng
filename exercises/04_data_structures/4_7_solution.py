#!/usr/bin/env python3
print('''
Задание 4.7
Преобразовать MAC-адрес mac в двоичную строку такого вида:
    '101010101010101010111011101110111100110011001100'
Ограничение: Все задания надо выполнять используя только пройденные темы.
''')

mac = 'AAAA:BBBB:CCCC'

mac = mac.replace(':', '')

print('-' * 70)
print('The best way by using the method str.replace().')
print('-' * 70, '\n')

print('Objective line : 101010101010101010111011101110111100110011001100')
print('Result line    :', str(bin(int(mac, 16))).replace('0b', ''), '\n')

print('-' * 70, '\n')
