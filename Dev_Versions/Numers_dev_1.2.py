# -*- coding: iso-8859-2 -*-

import random
a = 1
b = 0
c = 8
while a != 0:
    b = str(b)
    print (b + ' points')
    b = int(b)
    a = random.randint(0,c)
    b = b + a
    c = c - 1
    continue
b = str(b)
print ('Game over! You scored ' + b + ' points!') #Error 000: b was no str (fixed dev_1.0)
    
