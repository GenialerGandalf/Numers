# -*- coding: iso-8859-2 -*-

import random, time, pygame, sys #eclipse for launch without download, or hello world 

def Changelog(screen, down):
    Version = [["dev-0.0", "add: iso-codeline"],
               ["dev-0.1", "add: random import"],
               ["dev-0.2", "add: random print 0-8"],
               ["dev-0.3", "add: 0 = Game over"],
               ["dev-0.4", "add: point display"],
               ["dev-0.5", "add: final score print"],
               ["dev-1.0", "fix: final score print"],
               ["dev-1.1", "add: remove 1 every round"],
               ["dev-1.2", "add: 'points' behind the points"],
               ["dev-1.3", "add: points of round print"],
               ["dev-1.3-a", "fix: first round has a +1"],
               ["dev-2.0", "fix: not a singular for 1 point"],
               ["dev-3.0", "fix: every result only once"],
               ["dev-4.0", "fix: dev-3.0 not finished", "add: multipliers, ^2"],
               ["dev-4.1", "fix: broken return of multipliers"],
               ["dev-5.0", "add: enter to get next draw"]
               ]
    screen.fill([0, 0, 0])
    deve = 1
    line = 0
    T = [None, 100, "Changelog", True, 255, 255, 255, hintergrund.get_width()/2, hintergrund.get_height()/16]
    screen = Texts(T)
    T = [None, 75, "Early development", True, 255, 255, 127, hintergrund.get_width()/2, hintergrund.get_height()/8 + 20]
    screen = Texts(T)
    for dev in range(0, len(Version)):
        sub = Version[len(Version)-dev-1]
        if hintergrund.get_height()/8 + 45 + 60*dev + 30*(line+1) - down*25 > hintergrund.get_height()/8 + 50:
            T = [None, 50, sub[0], True, 255, 255, 0, hintergrund.get_width()/2, hintergrund.get_height()/8 + 45 + 60*dev + 30*(line+1) - down*25]
            screen = Texts(T)
        if len(sub) > 0:
            for deve in range(1, len(sub)):
                if deve > 1:
                    line = line + 1
                if hintergrund.get_height()/8 + 40 + 60*dev + 30*(line+2) - down*25 > hintergrund.get_height()/8 + 50:
                    T = [None, 25, sub[deve], True, 127, 255, 0, hintergrund.get_width()/2, hintergrund.get_height()/8 + 40 + 60*dev + 30*(line+2) - down*25]
                    screen = Texts(T)
    return screen, down

def Return(go):
    go = "°"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = "n"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                go = 'y'
            elif event.key == pygame.K_UP:
                go = "up"
            elif event.key == pygame.K_DOWN:
                go = "down"
            elif event.key == pygame.K_RIGHT:
                go = "right"
            elif event.key == pygame.K_LEFT:
                go = "left"
            elif event.key == pygame.K_ESCAPE:
                go = "esc"
    return go

def Calcul1000(cent):
    cal, ten, mil, deci, centi = cent, 0, 0, 0, 0
    while cent > 10 or cent < -10:
        while cent >= 1000 or cent <= -1000:
            cent, mil = cent / 1000, mil + 1
        if cent > 10 or cent < -10:
            cent, ten = cent / 10, ten + 1
    while mil >= 10:
        deci = deci + 1
        mil = mil - 10
    while deci >= 10:
        centi = centi + 1
        deci = deci - 10
    MIL, DECI, CENTI = ["","M","B","T","Q","q","S","s","O" ,"N"], ["","De","Vi","Tr","Qu","qu","Se","se","Ok","No"], ["","Cen","Duc","Tre","Qua","Qui","Ses","Sep","Oct","Non"]
    kar = MIL[mil] + DECI[deci] + CENTI[centi]
    mil = mil + deci*10 + centi*100
    return kar, ten, mil, cent

def Rlsview(A):
    if len(A) > 0:
        B1 = "["
    else:
        B1 = ""
    for lena in range (0, len (A)):
        if A[lena] == 0:
            B1 = B1 + "Game Over"
        if A[lena] == 1:
            B1 = B1 + "+1"
        if A[lena] == 2:
            B1 = B1 + "+2"
        if A[lena] == 3:
            B1 = B1 + "+3"
        if A[lena] == 4:
            B1 = B1 + "+4"
        if A[lena] == 5:
            B1 = B1 + "+5"
        if A[lena] == 6:
            B1 = B1 + "*2"
        if A[lena] == 7:
            B1 = B1 + "*3"
        if A[lena] == 8:
           B1 = B1 + "^2"
        if lena != len(A)-1:
            B1 = B1 + ", "
        else:
            B1 = B1 + "]"
    B1 = str(B1)
    font = pygame.font.Font(None, 96)
    text = font.render((B1), True, (255, 255, 0))
    textpos = text.get_rect(centerx = screen.get_width()/2, y = 700)
    screen.blit(text, textpos)

