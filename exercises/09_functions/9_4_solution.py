#!/usr/bin/env python3

from pprint import pprint

def get_int_vlan_map(config_filename):
    with open(config_filename) as file:
        ignore = ['duplex', 'alias', 'Current configuration']
        ignore_2 = ['!', '\n', 'end']
        interfaces_cfg_d = {}
        commands_exec = []
        commands_intf_l = ['switchport', 'ip address']
        commands_line_l = ['exec-timeout', 'privilege', 'logging', 'login', 'transport']
        for line in file:
            if not any(line.find(symb) != -1 or line.startswith('!') or line.startswith('\n') or line.startswith('end') for symb in ignore):
                if not any(s in line for s in commands_intf_l) and not any(w in line for w in commands_line_l):
                    key = line.strip()
                    interfaces_cfg_d[key] = []
                elif any(s in line for s in commands_intf_l):
                    interfaces_cfg_d[key].append(line.strip())
                elif any(s in line for s in commands_line_l):
                    interfaces_cfg_d[key].append(line.strip())
    return interfaces_cfg_d

pprint(get_int_vlan_map('config_sw1.txt'))
