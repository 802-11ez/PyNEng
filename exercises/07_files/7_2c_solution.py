#!/usr/bin/env python3

from sys import argv

src_file_name = argv[1]
dst_file_name = argv[2]

ignore = ['duplex', 'alias', 'Current configuration']
cleared_cfg_l = []

with open(src_file_name) as src, open(dst_file_name, 'w') as dst:
    for line in src:
        if not any(line.find(symb) != -1 or line.startswith('!') for symb in ignore):
            dst.write(line)
