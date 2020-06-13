#!/usr/bin/env python3
print('''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима, задавались разные вопросы в запросе о номере VLANа или списка VLANов:
  * для access: 'Введите номер VLAN:'
  * для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
''')

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

int_mode = input('Введите режим работы интерфейса (access/trunk): ')
int_id = input('Введите тип и номер интерфейса: ')
vlan_ids = input('Введите номер влан(ов): ')

template = {'access': ['switchport mode access', 'switchport access vlan {}',
                       'switchport nonegotiate', 'spanning-tree portfast', 
                       'spanning-tree bpduguard enable'],
            'trunk': ['switchport trunk encapsulation dot1q', 'switchport mode trunk',
                      'switchport trunk allowed vlan {}']
           }

#print(template.get(int_mode.lower(), 'Такого параметра нет'))
print('-' * 70, '\n')
print('interface ', int_id)
print('\n'.join(template.get(int_mode.lower())).format(vlan_ids), '\n')
print('-' * 70, '\n')
