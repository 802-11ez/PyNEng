#!/usr/bin/env python3

from pprint import pprint

vlan_id_entered = input('Введите номер VLAN: ')

mac_l = []

with open('CAM_table.txt') as file:
    for line in file:
        if line.find('DYNAMIC') != -1:
            vlan_id, mac, _, intf = line.split()
            mac_l.append([vlan_id, mac, intf])

print('-' * 32)
for i in mac_l:
    if i[0] == vlan_id_entered:
        print(' {:<7}{:<18}{:<8}'.format(i[0], i[1], i[2]))
print('-' * 32)
