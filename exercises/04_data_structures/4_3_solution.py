#!/usr/bin/env python3
print('''
Задание 4.3

Получить из строки config список VLANов вида:

      ['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.
''')
print('-' * 70)
print('The first way by using the methods str.find(), len(), and str.split()')
print('-' * 70, '\n')

config = 'switchport trunk allowed vlan 1,3,10,20,30,100'

lenght_str = len('vlan ')
in_char = config.find('vlan ')
vlan_ids = config[in_char + lenght_str:]
vlan_ids_list = vlan_ids.split(',')

print('Длина строки "vlan "             :', lenght_str)
print('Начальная позиция строки "vlan " :', in_char)
print('Строка с номарами vlan           :', vlan_ids)
print('Список номеров vlan              :', vlan_ids_list, '\n')
print('-' * 70)
print('The second way by using the methods str.split() and str.split(',')')                                          
print('-' * 70, '\n')
config_split = config.split()
vlan_ids = config_split[-1].split(',')
print('Строка с номарами vlan           :', config_split[-1])
print('Список номеров vlan              :', vlan_ids, '\n')
print('-' * 70, '\n')