def Ptsview(b,extra,a,notthird,goal,A):
    global nah
    cent = int(b)
    kar, ten, mil, cent = Calcul1000(cent)
    rz, wz, mn1, p0 = 255, 0, 1, 140
    screen.fill([0, 0, 0])
    Rlsview(A)
    if cent + cent < cent:
        rz, wz, p0, mn1 = 0, 255, 1140, -1
    yik = p0 + int(int(b)*100/((10**ten)*(1000**mil)))
    line = pygame.draw.rect(screen, (255, rz, rz), (p0*rz/255, 390, 1140, 5))
    for dec in range(0, 12):
        if dec == 10 or dec == 0:
            mark = pygame.draw.rect(screen, (255, rz, rz), ((p0 - 2 + mn1 * 100 * dec), 375, 5, 35))
        mark = pygame.draw.rect(screen, (255, rz, rz), ((p0 - 1 + mn1 * 100 * dec), 380, 3, 25))
    if notthird == False:
        mark = pygame.draw.rect(screen, (255, wz, wz), (p0 - 140*rz/255, 390, 138, 5))
        mark = pygame.draw.rect(screen, (255, wz, wz), (p0 - 100 * mn1 - 1, 380, 3, 25))
        font = pygame.font.Font(None, 40)
        text = font.render(str(-1 * mn1 * (10**ten)) + kar, True, (255, wz, wz))
        textpos = text.get_rect(centerx = p0 - 100 * mn1, y = 420)
        screen.blit(text, textpos)
        for dec in range(0, 115):
            mark = pygame.draw.rect(screen, (255, rz, rz), (((140*rz/255) + 10 * dec), 385, 1, 15))
        for dec in range(1, 16):
            mark = pygame.draw.rect(screen, (255, wz, wz), ((p0 - 10 * dec * mn1), 385, 1, 15))
    for dec in range(0, 12):
        if rz == 0:
            dec = 0 - dec
        font = pygame.font.Font(None, 40)
        text = font.render(str(dec * (10**ten)) + kar, True, (255, rz, rz))
        textpos = text.get_rect(centerx = p0 + dec * 100, y = 420)
        screen.blit(text, textpos)
    if ten + mil > 0 and notthird == True:
        for dec in range(0, 115):
            mark = pygame.draw.rect(screen, (255, rz, rz), ((140 + 10 * dec), 385, 1, 15))
    line = pygame.draw.rect(screen, (0, 0, 255), (p0 - p0*wz/255 + yik*wz/255, 391, yik-140, 3))
    pygame.draw.polygon(screen, (0,255,0), ([yik-8,350],[yik,370],[yik+8,350]))
    font = pygame.font.Font(None, 40)
    text = font.render(str(b), True, (0, 255, 0))
    textpos = text.get_rect(centerx = yik, y = 320)
    screen.blit(text, textpos)
    font = pygame.font.Font(None, 40)
    if int(b) <= goal/10 and goal != 10:
        text = font.render("Goal: " + str(goal), True, (255, 255, 255))
        pygame.draw.polygon(screen, (255,255,255), ([1220,270],[1220,290],[1240,280]))
    elif int(b) >= goal:
        text = font.render("Goal: " + str(goal), True, (0, 255, 0))
    else:
        text = font.render("Goal: " + str(goal), True, (255, 255, 255))
        pygame.draw.polygon(screen, (255,255,255), ([1130,300],[1140,320],[1150,300]))
    textpos = text.get_rect(right = 1200, centery = 280)
    screen.blit(text, textpos)
    if extra != "a":
        font = pygame.font.Font(None, 100)
        text = font.render((str(extra) + " " + str(a)), True, (0, 255, 255))
        textpos = text.get_rect(centerx = 640, y = 200)
        screen.blit(text, textpos)
    nah = int(b)
    pygame.display.flip()

def Texts(T):
    font = pygame.font.Font(T[0], T[1])
    text = font.render(T[2], T[3], (T[4], T[5], T[6]))
    textpos = text.get_rect(centerx = T[7], centery = T[8])
    screen.blit(text, textpos)
    return screen

