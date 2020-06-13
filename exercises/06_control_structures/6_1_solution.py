#!/usr/bin/env python3

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']

mac_cisco = [i.replace(':', '.') for i in mac]

template_mac = '{:>16} : {:<18}'

print('-' * 70)
for i in mac:
    idx = mac.index(i)
    print(template_mac.format('Original MAC', i))
    print(template_mac.format('CiscoLike MAC', mac_cisco[idx]))
print('-' * 70, '\n')
