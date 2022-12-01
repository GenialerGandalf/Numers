import random, time
a = True
if a == True:
    if a == True:
        if a == True:
            time.sleep(1)
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
            last = 0
            nex = 0
            div = False # for negative at ^-1
            neg = False # for negative at *-1 etc.
            live = 0
            redt = False
            TC = [0,0,0,0,0,0,0,0,0,0,0]
            mi = 1
            br = 0
            BSTv = [0,0,0,0,0,0,0,0,0,0] 
            BST = [0,0,0,0,0,0,0,0,0,0] # for boost numbers 
            while a2 == 1:
                if redt == True:
                    if t == 0:
                        a2 = 0
                        break
                    else:
                        t = t - 1
                L2 = False
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
                            a2 = 0
                            break
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
                            a2 = 0
                            break
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
                    total = PTR[roun-1]
                elif val == "iny":
                    iny = last
                    pry = pre
                    total = PTR[roun-1]
                elif val == "inz":
                    inz = last
                    prz = pre
                    total = PTR[roun-1]
                elif val == "ina":
                    ina = last
                    pra = pre
                    total = PTR[roun-1]
                elif val == "rb":
                    rb = True
                    total = PTR[roun-1]
                elif val == "rc":
                    rc = True
                    total = PTR[roun-1]
                elif val == "(i)":
                    bra = True
                elif val == "t":
                    a2 = 0
                    total = 0
                    break
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
                    total = PTR[roun-1]
                elif val == "lxn":
                    ln = 2
                    total = PTR[roun-1]
                elif val == "l^n":
                    ln = 3
                    total = PTR[roun-1]
                elif val == "l?n":
                    ln = 4
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
                    break
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
                    break
                if rb == True:
                    rep = nex * rep
                    rb = false
                if rc == True:
                    rep = nex * rep
                    rc = false
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
                                nex = nex ^ BST[boost]
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
                            break
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
                            break
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
                            break
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
