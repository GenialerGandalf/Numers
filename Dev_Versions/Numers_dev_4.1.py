# -*- coding: iso-8859-2 -*-

import random
a = -1
b = 0
c = 8
m = 0
extra = ''
A = [0, 1, 2, 3, 4, 5, 6, 7, 8]
while a != 0:
    a = random.randint(0,c)
    a = A[a]
    A.remove(a)                                                     #Error 003: a is not suscriptable (fixed dev_3.0)
    if a > 4 and a < 7:
        b = b * (a - 3)
    elif a == 7:
        b = b ** 2
    elif a == 8:
        b = 0
        m = 1
    elif a == 0:
        break
    else:
        b = b + a
    b = str(b)
    if a == 0:
        extra = 'x'
    elif a > 0 and a < 5:
        extra = '+'
    elif a > 4 and a < 7:
        extra = 'x'
        a = a - 3
    elif a == 7:
        extra = '^'
        a = 2
    elif a == 8:
        extra = 'x'
        a = 0
    a = str(a)
    if b == '1':
        print ('(' + extra  +' '+ a + ' ) --> ' + b +' point')
    else:
        print ('(' + extra  +' '+ a + ' ) --> ' + b +' points')         #Error 001: a gave +1 at beginning (fixed dev_1.3-a)                                            
    a = int(a)
    b = int(b)
    c = c - 1
    if m == 1:
        m = 0
        a = 1
    continue
if b == 1:
    b = str(b)
    print ('Game over! You scored 1 point!')                        #Error 002: b = 1 still plural point (fixed dev_2.0)
elif b > 36:
    b = str(b)
    print ('Game over! You scored ' + b + ' points!')               #Error 000: b was no str (fixed dev_1.0)
    print ('You are allowed to get to the next level!')
elif b == 0:
    b = str(b)
    print ('Game over! You scored 0 points!')
    print ('This is unlucky, try again.')
else:
    b = str(b)
    print ('Game over! You scored ' + b + ' points!')
