"""The first line contains and separated by a space.
The next lines contains the space separated marks obtained by students in a particular subject. Print the averages of all students on separate lines.Print the averages of all students on separate lines."""

#!/usr/bin/python

n,x = map(int, raw_input().split())
l = []
for i in range(x):
    l.append(map(float, raw_input().split()))
    
for i in zip(*l):
    print sum(i)/len(i)