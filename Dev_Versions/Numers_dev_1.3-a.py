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
    print (b + ' points (+' + a + ')')              #Error 001: a gave +1 at beginning
    a = int(a)
    b = int(b)
    a = random.randint(0,c)
    b = b + a
    c = c - 1
    continue
b = str(b)
print ('Game over! You scored ' + b + ' points!')   #Error 000: b was no str (fixed dev_1.0)
    
