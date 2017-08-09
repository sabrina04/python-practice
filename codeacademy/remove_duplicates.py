#!/usr/bin/python

def remove_duplicates(l):
    res = list(set(l))
    return res

print remove_duplicates([1,1,1,3,4,2])