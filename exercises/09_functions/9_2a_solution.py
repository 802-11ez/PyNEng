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

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    result_trunk_config_d = dict.fromkeys(list(trunk_config.keys()))
    for key in result_trunk_config_d.keys():
        result_trunk_config_d[key] = []
        for line in trunk_mode_template:
            if line.endswith('allowed vlan'):
                vlans = trunk_config[key]
                for i in vlans: vlans[vlans.index(i)] = str(i)
                result_trunk_config_d[key].append(line + ' ' + ','.join(vlans))
            else:
                result_trunk_config_d[key].append(line)
    return result_trunk_config_d

result_trunk_config_d = generate_trunk_config(trunk_config, trunk_mode_template)
pprint(result_trunk_config_d)
