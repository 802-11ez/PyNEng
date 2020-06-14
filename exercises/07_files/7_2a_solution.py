#!/usr/bin/env python3

from sys import argv

file_name = argv[1]
ignore = ['duplex', 'alias', 'Current configuration']

with open(file_name) as file:
    for line in file:
        if not any(line.find(symb) != -1 or line.startswith('!') for symb in ignore):
            print(line.rstrip())
