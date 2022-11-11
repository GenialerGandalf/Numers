# -*- coding: iso-8859-2 -*-

import random, time
go = 'y'
while go == 'y':
    a = -1
    b = 0
    c = 8
    m = 0
    extra = ''
    n1 = False
    A = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while a != 0:
        time.sleep(0.5)
        a = random.randint(0,c)
        a = A[a]
        A.remove(a)             #Error 003: a is not suscriptable (fixed dev_3.0)
        if a > 4 and a < 7:
            b = b * (a - 3)
        elif a == 7:
            b = b ** 2
        elif a == 8:
            b = b + 5
        elif a == 0:
            break
        else:
            b = b + a
        b = str(b)
        if a == 0:
            break
        elif a > 0 and a < 5:
            extra = '+'
            a = a 
        elif a > 4 and a < 7:
            extra = 'x'
            a = a - 3
        elif a == 7:
            extra = '^'
            a = 2
        elif a == 8:
            extra = '+'
            a = 5
        a = str(a)
        if b == '1':
            print ('(' + extra  +' '+ a + ') --> ' + b +' point')
        else:
            print ('(' + extra  +' '+ a + ') --> ' + b +' points')         #Error 001: a gave +1 at beginning (fixed dev_1.3-a)                                            
        a = int(a)
        b = int(b)
        c = c - 1
        continue
    if b == 1:
        b = str(b)
        print ('Game over! You scored 1 point!')                        #Error 002: b = 1 still plural point (fixed dev_2.0)
    elif b == 99:
        print ('Game over! You scored 99 points!')
        print ('Close Call! -be 1 point short')
        print ('You are barely not allowed to get to the next level')
    elif b == 42:
        print ('Game over! You scored 42 points!')
        print ('How do you win?')
        print ('42!')
        print ('Eh, I lost with 42...')
        print ('But 42 is always the answer.')
        print ('Sure?')
        print ('42!')
        print ('Bye.')
        print ('Bye.')
    elif b == 69:
        print ('Heh... :) ')
    elif b == 3600:
        b = str(b)
        print ('Game over! You scored ' + b + ' points!')
        print ('Max points! Wow you are lucky!')
    elif b == 100:
        b = str(b)
        print ('Game over! You scored ' + b + ' points!')
        print ('EXACT HIT! Achievements... will be added soon!')
        print ('You are barely allowed to get to the next level!')
        n1 = True
    elif b > 99:
        b = str(b)
        print ('Game over! You scored ' + b + ' points!')               #Error 000: b was no str (fixed dev_1.0)
        print ('You are allowed to get to the next level!')
        n1 = True
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
        q = 0
        poss = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,7,7,7,7,10,10,10,10,13,13,13,13,16,16,16,16,20,20,20,20,30,30,30,30,60,60,90,90,200,200,400,0]
        rest = [8,8,8,8,8,8,8,8]
        f = 7
        g = 64
        while a2 == 1:
            L2 = False
            s = "s"
            g = g - 1
            dop = random.randint(0,f)
            mop = random.randint(0,g)
            hop = random.randint(0,rest[dop])
            if hop == 0:
                a2 = 0
                break
            rest[dop] = rest[dop] - 1
            nop = poss[mop]
            poss.remove(poss[mop])                                      #Error 004:remove(x) not working (fixed alpha_1.4)
            if nop == 0:
                q = 0
                zu = "*"
                x = 0
            if nop < 20 and nop > 0:
                q = q + nop
                zu = "+"
                x = nop
            elif nop < 200 and nop > 19:
                x = int(nop / 10)
                q = q * x
                zu = "*"
            elif nop > 199:
                x = int(nop / 100)
                q = q ** x
                zu = "^"
            if q == 1:
                s = ""
            q = int(q)
            print ("You got a " + str(hop))
            print ("(" + zu + " " + str(x) + ") --> " + str(q) + " point" + s)
            r = input ('press enter to go on')
            
        if q == 0:
            b = str(b)
            print ('Game over! You scored 0 points!')
            print ('This is unlucky, try again.')
        elif q < 999999999:
            b = str(b)
            print ('Game over! You scored ' + str(q) + ' points!')
        elif q == 999999999:
            b = str(b)
            print ('Game over! You scored 999999999 points!')
            print ('Close Call II')
            print ('You are barely not allowed to go to the next level')
        elif q == 1000000000:
            b = str(b)
            print ('Game over! You scored 1000000000 points!')
            print ('You are barely allowed to go to the next level!')
            L2 = True
        elif q > 1000000000:
            b = str(b)
            print ('Game over! You scored ' + str(q) + ' points!')
            print ('You are allowed to go to the next level!')
            L2 = True
        if L2 == True:
            print ('This is the planned Numers 2.0')
            print ('Today it should show the great viarity of numers u can have.')
            
        
    print ('Wanna try another time? (y|n)')
    go = input('>>> ')
