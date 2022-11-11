# -*- coding: iso-8859-2 -*-

import random, time, pygame
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
        print ('Heh... :) Noice')
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
        g = 64
        while a2 == 1:
            L2 = False
            s = "s"
            g = g - 1
            f = 8
            dop = random.randint(1,f)
            kop = random.randint(0,rest[dop-1])                         #Error 005:IndexError: list index out of range (fixed alpha_2.3)
            mop = random.randint(0,g)
            hop = dop
            if kop == 1:
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
            print ('Today it should show the great viarity of values u can have. And there will be added even more!')
            Alle = [-163840000000000,-128000000000,-128000000000,-128000000000,-960000000,-480000000,-480000000,-480000000,-240000000,-240000000,-240000000,-240000000,-240000000,-120000000,-120000000,-120000000,-120000000,-120000000,-120000000,-120000000,-60000000,-50000000,-50000000,-50000000,-40000000,-40000000,-40000000,-40000000,-40000000,-30000000,-30000000,-30000000,-30000000,-30000000,-30000000,-30000000,-20000000,-20000000,-20000000,-20000000,-20000000,-20000000,-20000000,-20000000,-20000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-1048576,-1024,-1024,-1024,-512,-256,-256,-256,-128,-128,-128,-128,-128,-64,-64,-64,-64,-64,-64,-64,-32,-28,-28,-28,-24,-24,-24,-24,-24,-20,-20,-20,-20,-20,-20,-20,-16,-16,-16,-16,-16,-16,-16,-16,-16,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-8,-7,-7,-7,-6,-6,-6,-6,-6,-5,-5,-5,-5,-5,-5,-5,-4,-4,-4,-4,-4,-4,-4,-4,-4,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,15,15,15,15,15,15,15,15,22,22,22,22,22,22,22,22,29,29,29,29,29,29,29,29,36,36,36,36,36,36,36,36,43,43,43,43,43,43,43,43,50,50,50,50,50,50,50,50,57,57,57,57,57,57,57,57,64,64,64,64,64,64,64,64,128,128,128,128,128,128,128,192,192,192,192,192,192,192,256,256,256,256,256,256,256,320,320,320,320,320,320,320,384,384,384,384,384,384,384,448,448,448,448,448,448,448,512,512,512,512,512,512,512,1000,1000,1000,1000,1000,1000,2000,2000,2000,2000,2000,2000,3000,3000,3000,3000,3000,3000,4000,4000,4000,4000,4000,4000,5000,5000,5000,5000,5000,5000,6000,6000,6000,6000,6000,6000,12000,12000,12000,12000,12000,18000,18000,18000,18000,18000,24000,24000,24000,24000,24000,30000,30000,30000,30000,30000,36000,36000,36000,36000,36000,81000,81000,81000,81000,126000,126000,126000,126000,171000,171000,171000,171000,216000,216000,216000,216000,2000000,2000000,2000000,3000000,3000000,3000000,4000000,4000000,4000000,10000000,10000000,16000000,16000000,64000000,"^1","x0","x-1","x-2","-3","-2","-1","1","2","3","inx","iny","inz","ina","rb","rc","(i)","t","-4t","-3t","-2t","-1t","0t","1t","2t","3t","4t","l+n","l+n","l+n","lxn","lxn","l^n","l?n","^(-1)","^(-1)","^(-1)","x(-1)","x(-1)","x(-1)","x0","^0","/0","l"]
            rest1 = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
            rest2 = [64,64,64,64,64,64,64,64]
            rest3 = 512
            l = 64
            k = 7
            while a2 == 1:
                L2 = False
                s = "s"
                rest3 = rest3 - 1
                aop = random.randint(0,k)
                bop = random.randint(0,l)
                cop = random.randint(0,rest3)
                eop = aop
                fop = eop
                gop = random.randint(0,)
                if hop == 0:
                    a2 = 0
                    break
            
    print ('Wanna try another time? (y|n)')
    go = input('>>> ')


