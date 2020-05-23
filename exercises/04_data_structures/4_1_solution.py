#!/usr/bin/env python
print('''
Задание 4.1
Обработать строку nat таким образом,
чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.
Ограничение: Все задания надо выполнять используя только пройденные темы.
''')

print('-' * 70)
print('The best way by using the method str.replace().')
print('-' * 70, '\n')

nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload'
nat_gi = nat.replace('FastEthernet', 'GigabitEthernet')
print(nat, '\n')

print(nat_gi, '\n')
print('-' * 70, '\n')
