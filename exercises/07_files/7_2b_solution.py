#!/usr/bin/env python3

from sys import argv

file_name = argv[1]

ignore = ['duplex', 'alias', 'Current configuration']
cleared_cfg_l = []

with open(file_name) as file:
    for line in file:
        if not any(line.find(symb) != -1 or line.startswith('!') for symb in ignore):
            cleared_cfg_l.append(line.rstrip())

with open('config_sw1_cleared.txt', 'w') as file:
    for i in cleared_cfg_l:
        file.write(i + '\n')
