#!/usr/bin/env python3
from pprint import pprint

ospf_route_l = []

with open('ospf.txt') as file:
    for line in file:
        ospf_route_l.append(line)

template = '''Protocol           : {0}
Prefix             : {1}
AD/Metric          : {2}
Next-Hop           : {3}
Last update        : {4}
Outbound Interface : {5}'''

for i in ospf_route_l:
    idx = ospf_route_l.index(i)
    i = i.replace('O', 'OSPF')
    for char in [',', '[', ']']:
        i = i.replace(char, '')
    i = i.strip()
    protocol, prefix, ad, _, nexthop, l_update, intf = i.split()
    print('-' * 70,)
    print(template.format(protocol, prefix, ad, nexthop, l_update, intf))
    print('-' * 70, '\n')
