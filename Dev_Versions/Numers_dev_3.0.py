# -*- coding: iso-8859-2 -*-

import random
a = -1
b = 0
c = 8
A = [0, 1, 2, 3, 4, 5, 6, 7, 8]
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
    a = A[a]
    A.remove(a)                                             #Error 003: a is not suscriptable (fixed dev_3.0)
    b = b + a
    c = c - 1
    continue
if b == 1:
    b = str(b)
    print ('Game over! You scored 1 point!')                #Error 002: b = 1 still plural point (fixed dev_2.0)
elif b < 36:
    b = str(b)
    print ('Game over! You scored ' + b + ' points!')       #Error 000: b was no str (fixed dev_1.0)
    print ('You are allowed to get to the next level!')
elif:
    b = str(b)
    print ('Game over! You scored 0 points!')
    print ('This is unlucky, try again.')
