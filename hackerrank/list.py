#!/usr/bin/python

if __name__ == '__main__':
    N = int(raw_input())

    l = []
    for i in range(0,N):
        str_input = raw_input()
        str = str_input.split(' ')
        if str[0] == "insert":
            l.insert(int(str[1]), int(str[2]))
        elif str[0] == "print":
            print l
        elif str[0] == "remove" :
            l.remove(int(str[1]))
        elif str[0] == "append" :
            l.append(int(str[1]))
        elif str[0] == "sort" :
            l.sort()
        elif str[0] == "pop" :
            l.pop(len(l)-1)
        elif str[0] == "reverse" :
            l.reverse()