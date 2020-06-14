#!/usr/bin/env python3
print('''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
    'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.''')
print('-' * 70, '\n')
        
ip = input('Введите IP-адрес в формате xxx.xxx.xxx.xxx: ')
ip_l = ip.split('.')

if len(ip_l) != 4:
    print('-' * 70, '\n')
    print('Неверный IP-адрес Lenght is not equal 4.', '\n')
elif any(oct == '' for oct in ip_l):
    print('-' * 70, '\n')
    print('Неверный IP-адрес One or more octets is empty.', '\n')
elif any(oct.isalpha() for oct in ip_l):
    print('-' * 70, '\n')
    print('Неверный IP-адрес isalpha()', '\n')
elif not all(oct.isdigit() for oct in ip_l):
    print('-' * 70, '\n')
    print('Неверный IP-адрес isdigit()', '\n')
elif any(int(oct) not in range(1,255) for oct in ip_l):
    print('-' * 70, '\n')
    print('Неверный IP-адрес Not in range', '\n')
else: 
    print('-' * 70, '\n')
    if int(ip_l[0]) in range(1,224):
        print('IP address - ', ip, 'is unicast\n')
    elif int(ip_l[0]) in range(224, 240):
        print('IP address - ', ip, 'is multicast\n')
    elif ip == '255.255.255.255':
        print('IP address - ', ip, 'is local broadcast\n')
    elif ip == '0.0.0.0':
        print('IP address - ', ip, 'is unassigned\n')
    else:
        print('IP address - ', ip, 'is unused\n')
print('-' * 70, '\n')