def NF1(a1, a, A):
    goal = 10
    if a1 == 0:
        global b, notthird, n1
        notthird, b, a, m, extra, n1 = True, 0, 'Start', 0, "", 0
        A = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        Ptsview(b,extra,a,notthird,goal,A)
    if a != 0:
        a1 = a1 + 1
        a = random.randint(0, 9 - a1)
        a = A[a]
        A.remove(a)                 #Error 003: a is not suscriptable (fixed dev_3.0)
        a = int(a)
        b = int(b)
        if a > 5 and a < 8:
            b = b * (a - 4)
        elif a == 8:
            b = b ** 2
        elif a == 0:
            a1 = 0
            extra = "Game Over"
        else:
            b = b + a
        b = str(b)
        if a > 0 and a < 6:
            extra = '+'
            a = a 
        elif a > 5 and a < 8:
            extra = 'x'
            a = a - 4
        elif a == 8:
            extra = '^'
            a = 2
        a = str(a)
        if b == '1':
            print ('(' + extra  +' '+ a + ') --> ' + b +' point')
        else:
            print ('(' + extra  +' '+ a + ') --> ' + b +' points')         #Error 001: a gave +1 at beginning (fixed dev_1.3-a)                                            
        a = int(a)
        b = int(b)
        Ptsview(b,extra,a,notthird,goal,A)
    if a1 == 0:
        b2 = str(b)
        if b == 1:
            print ('Game over! You scored 1 point!')                        #Error 002: b = 1 still plural point (fixed dev_2.0)
        elif b == 9:
            print ('Game over! You scored 9 points!')
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
        elif b == 8100:
            print ('Game over! You scored ' + b2 + ' points!')
            print ('Max points! Wow you are lucky!')
        elif b == 10:
            print ('Game over! You scored ' + b2 + ' points!')
            print ('EXACT HIT! Achievements... will be added soon!')
            print ('You are barely allowed to get to the next level!')
            n1 = 1
        elif b > 9:
            print ('Game over! You scored ' + b2 + ' points!')               #Error 000: b was no str (fixed dev_1.0)
            print ('You are allowed to get to the next level!')
            n1 = 1
        elif b == 0:
            print ('Game over! You scored 0 points!')
            print ('This is unlucky, try again.')
        else:
            print ('Game over! You scored ' + b2 + ' points!')
    return n1, a1, a, A

def NF2(n1):
    goal = 1000
    if n1 == 1:
        global q, poss, rest, g, zu, x, a2
        print ("This is the next level, it's a modified version of the very first numers.")
        a2 = 1
        q = 0
        poss = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,7,7,7,7,10,10,10,10,13,13,13,13,16,16,16,16,20,20,20,20,30,30,30,30,60,60,90,90,200,200,400,0]
        rest = [8,8,8,8,8,8,8,8]
        g = 64
        zu = ""
        x = ""
        n1 = 2
    if a2 == 1:
        b = q
        extra = zu
        a = str(x)
        Ptsview(b,extra,a,notthird,goal,A)
        L2 = 0
        s = "s"
        g = g - 1
        dop = random.randint(0,7)
        kop = random.randint(0,rest[dop])                           #Error 005:IndexError: list index out of range (fixed alpha_2.4)
        mop = random.randint(0,g)
        hop = dop
        if kop == 0:
            n1 = 1
        rest[dop-1] = rest[dop-1] - 1
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
    if n1 == 1:
        b = str(b)
        if q == 0:
            print ('Game over! You scored 0 points!')
            print ('This is unlucky, try again.')
        elif q < 999:
            print ('Game over! You scored ' + str(q) + ' points!')
        elif q == 999:
            print ('Game over! You scored 999 points!')
            print ('Close Call II')
            print ('You are barely not allowed to go to the next level')
        elif q == 1000:
            print ('Game over! You scored 1000 points!')
            print ('You are barely allowed to go to the next level!')
            L2 = 1
        elif q > 1000:
            print ('Game over! You scored ' + str(q) + ' points!')
            print ('You are allowed to go to the next level!')
            L2 = 1
    return L2, n1

