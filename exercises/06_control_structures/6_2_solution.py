#!/usr/bin/env python3
print('''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
    'unicast'         - если первый байт в диапазоне 1-223
    'multicast'       - если первый байт в диапазоне 224-239
    'local broadcast' - если IP-адрес равен 255.255.255.255
    'unassigned'      - если IP-адрес равен 0.0.0.0
    'unused'          - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.''')
print('-' * 70, '\n')

ip = input('Введите IP-адрес в формате xxx.xxx.xxx.xxx: ')
ip_l = ip.split('.')
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
