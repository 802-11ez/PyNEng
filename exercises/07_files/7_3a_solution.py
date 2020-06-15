#!/usr/bin/env python3

from pprint import pprint

mac_l = []
mac_sort_l = []
mac_vlans_l = []

with open('CAM_table.txt') as file:
    for line in file:
        if line.find('DYNAMIC') != -1:
            mac_l.append(line.split())

for k in mac_l:
    idx = mac_l.index(k)
    mac_vlans_l.append(int(mac_l[idx][0]))

mac_vlans_l = sorted(mac_vlans_l)

for i in mac_vlans_l:
    for m in mac_l:
        if int(m[0]) == i:
            mac_sort_l.append(m)
            mac_l.pop(mac_l.index(m))

print('-' * 50)
for a in mac_sort_l:
    vlan_id, mac, _, intf = a
    print(' {:<7}{:<18}{:}'.format(vlan_id, mac, intf))
print('-' * 50)
