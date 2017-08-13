""" You are given data in a tabular format. The data contains rows, and each row contains space separated elements. Your task is to sort the table on the th attribute and print the final resulting table. """

#!/usr/bin/python

n,m = map(int, raw_input().split())
l = []
for i in range(n):
    l.append(map(int, raw_input().split()))
k = int(raw_input())
sorted_list = sorted(l, key=lambda x: int(x[k]))

for line in sorted_list:
    for item in line:
        print item,
    print 