# -*- coding: iso-8859-2 -*-

import random
a = 1
b = 0

while a != 0:
    print (b)
    a = random.randint(0,8)
    b = b + a
print ('Game over! You scored ' +  b + ' points!')
    
