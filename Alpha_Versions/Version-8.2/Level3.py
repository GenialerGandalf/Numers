import random, time, pygame, sys, datetime
def NF3(L2, go, naxt, Ach, total):
    global goal
    goal = 1000000
    if L2 == 3:
        if total > 1000000:
            L2 = -2
        else:
            L2 = 1
    elif L2 == 1:
        global notthird, count, roun, rest0, rest1, rest2, rest3, PTR, agob, rounb, l, k, rep, a2, cal, prei, inx, iny, inz, ina, rinx, riny, rinz, rina, rb, rc, t, bra, brat, bratt, ln, mul, pre, last, nex, div, neg, live, redt, TC, mi, br, BSTv, BST
        notthind = False
        print('This is the planned Numers 2.0')
        print('Today it should show the great viarity of values u can have. And there will be added even more!')
        count = 0
        roun = 0
        n1 = 2
        rest0 = [-16384000000000, -128000000000, -128000000000, -128000000000, -960000000, -480000000, -480000000,
                 -480000000, -240000000, -240000000, -240000000, -240000000, -240000000, -120000000, -120000000,
                 -120000000, -120000000, -120000000, -120000000, -120000000, -60000000, -50000000, -50000000, -50000000,
                 -40000000, -40000000, -40000000, -40000000, -40000000, -30000000, -30000000, -30000000, -30000000,
                 -30000000, -30000000, -30000000, -20000000, -20000000, -20000000, -20000000, -20000000, -20000000,
                 -20000000, -20000000, -20000000, -10000000, -10000000, -10000000, -10000000, -10000000, -10000000,
                 -10000000, -10000000, -10000000, -10000000, -10000000, -1048576, -1024, -1024, -1024, -512, -256, -256,
                 -256, -128, -128, -128, -128, -128, -64, -64, -64, -64, -64, -64, -64, -32, -28, -28, -28, -24, -24,
                 -24, -24, -24, -20, -20, -20, -20, -20, -20, -20, -16, -16, -16, -16, -16, -16, -16, -16, -16, -12,
                 -12, -12, -12, -12, -12, -12, -12, -12, -12, -12, -8, -7, -7, -7, -6, -6, -6, -6, -6, -5, -5, -5, -5,
                 -5, -5, -5, -4, -4, -4, -4, -4, -4, -4, -4, -4, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -2, -2, -2,
                 -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4,
                 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7,
                 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 15, 15, 15, 15, 15, 15, 15, 15, 22, 22, 22, 22,
                 22, 22, 22, 22, 29, 29, 29, 29, 29, 29, 29, 29, 36, 36, 36, 36, 36, 36, 36, 36, 43, 43, 43, 43, 43, 43,
                 43, 43, 50, 50, 50, 50, 50, 50, 50, 50, 57, 57, 57, 57, 57, 57, 57, 57, 64, 64, 64, 64, 64, 64, 64, 64,
                 128, 128, 128, 128, 128, 128, 128, 192, 192, 192, 192, 192, 192, 192, 256, 256, 256, 256, 256, 256,
                 256, 320, 320, 320, 320, 320, 320, 320, 384, 384, 384, 384, 384, 384, 384, 448, 448, 448, 448, 448,
                 448, 448, 512, 512, 512, 512, 512, 512, 512, 1000, 1000, 1000, 1000, 1000, 1000, 2000, 2000, 2000,
                 2000, 2000, 2000, 3000, 3000, 3000, 3000, 3000, 3000, 4000, 4000, 4000, 4000, 4000, 4000, 5000, 5000,
                 5000, 5000, 5000, 5000, 6000, 6000, 6000, 6000, 6000, 6000, 12000, 12000, 12000, 12000, 12000, 18000,
                 18000, 18000, 18000, 18000, 24000, 24000, 24000, 24000, 24000, 30000, 30000, 30000, 30000, 30000,
                 36000, 36000, 36000, 36000, 36000, 81000, 81000, 81000, 81000, 126000, 126000, 126000, 126000, 171000,
                 171000, 171000, 171000, 216000, 216000, 216000, 216000, 2000000, 2000000, 2000000, 3000000, 3000000,
                 3000000, 4000000, 4000000, 5000000, 5000000, 6000000, 6000000, 7000000, 8000000, "^-1", "x0", "x-1",
                 "x-2", "-3", "-2", "-1", "1", "2", "3", "inx", "iny", "inz", "ina", "rb", "rc", "(i)", "t", "-4t",
                 "-3t", "-2t", "-1t", "0t", "1t", "2t", "3t", "4t", "l+n", "l+n", "l+n", "lxn", "lxn", "l^n", "l?n",
                 "^(-1)", "^(-1)", "^(-1)", "x(-1)", "x(-1)", "x(-1)", "x0", "^0", "/0", "l"]
        rest1 = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
                 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
        rest2 = [64, 64, 64, 64, 64, 64, 64, 64]
        rest3, PTR, agob, rounb, l, k, rep, a2, total, L2, cal, prei, inx, rinx, riny, rinz, rina, iny, inz, ina, rb, rc, bra, bratt, t, brat, ln, mul, pre, last, nex = 512, [], 0, [], 64, 8, 1, 1, 0, 2, 0, "", 0, 0, 0, 0, 0, 0, 0, 0, False, False, False, False, 0, 0, 0, "", "", 0, ""
        div, neg, live, redt, TC, mi, br, BSTv, BST = False, False, 0, False, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1, 0, [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # for negative at ^-1
        a = nex
        b = total
        extra = pre
        naxt = 0
    if a2 == 1:
        naxt = total
        n1 = 2
        if go == "y":
            notthird = False
            if nex == "":
                nex = 0
            if redt == True:
                if t == 0:
                    L2 = 3
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
            aop = random.randint(1, k)  # for you got an 1,2...
            bop = random.randint(1, k)  # for you gon an A1,A2...
            cop = random.randint(0, rest3)  # for (+ sth)
            fop = (aop - 1) * 8 + bop
            eop = random.randint(0, rest1[fop - 1])  # for validation 1
            if eop == 0:
                if live == 1 and aop != 0:
                    print("You lost a life")
                    live = 0
                elif live == 0 and aop != 0:
                    pre = ""
                    if t < 1:
                        L2 = 3
                    if t > 0:
                        a2 = 1
                        redt = True
            gop = random.randint(0, rest2[aop - 1])  # for validation 2
            if aop == 0:
                if live == 1:
                    live = 0
                    print("You lost a life")
                else:
                    pre = ""
                    if t < 1:
                        L2 = 3
                    if t > 0:
                        a2 = 1
                        redt = True
            rest2[aop - 1] = rest2[aop - 1] - 1
            rest1[fop - 1] = rest1[fop - 1] - 1
            val = rest0[cop]
            rest0.remove(rest0[cop])
            print("You got " + str(aop))
            let = ["A", "B", "C", "D", "E", "F", "G", "H"]
            lap = let[aop - 1]
            print("You got " + str(lap) + str(bop))
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
                    for boost in range(0, br):
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
                    for boost in range(0, br):
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
                    for boost in range(0, br):
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
                    for boost in range(0, br):
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
                    for boost in range(0, br):
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
                    for boost in range(0, br):
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
                    for boost in range(0, br):
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
                    for boost in range(0, br):
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
                    for boost in range(0, br):
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
                    for boost in range(0, br):
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
                    total = PTR[roun - 1]
            elif val == "iny":
                iny = last
                pry = pre
                if len(PTR) > 0:
                    total = PTR[roun - 1]
            elif val == "inz":
                inz = last
                prz = pre
                if len(PTR) > 0:
                    total = PTR[roun - 1]
            elif val == "ina":
                ina = last
                pra = pre
                if len(PTR) > 0:
                    total = PTR[roun - 1]
            elif val == "rb":
                rb = True
                if len(PTR) > 0:
                    total = PTR[roun - 1]
            elif val == "rc":
                rc = True
                if len(PTR) > 0:
                    total = PTR[roun - 1]
            elif val == "(i)":
                bra = True
            elif val == "t":
                total = 0
                L2 = 3
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
                    total = PTR[roun - 1]
            elif val == "lxn":
                ln = 2
                if len(PTR) > 0:
                    total = PTR[roun - 1]
            elif val == "l^n":
                ln = 3
                if len(PTR) > 0:
                    total = PTR[roun - 1]
            elif val == "l?n":
                ln = 4
                if len(PTR) > 0:
                    total = PTR[roun - 1]
            elif val == "^(-1)":
                total = 1 / total
                print("Point Switch: 1/points")
            elif val == "x(-1)":
                total = -total
                print("Point Switch: -points")
            elif val == "x0":
                total = 0
            elif val == "^0":
                total = 1
            elif val == "/0":
                print("(/0) --> Impossible! NO dividing through 0!")
                L2 = 1
            elif val == "l":
                live = 1
                print("You got a life")
                redt = False
            elif val < -100000000000:
                nex = val / 1000000000
                pre = "r"
                if neg == True:
                    pre = "r-"
            elif val < -9999999 and val > -100000000000:
                nex = val / 10000000
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
                nex = val / 1000
                pre = "x"
                if neg == True:
                    pre = "x-"
            elif val > 216000:
                nex = val / 1000000
                pre = "^"
                if neg == True:
                    pre = "^-"
            else:
                L2 = 3
            if rb == True:
                rep = nex * rep
                rb = False
            if rc == True:
                rep = nex * rep
                rc = False
            for why in range(0, int(rep)):
                if nex < -nex:
                    nex = -nex
                if neg == True:
                    mi = -1
                else:
                    mi = 1
                if br > 0:
                    for boost in range(0, len(BST)):
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
                            nex = last ** (1 / nex)
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
                        L2 = 3
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
                        print("YOU DIVIDED BY 0!")
                        L2 = 1
                    else:
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
                        print("YOU ROOTED BY 0!")
                        L2 = 1
                    else:
                        total = (total ** (1 / nex)) * mi
                    if bi == True:
                        total = -total
                for tr in range(-9, 1):
                    TC[-tr + 1] = TC[-tr]
                TC[0] = total
                if total == 1:
                    s = ""
                else:
                    s = "s"
                last = nex
                print("(" + pre + str(nex) + ") --> " + str(total) + mul + " point" + s)
                PTR.append(total)
                roun = roun + 1
                pre1 = pre
            if rep > 1:
                rep = 1
            a, b, extra = nex, total, pre
        else:
            idk = 1
    if t < 0:
        print(TC[-t])
        L2 = -1
        n1 = -1
    return n1, L2, naxt, total, goal, pre, nex, rest1, rest2, rest0, Ach
