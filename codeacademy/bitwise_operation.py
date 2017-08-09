#!/usr/bin/python

# slip and slide
def flip_bit(number,n):
    mask = 0b1 << (n-1)
    result = number ^ mask
    return bin(result)
    
print flip_bit(10,3)

#flip bit
a = 0b11101110
mask = 0b11111111
des = a ^ mask
print bin(des)

# bit mask
def check_bit4(input):
    if (input & 0b00001000)>0 :
        return "on"
    else:
        return "off"