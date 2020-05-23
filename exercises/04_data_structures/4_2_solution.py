#!/usr/bin/env python
print('''
Задание 4.2
Преобразовать строку mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX
Ограничение: Все задания надо выполнять используя только пройденные темы.
''')

print('-' * 70)                                                                                                         
print('The best way by using the method str.replace().')                                                                
print('-' * 70, '\n')

mac = 'AAAA:BBBB:CCCC'
mac_doted = mac.replace(':', '.')

print('mac       :', mac, '\n')
print('mac_doted :', mac_doted, '\n')
print('-' * 70, '\n')