def NF3(L2):
    goal = 1000000
    if L2 == 1:
        global notthird, count, roun, rest0, rest1, rest2, rest3, PTR, agob, rounb, l, k, rep, a2, total, cal, prei, inx, iny, inz, ina, rinx, riny, rinz, rina, rb, rc, t, bra, brat, bratt, ln, mul, pre, last, nex, div, neg, live, redt, TC, mi, br, BSTv, BST, total
        notthind = False
        print ('This is the planned Numers 2.0')
        print ('Today it should show the great viarity of values u can have. And there will be added even more!')
        count = 0
        roun = 0
        rest0 = [-16384000000000,-128000000000,-128000000000,-128000000000,-960000000,-480000000,-480000000,-480000000,-240000000,-240000000,-240000000,-240000000,-240000000,-120000000,-120000000,-120000000,-120000000,-120000000,-120000000,-120000000,-60000000,-50000000,-50000000,-50000000,-40000000,-40000000,-40000000,-40000000,-40000000,-30000000,-30000000,-30000000,-30000000,-30000000,-30000000,-30000000,-20000000,-20000000,-20000000,-20000000,-20000000,-20000000,-20000000,-20000000,-20000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-1048576,-1024,-1024,-1024,-512,-256,-256,-256,-128,-128,-128,-128,-128,-64,-64,-64,-64,-64,-64,-64,-32,-28,-28,-28,-24,-24,-24,-24,-24,-20,-20,-20,-20,-20,-20,-20,-16,-16,-16,-16,-16,-16,-16,-16,-16,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-8,-7,-7,-7,-6,-6,-6,-6,-6,-5,-5,-5,-5,-5,-5,-5,-4,-4,-4,-4,-4,-4,-4,-4,-4,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,15,15,15,15,15,15,15,15,22,22,22,22,22,22,22,22,29,29,29,29,29,29,29,29,36,36,36,36,36,36,36,36,43,43,43,43,43,43,43,43,50,50,50,50,50,50,50,50,57,57,57,57,57,57,57,57,64,64,64,64,64,64,64,64,128,128,128,128,128,128,128,192,192,192,192,192,192,192,256,256,256,256,256,256,256,320,320,320,320,320,320,320,384,384,384,384,384,384,384,448,448,448,448,448,448,448,512,512,512,512,512,512,512,1000,1000,1000,1000,1000,1000,2000,2000,2000,2000,2000,2000,3000,3000,3000,3000,3000,3000,4000,4000,4000,4000,4000,4000,5000,5000,5000,5000,5000,5000,6000,6000,6000,6000,6000,6000,12000,12000,12000,12000,12000,18000,18000,18000,18000,18000,24000,24000,24000,24000,24000,30000,30000,30000,30000,30000,36000,36000,36000,36000,36000,81000,81000,81000,81000,126000,126000,126000,126000,171000,171000,171000,171000,216000,216000,216000,216000,2000000,2000000,2000000,3000000,3000000,3000000,4000000,4000000,4000000,10000000,10000000,16000000,16000000,64000000,"^-1","x0","x-1","x-2","-3","-2","-1","1","2","3","inx","iny","inz","ina","rb","rc","(i)","t","-4t","-3t","-2t","-1t","0t","1t","2t","3t","4t","l+n","l+n","l+n","lxn","lxn","l^n","l?n","^(-1)","^(-1)","^(-1)","x(-1)","x(-1)","x(-1)","x0","^0","/0","l"]
        rest1 = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
        rest2 = [64,64,64,64,64,64,64,64]
        rest3, PTR, agob, rounb, l, k, rep, a2, total, L2, cal, prei, inx, rinx, riny, rinz, rina, iny, inz, ina, rb, rc, bra, bratt, t, brat, ln, mul, pre, last, nex = 512, [], 0, [], 64, 8, 1, 1, 0, 2, 0, "", 0, 0, 0, 0, 0, 0, 0, 0, False, False, False, False, 0, 0, 0, "", "", 0, ""
        div, neg, live, redt, TC, mi, br, BSTv, BST = False, False, 0, False, [0,0,0,0,0,0,0,0,0,0,0], 1, 0, [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0] # for negative at ^-1
        a = nex
        b = total
        extra = pre
        Ptsview(b,extra,a,notthird,goal,A)
    if a2 == 1:
        notthird = False
        if nex == "":
            nex = 0
        if redt == True:
            if t == 0:
                L2 = 1
            else:
                t = t - 1
        s = "s"
        if rinx != 0:
            rinx = rinx - 1
            if rinx == 0:
                nex = inx
                pre = prx
        if riny != 0:
            riny = riny - 1
            if riny == 0:
                nex = iny
                pre = pry
        if rinz != 0:
            rinz = rinz - 1
            if rinz == 0:
                nex = inz
                pre = prz
        if rina != 0:
            rina = rina - 1
            if rina == 0:
                nex = ina
                pre = pra
        rest3 = rest3 - 1
        aop = random.randint(1,k) # for you got an 1,2...
        bop = random.randint(1,k) # for you gon an A1,A2...
        cop = random.randint(0,rest3) # for (+ sth)
        fop = (aop-1) * 8 + bop
        eop = random.randint(0,rest1[fop-1]) # for validation 1
        if eop == 0:
            if live == 1 and aop != 0:
                print ("You lost a life")
                live = 0
            elif live == 0 and aop != 0:
                pre = ""
                if t < 1:
                    L2 = 1
                if t > 0:
                    a2 = 1
                    redt = True
        gop = random.randint(0,rest2[aop-1]) # for validation 2
        if aop == 0:
            if live == 1:
                live = 0
                print ("You lost a life")
            else:
                pre = ""
                if t < 1:
                    L2 = 1
                if t > 0:
                    a2 = 1
                    redt = True
        rest2[aop-1] = rest2[aop-1] - 1
        rest1[fop-1] = rest1[fop-1] - 1
        val = rest0[cop]
        rest0.remove(rest0[cop])
        print ("You got " + str(aop))
        let = ["A","B","C","D","E","F","G","H"]
        lap = let[aop-1]
        print ("You got " + str(lap) + str(bop))
        rounb.append(val)
        agob = agob + 1
        if inx != last and iny != last and inz != last and ina != last:
            if inx > 0:
                rinx = last
            if iny > 0:
                riny = last
            if inz > 0:
                rinz = last
            if ina > 0:
                rina = last
        if val == "^-1":
            BSTv[br] = 3
            boo = -1
            if br > 0:
                for boost in range(0,br):
                    if BSTv[boost] == 2:
                        boo = boo * BST[boost]
                    if BSTv[boost] == 1:
                        boo = boo + BST[boost]
            BST[br] = boo
            br = br + 1
            print(boo)
        elif val == "x0":
            BSTv[br] = 2
            boo = 0
            if br > 0:
                for boost in range(0,br):
                    if BSTv[boost] == 3:
                        boo = boo ^ BST[boost]
                    if BSTv[boost] == 2:
                        boo = boo * BST[boost]
                    if BSTv[boost] == 1:
                        boo = boo + BST[boost]
            BST[br] = boo
            br = br + 1
            print(boo)
        elif val == "x-1":
            BSTv[br] = 2
            boo = -1
            if br > 0:
                for boost in range(0,br):
                    if BSTv[boost] == 3:
                        boo = boo ^ BST[boost]
                    if BSTv[boost] == 2:
                        boo = boo * BST[boost]
                    if BSTv[boost] == 1:
                        boo = boo + BST[boost]
            BST[br] = boo
            br = br + 1
            print(boo)
        elif val == "x-2":
            BSTv[br] = 2
            boo = -2
            if br > 0:
                for boost in range(0,br):
                    if BSTv[boost] == 3:
                        boo = boo ^ BST[boost]
                    if BSTv[boost] == 2:
                        boo = boo * BST[boost]
                    if BSTv[boost] == 1:
                        boo = boo + BST[boost]
            BST[br] = boo
            br = br + 1
            print(boo)
        elif val == "-3":
            BSTv[br] = 1
            boo = -3
            if br > 0:
                for boost in range(0,br):
                    if BSTv[boost] == 3:
                        boo = boo ^ BST[boost]
                    if BSTv[boost] == 2:
                        boo = boo * BST[boost]
                    if BSTv[boost] == 1:
                        boo = boo + BST[boost]
            BST[br] = boo
            br = br + 1
            print(boo)
        elif val == "-2":
            BSTv[br] = 1
            boo = -2
            if br > 0:
                for boost in range(0,br):
                    if BSTv[boost] == 3:
                        boo = boo ^ BST[boost]
                    if BSTv[boost] == 2:
                        boo = boo * BST[boost]
                    if BSTv[boost] == 1:
                        boo = boo + BST[boost]
            BST[br] = boo
            br = br + 1
            print(boo)
        elif val == "-1":
            BSTv[br] = 1
            boo = -1
            if br > 0:
                for boost in range(0,br):
                    if BSTv[boost] == 3:
                        boo = boo ^ BST[boost]
                    if BSTv[boost] == 2:
                        boo = boo * BST[boost]
                    if BSTv[boost] == 1:
                        boo = boo + BST[boost]
            BST[br] = boo
            br = br + 1
            print(boo)
        elif val == "1":
            BSTv[br] = 1
            boo = 1
            if br > 0:
                for boost in range(0,br):
                    if BSTv[boost] == 3:
                        boo = boo ^ BST[boost]
                    if BSTv[boost] == 2:
                        boo = boo * BST[boost]
                    if BSTv[boost] == 1:
                        boo = boo + BST[boost]
            BST[br] = boo
            br = br + 1
            print(boo)
        elif val == "2":
            BSTv[br] = 1
            boo = 2
            if br > 0:
                for boost in range(0,br):
                    if BSTv[boost] == 3:
                        boo = boo ^ BST[boost]
                    if BSTv[boost] == 2:
                        boo = boo * BST[boost]
                    if BSTv[boost] == 1:
                        boo = boo + BST[boost]
            BST[br] = boo
            br = br + 1
            print(boo)
        elif val == "3":
            BSTv[br] = 1
            boo = 3
            if br > 0:
                for boost in range(0,br):
                    if BSTv[boost] == 3:
                        boo = boo ^ BST[boost]
                    if BSTv[boost] == 2:
                        boo = boo * BST[boost]
                    if BSTv[boost] == 1:
                        boo = boo + BST[boost]
            BST[br] = boo
            br = br + 1
            print(boo)
        elif val == "inx":
            inx = last
            prx = pre
            if len(PTR) > 0:
                total = PTR[roun-1]
        elif val == "iny":
            iny = last
            pry = pre
            if len(PTR) > 0:
                total = PTR[roun-1]
        elif val == "inz":
            inz = last
            prz = pre
            if len(PTR) > 0:
                total = PTR[roun-1]
        elif val == "ina":
            ina = last
            pra = pre
            if len(PTR) > 0:
                total = PTR[roun-1]
        elif val == "rb":
            rb = True
            if len(PTR) > 0:
                total = PTR[roun-1]
        elif val == "rc":
            rc = True
            if len(PTR) > 0:
                total = PTR[roun-1]
        elif val == "(i)":
            bra = True
        elif val == "t":
            total = 0
            L2 = 1
        elif val == "-4t":
            t = t - 4
            a = ("You got -4 Turns")
        elif val == "-3t":
            t = t - 3
            a = ("You got -3 Turns")
        elif val == "-2t":
            t = t - 2
            a = ("You got -2 Turns")
        elif val == "-1t":
            t = t - 1
            a = ("You got -1 Turn")
        elif val == "0t":
            t = t + 0
            a = ("You got 0 Turns")
        elif val == "1t":
            t = t + 1
            a = ("You got +1 Turn")
        elif val == "2t":
            t = t + 2
            a = ("You got +2 Turns")
        elif val == "3t":
            t = t + 3
            a = ("You got +3 Turns")
        elif val == "4t":
            t = t + 4
            a = ("You got +4 Turns")
        elif val == "l+n":
            ln = 1
            if len(PTR) > 0:
                total = PTR[roun-1]
        elif val == "lxn":
            ln = 2
            if len(PTR) > 0:
                total = PTR[roun-1]
        elif val == "l^n":
            ln = 3
            if len(PTR) > 0:
                total = PTR[roun-1]
        elif val == "l?n":
            ln = 4
            if len(PTR) > 0:
                total = PTR[roun-1]
        elif val == "^(-1)":
            total = 1/total
            print("Point Switch: 1/points")
        elif val == "x(-1)":
            total = -total
            print("Point Switch: -points")
        elif val == "x0":
            total = 0
        elif val == "^0":
            total = 1
        elif val == "/0":
            print ("(/0) --> Impossible! NO dividing through 0!")
            L2 = 1
        elif val == "l":
            live = 1
            print ("You got a life")
            redt = False
        elif val < -100000000000:
            nex = val/1000000000
            pre = "r"
            if neg == True:
                pre = "r-"
        elif val < -9999999 and val > -100000000000:
            nex = val/10000000
            pre = "/"
            if neg == True:
                pre = "/-"
        elif val < 0 and val > -1048577:
            nex = val
            pre = "-"
            if neg == True:
                pre = "+"
        elif val == 0:
            nex = val
            pre = " "
        elif val > 0 and val < 513:
            nex = val
            pre = "+"
            if neg == True:
                pre = "-"
        elif val > 512 and val < 216001:
            nex = val/1000
            pre = "x"
            if neg == True:
                pre = "x-"
        elif val > 216000:
            nex = val/1000000
            pre = "^"
            if neg == True:
                pre = "^-"
        else:
            L2 = 1
        if rb == True:
            rep = nex * rep
            rb = False
        if rc == True:
            rep = nex * rep
            rc = False
        for why in range (0,rep):
            if nex < -nex:
                nex = -nex
            if neg == True:
                mi = -1
            else:
                mi = 1
            if br > 0:
                for boost in range(0,len(BST)):
                    if BSTv[boost] == 3:
                        nex = nex ** BST[boost]
                    if BSTv[boost] == 2:
                        nex = nex * BST[boost]
                    if BSTv[boost] == 1:
                        nex = nex + BST[boost]
            if ln > 0:
                if ln == 1:
                    nex = nex + last
                if ln == 2:
                    nex = nex * last
                if ln == 3:
                    nex = last ** nex
                if ln == 4:
                    if pre == "+":
                        nex = nex + last
                    if pre == "-":
                        nex = last - nex
                    if pre == "x":
                        nex = last * nex
                    if pre == "/":
                        nex = last / nex
                    if pre == "^":
                        nex = last ** nex
                    if pre == "r":
                        nex = last ** (1/nex)
                ln = 0
            if bra == True:
                if bratt == False:
                    brat, prea = nex, pre
                    pre = ""
                    bratt = True
                    lel = total
                    total = 0
                if brat == 0:
                    bra = False
                    L2 = 1
                brat = brat - 1
                if brat < 1:
                    if prea == "+":
                        total = total + lel
                    if prea == "-":
                        total = lel - total
                    if prea == "*":
                        total = total * lel
                    if prea == "/" and total != 0:
                        total = lel / total
                    if prea == "^":
                        total = lel ** total
                    if prea == "r" and total != 0:
                        total = lel ** (1 / total)
                    bra = False
            if pre == "+":
                total = (total + nex) * mi
            elif pre == "-":
                total = (total - nex) * mi
            elif pre == "x":
                total = (total * nex) * mi
            elif pre == "/":
                if nex == 0:
                    print ("YOU DIVIDED BY 0!")
                    L2 = 1
                total = (total / nex) * mi
            elif pre == "^":
                total = (total ** nex) * mi
            elif pre == "r":
                if total < -total:
                    total = -total
                    bi = True
                else:
                    bi = False
                if nex == 0:
                    print ("YOU ROOTED BY 0!")
                    L2 = 1
                total = (total ** (1/nex)) * mi
                if bi == True:
                    total = -total
            for tr in range (-9,1):
                TC[-tr+1] = TC[-tr]
            TC[0] = total
            if total == 1:
                s = ""
            else:
                s = "s"
            last = nex
            print ("(" + pre + str(nex) + ") --> " + str(total) + mul + " point" + s)
            PTR.append(total)
            roun = roun + 1
            pre1 = pre
        if rep > 1:
            rep = 1
        a, b, extra = nex, total, pre
        Ptsview(b,extra,a,notthird,goal,A)
    if t < 0:
        print (TC[-t])
    return L2
             
