""" Given a string, , of length that is indexed from to , print its even-indexed and odd-indexed characters as space-separated 2 strings on a single line """


#!/usr/bin/python

t = int(raw_input())

if t>=1 and t<=10:
    str1,temp1,temp2 = '','',''
    even, odd = [],[]

    for i in range(t):
        str1 = raw_input()
        for j in range(len(str1)):
            if j%2==0:
                temp1 += str1[j]
            else:
                temp2 += str1[j]

        even.append(temp1)
        odd.append(temp2)
        str1,temp1,temp2 = '','',''

    j=0
    for i in range(t):
        print even[j],
        print odd[j]
        j += 1