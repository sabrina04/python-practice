"""You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer."""

#!/usr/bin/python

l = [] 
n = int(raw_input())
if n>0 and n<100:
    l = raw_input().split()

    if all([int(i)>0 for i in l]) and any([j==j[::-1] for j in l]):
        print 'True'
    else:
        print 'False'