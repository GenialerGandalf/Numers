import random, time, pygame, sys, datetime
from rend import *


def NF2(n1, L2, go):
    global goal, noxt
    goal = 1000
    global q, poss, rest, g, zu, x, a2, extra, p, b
    if n1 == 3 and go == "y":
        if q == 0:
            print('Game over! You scored 0 points!')
            print('This is unlucky, try again.')
        elif q < 999:
            print('Game over! You scored ' + str(q) + ' points!')
        elif q == 999:
            print('Game over! You scored 999 points!')
            print('Close Call II')
            print('You are barely not allowed to go to the next level')
        elif q == 1000:
            print('Game over! You scored 1000 points!')
            print('You are barely allowed to go to the next level!')
            L2 = 1
        elif q > 1000:
            print('Game over! You scored ' + str(q) + ' points!')
            print('You are allowed to go to the next level!')
            L2 = 1
        a2 = 0
        n1 = 4
    if n1 == 1 and L2 == 0:
        print("This is the next level, it's a modified version of the very first numers.")
        a2 = 1
        q = 0
        poss = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 7, 7, 7,
                7, 10, 10, 10, 10, 13, 13, 13, 13, 16, 16, 16, 16, 20, 20, 20, 20, 30, 30, 30, 30, 60, 60, 90, 90, 200,
                200, 400, 0]
        rest = [8, 8, 8, 8, 8, 8, 8, 8]
        g = 64
        noxt = 0
        zu = ""
        x = ""
        n1 = 2
    if n1 == 4:
        n1 = 1
    if a2 == 1:
        if go == "y":
            noxt = q
            extra = zu
            a = str(x)
            L2 = 0
            s = "s"
            g = g - 1
            dop = random.randint(0, 7)
            kop = random.randint(0, rest[dop])  # Error 005:IndexError: list index out of range (fixed alpha_2.4)
            mop = random.randint(0, g)
            if kop == 0:
                n1 = 3
                zu = "Game Over"
            else:
                hop = dop
                rest[dop - 1] = rest[dop - 1] - 1
                nop = poss[mop]
                poss.remove(poss[mop])  # Error 004:remove(x) not working (fixed alpha_1.4)
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
                print("You got a " + str(hop))
                print("(" + zu + " " + str(x) + ") --> " + str(q) + " point" + s)
        else:
            L2 = 0
    return L2, n1
