#!/usr/bin/env python3

from sys import argv

file_name = argv[1]

with open(file_name) as file:
    for line in file:
        if not line.startswith('!'):
            print(line.rstrip())
