"""Your task is to sort the string in the following manner:
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
"""


from __future__ import print_function

s = raw_input()
s_list = sorted(s, key = lambda x: (x.isdigit() and int(x)%2==0, x.isdigit(), x.isupper(),x.islower(), x))
print(*s_list, sep='')