def Numers_Forward(a1, n1, L2, a, A):
    if L2 > 0 and total < 1000000:
        L2 = NF3(L2)
    elif n1 > 0 and L2 == 0:
        L2, n1 = NF2(n1)
    elif n1 == 0 and L2 == 0:
        n1, a1, a, A = NF1(a1, a, A)
    return a1, n1, L2, a, A

pygame.init()
screen = pygame.display.set_mode([1280,786]) # half is 393
hintergrund = pygame.Surface(screen.get_size())
screen.fill([0, 0, 0])
go, shad, uds, menu, A = "°", 127, 4, False, []
while go != "y" and go != "n" or menu == True:
    time.sleep(0.02)
    if menu == False and go != "y" and go != "n":
        if "alpha_" in __file__:
            version = __file__.strip('.py')
            totalvs = "Alpha " + version[__file__.index("alpha_")+6] + ""
            semi = version[__file__.index("alpha_")+7 : len(version)]
        for sha in range(0, 9):
            T = [None, 200, "NUMERS", True, 127+sha*16, 127+sha*16, 127+sha*16, hintergrund.get_width() / 2+sha, 100+sha]
            screen = Texts(T)
        pygame.display.set_caption("NUMERS " + totalvs + semi)
        for sha in range(0, 5):
            font = pygame.font.Font(None, 100)
            text = font.render(totalvs, True, (127+sha*32, 127+sha*32, 0))
            font2 = pygame.font.Font(None, 75)
            text2 = font2.render(semi, True, (127+sha*32, 127+sha*32, 0))
            textpos = text.get_rect(centerx=hintergrund.get_width() / 2+sha - text2.get_width()/2, y=256+sha)
            textpos2 = text2.get_rect(x=text.get_width()/2 + hintergrund.get_width()/2 + sha/2 - text2.get_width()/2, bottom=323+sha/2) # shall work for .x.y too
            screen.blit(text, textpos)
            screen.blit(text2, textpos2)
        T = [None, 50, "Press Return to Start!", True, shad, shad, shad, screen.get_width()/2, screen.get_height()/2]
        screen = Texts(T)
        pygame.display.flip()
        go = Return(go)
        if go == "y":
            menu = True
            screen.fill([0, 0, 0])
            go = "°"
            Choice = [255,127,127,127]
            change = False
            down = 0
        shad = shad - uds
        if shad == 3 or shad == 127:
            uds = -uds
    if menu == True:
        if change != True:
            T = [None, 200, "MENU", True, 255, 255, 255, screen.get_width()/2, screen.get_height()/8]
            screen = Texts(T)
            T = [None, 100, "Play*", True, Choice[0], Choice[0], Choice[0], screen.get_width()/2, screen.get_height()/2]
            screen = Texts(T)
            T = [None, 75, "Statistics", True, Choice[1], Choice[1], Choice[1], screen.get_width()/4, screen.get_height()/3*2]
            screen = Texts(T)
            T = [None, 75, "Changelog", True, Choice[3], Choice[3], Choice[3], screen.get_width()/4*3, screen.get_height()/3*2]
            screen = Texts(T)
            T = [None, 75, "Load Save", True, Choice[2], Choice[2], Choice[2], screen.get_width()/2, screen.get_height()/3*2]
            screen = Texts(T)
            T = [None, 50, "*Only mode right now", True, 127, 127, 127, screen.get_width()/2, screen.get_height()/4*3]
            screen = Texts(T)
        go = Return(go)
        if change == True:
            screen, down = Changelog(screen, down)
        if go == "n" or go == "y" and Choice[0] == 255:
            menu = False
        elif go == "y" and Choice[1] == 255:
            print ("not available jet")
        elif go == "y" and Choice[2] == 255:
            print ("not available jet")
        elif go == "y" and Choice[3] == 255:
            change = True
            screen, down = Changelog(screen, down)
        elif go == "up":
            if Choice[3] == 255:
                if down > 0:
                    down = down - 1
            else:
                Choice = [255,127,127,127]
        elif go == "down":
            if Choice[3] == 255:
                down = down + 1
            if Choice[0] == 255:
                Choice = [127,127,255,127]
        elif go == "right":
            if Choice[0] == 255 or Choice[2] == 255:
                Choice = [127,127,127,255]
            elif Choice[1] == 255:
                Choice = [127,127,255,127]
            elif Choice[3] == 255:
                Choice = [127,255,127,127]
        elif go == "left":
            if Choice[0] == 255 or Choice[2] == 255:
                Choice = [127,255,127,127]
            elif Choice[1] == 255:
                Choice = [127,127,127,255]
            elif Choice[3] == 255:
                Choice = [127,127,255,127]
        elif go == "esc":
            if Choice[3] == 255:
                change = False
                screen.fill([0,0,0])
        pygame.display.flip()
        
