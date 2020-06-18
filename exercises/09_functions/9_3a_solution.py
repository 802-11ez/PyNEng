#!/usr/bin/env python3

from pprint import pprint

def get_int_vlan_map(config_filename):
    with open(config_filename) as file:
        interfaces_t = ()
        interfaces_access_d = {}
        interfaces_trunk_d = {}
        for line in file:
            if 'interface ' in line:
                key = line.split()[-1]
            elif 'mode access' in line:
                interfaces_access_d[key] = 1
            elif 'access vlan' in line:
                vlan_ids = line.split()[-1]
                interfaces_access_d[key] = int(vlan_ids)
            elif 'trunk allowed vlan' in line:
                vlan_ids = line.split()[-1]
                vlan_ids_l = vlan_ids.split(',')
                for i in vlan_ids_l: vlan_ids_l[vlan_ids_l.index(i)] = int(i)
                interfaces_trunk_d[key] = vlan_ids.split(',')
        interfaces_t = (interfaces_access_d, interfaces_trunk_d)
    return interfaces_t

pprint(get_int_vlan_map('config_sw2.txt'))
