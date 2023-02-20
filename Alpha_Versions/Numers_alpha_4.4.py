# -*- coding: iso-8859-2 -*-

import random, time, pygame, sys #eclipse for launch without download, or hello world 

def Return(go):
    go = "°"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = "n"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                go = 'y'
    
    return go

def Calcul1000(cent):
    cal = cent
    ten = 0
    mil = 0
    deci = 0
    centi = 0
    while cent > 10 or cent < -10:
        while cent >= 1000 or cent <= -1000:
            cent = cent / 1000
            mil = mil + 1
        if cent > 10 or cent < -10:
            cent = cent / 10
            ten = ten + 1
    while mil >= 10:
        deci = deci + 1
        mil = mil - 10
    while deci >= 10:
        centi = centi + 1
        deci = deci - 10
    MIL = ["","M","B","T","Q","q","S","s","O","N"]
    DECI = ["","De","Vi","Tr","Qu","qu","Se","se","Ok","No"]
    CENTI = ["","Cen","Duc","Tre","Qua","Qui","Ses","Sep","Oct","Non","",""]
    kar = MIL[mil] + DECI[deci] + CENTI[centi]
    mil = mil + deci*10 + centi*100
    return kar, ten, mil, cent

def Ptsview(b,extra,a,notthird,goal):
    cent = int(b)
    kar, ten, mil, cent = Calcul1000(cent)
    rz = 255
    wz = 0
    mn1 = 1
    p0 = 140
    screen.fill([0, 0, 0])
    if cent + cent < cent:
        rz = 0
        wz = 255
        p0 = 1140
        mn1 = -1
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
    pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode([1280,786]) # half is 393
hintergrund = pygame.Surface(screen.get_size())
hintergrund.fill([0, 0, 0])
if "alpha_" in __file__:
    version = __file__.strip('.py')
    totalvs = "Alpha " + version[__file__.index("alpha_")+6] + ""
    semi = version[__file__.index("alpha_")+7 : len(version)]
for sha in range(0, 9):
    font = pygame.font.Font(None, 200)
    text = font.render("NUMERS", True, (127+sha*16, 127+sha*16, 127+sha*16))
    textpos = text.get_rect(centerx=hintergrund.get_width() / 2+sha, y=100+sha)
    hintergrund.blit(text, textpos)
for sha in range(0, 5):
    font = pygame.font.Font(None, 100)
    text = font.render(totalvs, True, (127+sha*32, 127+sha*32, 0))                  #the .x shall be smaller
    font2 = pygame.font.Font(None, 75)
    text2 = font2.render(semi, True, (127+sha*32, 127+sha*32, 0))
    textpos = text.get_rect(centerx=hintergrund.get_width() / 2+sha - text2.get_width()/2, y=256+sha)
    textpos2 = text2.get_rect(x=text.get_width()/2 + hintergrund.get_width()/2 + sha/2 - text2.get_width()/2, bottom=323+sha/2) # shall work for .x.y too 
    hintergrund.blit(text, textpos)
    hintergrund.blit(text2, textpos2)

screen.blit(hintergrund, (0, 0))
pygame.display.flip()

screen.fill([0, 0, 0])
pygame.display.flip()

def NF1(a1, a):
    goal = 10
    if a1 == 0:
        global A, b, notthird, n1
        notthird = True
        b = 0
        a = 'Start'
        m = 0
        extra = ''
        Ptsview(b,extra,a,notthird,goal)
        n1 = 0
        A = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    if a != 0:
        a1 = a1 + 1
        a = random.randint(0, 9 - a1)
        a = A[a]
        A.remove(a)                        #Error 003: a is not suscriptable (fixed dev_3.0)
        b = int(b)
        if a > 4 and a < 7:
            b = b * (a - 3)
        elif a == 7:
            b = b ** 2
        elif a == 8:
            b = b + 5
        elif a == 0:
            print ('not more then 1')
            a1 = 0
            extra = "Game Over"
        else:
            b = b + a
        b = str(b)
        if a > 0 and a < 5:
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
        Ptsview(b,extra,a,notthird,goal)
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
        elif b == 3600:
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
    return n1, a1, a

#mdmopqviqeviwevoivmowrmvimeiwvmopwmvion owensoindyciownaeocniwencvoiwecno

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
        Ptsview(b,extra,a,notthird,goal)
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

#fojnweofnewiowebfweofbwufwrbfonweifeirvberubferbvoburebvoeruvbues

