#!/usr/bin/env python3

from pprint import pprint

mac_l = []

with open('CAM_table.txt') as file:
    for line in file:
        if line.find('DYNAMIC') != -1:
            vlan_id, mac, _, intf = line.split()
            mac_l.append([vlan_id, mac, intf])

print('-' * 32)
for i in mac_l:
        print(' {:<7}{:<18}{:<8}'.format(i[0], i[1], i[2]))
print('-' * 32)