game = False
if go == "y":
    game = True

total = 0
screen.fill([0, 0, 0])
pygame.display.flip()
tick, tack, teck, tock, tuck, a1, n1, L2, a, nah = 0, 0, 0, 0, 0, 0, 0, 0, 1, 0
while game == True:
    sec, minit, hour, day = "", "", "", ""
    go = Return(go)
    if go == "n":
        game = False
        break
    time.sleep(0.01)                                #Usage for FPS options maybe?
    #PV_ani()
    if tick == 100:
        tick = 0
        tack = tack + 1
        if total < 999999:
            a1, n1, L2, a, A = Numers_Forward(a1, n1, L2, a, A)
        if total >= 1000000:
            screen.fill([0, 0, 0])
            T = [None, 100, "Points: " + str(total), True, 255, 255, 255, hintergrund.get_width()/2, hintergrund.get_height()/2]
            screen = Texts(T)
            pygame.display.flip()
    if tack == 60:
        teck = teck + 1
        tack = 0
    if tack > 0:
        sec = " " + str(tack) + "s"
    if teck == 60:
        tock = tock + 1
        teck = 0
    if teck > 0:
        minit = " " + str(teck) + "m"
    if tock == 24:
        tuck = tuck + 1
        tock = 0
    if tock > 0:
        hour = " " + str(tock) + "h"
    if tuck > 0:
        day = " " + str(tuck) + "d"
    pygame.display.set_caption("NUMERS " + totalvs + semi + day + hour + minit + sec + " " + str(tick*10) + "ms")
    tick = tick + 1 # normaly 1

pygame.quit()
