# -*- coding: iso-8859-2 -*-

import random
a = -1
b = 0
c = 8
m = 0
extra = ''
n1 = False
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
    r = input('press enter to go on')
    continue
if b == 1:
    b = str(b)
    print ('Game over! You scored 1 point!')                        #Error 002: b = 1 still plural point (fixed dev_2.0)
elif b > 100:
    b = str(b)
    print ('Game over! You scored ' + b + ' points!')               #Error 000: b was no str (fixed dev_1.0)
    print ('You are allowed to get to the next level!')
    n1 = True
elif b == 100:
    b = str(b)
    print ('Game over! You scored ' + b + ' points!')
    print ('EXACT HIT! Achievments... will be added soon!')
    print ('You are barely allowed to get to the next level!')
elif b == 0:
    b = str(b)
    print ('Game over! You scored 0 points!')
    print ('This is unlucky, try again.')
else:
    b = str(b)
    print ('Game over! You scored ' + b + ' points!')

if n1 == True:
    print ("This is the next level, it's a modified version of the very first numers.")
    a2 = 1
    poss = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,7,7,7,7,10,10,10,10,13,13,13,13,16,16,16,16,20,20,20,20,30,30,30,30,60,60,90,90,200,200,400,0]
    rest = [8,8,8,8,8,8,8,8]
    f = 8
    while a2 == 1:
        des = rand
        dop = random.randint(0,f)
        print (dop)
        
    
