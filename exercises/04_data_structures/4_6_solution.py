#!/usr/bin/env python3
print('''
Задание 4.6
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
    Protocol:              OSPF
    Prefix:                10.0.24.0/24
    AD/Metric:             110/41
    Next-Hop:              10.0.13.3
    Last update:           3d18h
    Outbound Interface:    FastEthernet0/0
Ограничение: Все задания надо выполнять используя только пройденные темы.
''')

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

for char in [',', '[', ']']:
        ospf_route = ospf_route.replace(char, '')

print('-' * 70)
print('The best way by using the methods str.replace(), str.replace() and str.format().')
print('-' * 70, '\n')

ospf_route = ospf_route.replace('O', 'OSPF')
#print(ospf_route)

ospf_route = ospf_route.split()

#print(ospf_route)

template = '''
Protocol           : {0}
Prefix             : {1}
AD/Metric          : {2}
Next-Hop           : {3}
Last update        : {4}
Outbound Interface : {5}
'''
print('-' * 70,)
print(template.format(ospf_route[0], ospf_route[1], ospf_route[2], ospf_route[4], ospf_route[5], ospf_route[6]))
print('-' * 70, '\n')
