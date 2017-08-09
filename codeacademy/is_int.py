#!/usr/bin/python

def is_int(x):
    if abs(x-round(x))>0 :
        return False
    else:
        return True

is_int(-2.6)