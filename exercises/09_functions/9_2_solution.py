#!/usr/bin/env python3

from pprint import pprint

trunk_mode_template = ['switchport mode trunk',
                       'switchport trunk native vlan 999',
                       'switchport trunk allowed vlan'
                      ]

trunk_config = {'FastEthernet0/1': [10, 20, 30],
                'FastEthernet0/2': [11, 30],
                'FastEthernet0/4': [17]
               }

result_trunk_config_l = []

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    for intf, vlans in intf_vlan_mapping.items():
        result_trunk_config_l.append('interface ' + intf)
        for line in trunk_template:
            if line.endswith('allowed vlan'):
                for i in vlans: vlans[vlans.index(i)] = str(i)
                result_trunk_config_l.append(line + ' ' + ','.join(vlans))
            else:
                result_trunk_config_l.append(line)
    return result_trunk_config_l

result_trunk_config_l = generate_trunk_config(trunk_config, trunk_mode_template)
pprint(result_trunk_config_l)
