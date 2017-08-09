#!/usr/bin/python

from __future__ import print_function
import sys

if __name__ == '__main__':
    n = int(raw_input())

    for i in range(1,n+1) :
        print(i,sep='',end='',file=sys.stdout)
        
        