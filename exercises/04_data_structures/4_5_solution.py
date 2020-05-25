#!/usr/bin/env python3
print('''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.
''')

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

print('-' * 70, '\n')
print('''The best way by using the converting method from list() to set().
Then will define the intersection of sets.
Finally we will sorted list of intersection of sets.
''')
print('-' * 70, '\n')

# Извлекаем из строки command1 список VLAN ID и выводим его на экран
vlans1 = command1.split()[-1].split(',')
print(vlans1)

# Преобразуем список в множество и выводим его на экран
vlans1_set = set(vlans1)
print(vlans1_set, '\n')

# Извлекаем из строки command2 список VLAN ID и выводим его на экран
vlans2 = command2.split()[-1].split(',')
print(vlans2)

# Преобразуем список в множество и выводим его на экран
vlans2_set = set(vlans2)
print(vlans2_set, '\n')

# Определяем VLAN ID, содержащиеся в извлеченных множествах.
# Преобразуем обратно в список и сортируем

vlan_ids = sorted(list(vlans1_set.intersection(vlans2_set)))

# Выводим на экран результат.
print('-' * 70, '\n')
print(vlan_ids, '\n')
print('-' * 70, '\n')
