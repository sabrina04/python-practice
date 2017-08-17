#!/usr/bin/python

import sys
import re

n = int(raw_input().strip())
binary = bin(n)[2:]

prog = re.compile('1+')
result = prog.findall(binary)

max_len = 0

for one in result:
    if(max_len<len(one)):
        max_len = len(one)

print max_len 