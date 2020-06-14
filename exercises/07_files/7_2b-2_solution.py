#!/usr/bin/env python3

from sys import argv

file_name = argv[1]

ignore = ['duplex', 'alias', 'Current configuration']
cleared_cfg_l = []

with open(file_name) as src, open('config_sw1_cleared_2.txt', 'w') as dst:
    for line in src:
        if not any(line.find(symb) != -1 or line.startswith('!') for symb in ignore):
            dst.write(line)
