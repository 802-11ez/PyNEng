#!/usr/bin/env python3

from pprint import pprint

access_mode_template = ['switchport mode access', 'switchport access vlan',
                        'switchport nonegotiate', 'spanning-tree portfast',
                        'spanning-tree bpduguard enable'
                       ]

port_security_template = ['switchport port-security maximum 2',
                          'switchport port-security violation restrict',
                          'switchport port-security'
                         ]

access_config = {'FastEthernet0/12': 10,
                 'FastEthernet0/14': 11,
                 'FastEthernet0/16': 17
                }

def generate_access_config(intf_vlan_mapping, access_template, psecurity = None):
    '''
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    '''
    result_access_config_l = []
    
    for key, value in intf_vlan_mapping.items():
        result_access_config_l.append('interface ' + key)
        for i in access_mode_template:
            if i.endswith('access vlan'):
                result_access_config_l.append(i + ' ' + str(value))
            else:
                result_access_config_l.append(i)
        if psecurity != None:
            for p in psecurity:
                result_access_config_l.append(p)
    return result_access_config_l

result_access_config_l = generate_access_config(access_config, access_mode_template, port_security_template)

pprint(result_access_config_l)
