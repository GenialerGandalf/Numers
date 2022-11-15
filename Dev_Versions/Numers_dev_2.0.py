# -*- coding: iso-8859-2 -*-

import random
a = -1
b = 0
c = 8
while a != 0:
    if a == -1:
        a = 0
    b = str(b)
    a = str(a)
    if b == '1':
        print ('(+' + a + ') --> ' + b +' point')
    else:
        print ('(+' + a + ') --> ' + b +' points')          #Error 001: a gave +1 at beginning (fixed dev_1.3-a)                                            
    a = int(a)
    b = int(b)
    a = random.randint(0,c)
    b = b + a
    c = c - 1
    continue
b = str(b)
if a == 1:
    print ('Game over! You scored 1 point!')                #Error 002: b = 1 still plural point (fixed dev_2.0)
else:
    print ('Game over! You scored ' + b + ' points!')       #Error 000: b was no str (fixed dev_1.0)
 
    