def NF3(L2):
    goal = 1000000
    if L2 == 1:
        global notthird, count, roun, All, rest1, rest2, rest3, PTR, agob, rounb, l, k, rep, a2, total, cal, prei, inx, iny, inz, ina, rinx, riny, rinz, rina, rb, rc, t, bra, brat, bratt, ln, mul, pre, last, nex, div, neg, live, redt, TC, mi, br, BSTv, BST, total
        notthind = False
        print ('This is the planned Numers 2.0')
        print ('Today it should show the great viarity of values u can have. And there will be added even more!')
        count = 0
        roun = 0
        All = [-16384000000000,-128000000000,-128000000000,-128000000000,-960000000,-480000000,-480000000,-480000000,-240000000,-240000000,-240000000,-240000000,-240000000,-120000000,-120000000,-120000000,-120000000,-120000000,-120000000,-120000000,-60000000,-50000000,-50000000,-50000000,-40000000,-40000000,-40000000,-40000000,-40000000,-30000000,-30000000,-30000000,-30000000,-30000000,-30000000,-30000000,-20000000,-20000000,-20000000,-20000000,-20000000,-20000000,-20000000,-20000000,-20000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-1048576,-1024,-1024,-1024,-512,-256,-256,-256,-128,-128,-128,-128,-128,-64,-64,-64,-64,-64,-64,-64,-32,-28,-28,-28,-24,-24,-24,-24,-24,-20,-20,-20,-20,-20,-20,-20,-16,-16,-16,-16,-16,-16,-16,-16,-16,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-8,-7,-7,-7,-6,-6,-6,-6,-6,-5,-5,-5,-5,-5,-5,-5,-4,-4,-4,-4,-4,-4,-4,-4,-4,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,15,15,15,15,15,15,15,15,22,22,22,22,22,22,22,22,29,29,29,29,29,29,29,29,36,36,36,36,36,36,36,36,43,43,43,43,43,43,43,43,50,50,50,50,50,50,50,50,57,57,57,57,57,57,57,57,64,64,64,64,64,64,64,64,128,128,128,128,128,128,128,192,192,192,192,192,192,192,256,256,256,256,256,256,256,320,320,320,320,320,320,320,384,384,384,384,384,384,384,448,448,448,448,448,448,448,512,512,512,512,512,512,512,1000,1000,1000,1000,1000,1000,2000,2000,2000,2000,2000,2000,3000,3000,3000,3000,3000,3000,4000,4000,4000,4000,4000,4000,5000,5000,5000,5000,5000,5000,6000,6000,6000,6000,6000,6000,12000,12000,12000,12000,12000,18000,18000,18000,18000,18000,24000,24000,24000,24000,24000,30000,30000,30000,30000,30000,36000,36000,36000,36000,36000,81000,81000,81000,81000,126000,126000,126000,126000,171000,171000,171000,171000,216000,216000,216000,216000,2000000,2000000,2000000,3000000,3000000,3000000,4000000,4000000,4000000,10000000,10000000,16000000,16000000,64000000,"^-1","x0","x-1","x-2","-3","-2","-1","1","2","3","inx","iny","inz","ina","rb","rc","(i)","t","-4t","-3t","-2t","-1t","0t","1t","2t","3t","4t","l+n","l+n","l+n","lxn","lxn","l^n","l?n","^(-1)","^(-1)","^(-1)","x(-1)","x(-1)","x(-1)","x0","^0","/0","l"]
        rest1 = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
        rest2 = [64,64,64,64,64,64,64,64]
        rest3 = 512
        PTR = []
        agob = 0
        rounb = []
        l = 64
        k = 8
        rep = 1
        a2 = 1
        total = 0
        L2 = 2
        cal = 0
        prei = ""
        inx = 0
        rinx = 0
        riny = 0
        rinz = 0
        rina = 0
        iny = 0
        inz = 0
        ina = 0
        rb = False
        rc = False
        bra = False
        bratt = False
        t = 0
        brat = 0
        ln = 0
        mul = ""
        pre = ""
        last = 0
        nex = ""
        div = False # for negative at ^-1
        neg = False # for negative at *-1 etc.
        live = 0
        redt = False
        TC = [0,0,0,0,0,0,0,0,0,0,0]
        mi = 1
        br = 0
        BSTv = [0,0,0,0,0,0,0,0,0,0] 
        BST = [0,0,0,0,0,0,0,0,0,0] # for boost numbers
    if a2 == 1:
        notthird = False
        a = nex
        b = total
        extra = pre
        Ptsview(b,extra,a,notthird,goal)
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
        val = All[cop]
        All.remove(All[cop])
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
            print ("You got -4 Turns")
        elif val == "-3t":
            t = t - 3
            print ("You got -3 Turns")
        elif val == "-2t":
            t = t - 2
            print ("You got -2 Turns")
        elif val == "-1t":
            t = t - 1
            print ("You got -1 Turn")
        elif val == "0t":
            t = t + 0
            print ("You got 0 Turns")
        elif val == "1t":
            t = t + 1
            print ("You got +1 Turn")
        elif val == "2t":
            t = t + 2
            print ("You got +2 Turns")
        elif val == "3t":
            t = t + 3
            print ("You got +3 Turns")
        elif val == "4t":
            t = t + 4
            print ("You got +4 Turns")
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
                    brat = nex
                    prea = pre
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
                    if prea == "/":
                        total = lel / total
                    if prea == "^":
                        total = lel ** total
                    if prea == "r":
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
    if t < 0:
        print (TC[-t])
    return L2
             
def Numers_Forward(a1, n1, L2, a):
    if L2 > 0:
        L2 = NF3(L2)
    elif n1 > 0 and L2 == 0:
        L2, n1 = NF2(n1)
    elif n1 == 0 and L2 == 0:
        n1, a1, a = NF1(a1, a)
    return a1, n1, L2, a
    
go = "°"
shad = 127
uds = 2
while go == "°":
    font = pygame.font.Font(None, 50)
    text = font.render("Press Return to Start!", True, (shad, shad, shad))
    textpos = text.get_rect(centerx=hintergrund.get_width() / 2, y=420)
    hintergrund.blit(text, textpos)
    screen.blit(hintergrund, (0, 0))
    pygame.display.flip()
    time.sleep(0.02)
    go = Return(go)
    shad = shad - uds
    if shad == 1 or shad == 127:
        uds = -uds
game = False
if go == "y":
    game = True

screen.fill([0, 0, 0])
pygame.display.flip()
tick = 0
tack = 0
a1 = 0
n1 = 0
L2 = 0
a = 1
while game == True:
    go = Return(go)
    if go == "n":
        game = False
        break
    time.sleep(0.02)                                                          #Usage for FPS options maybe?
    #PV_ani()
    if tick == 25:
        tick = 0
        tack = tack + 1
        a1, n1, L2, a = Numers_Forward(a1, n1, L2, a)
    tick = tick + 1

pygame.quit()
