import random, time, pygame, sys, datetime
from rend import *


def NF1(a1, a, go, nixt):
    global extra, goal, ten
    goal = 10
    if a1 == 0:
        global b, notthird, n1, A
        notthird, b, a, m, extra, n1 = True, 0, 'Start', 0, "", 0
        A = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        Aview = ["Game Over", "+1", "+2", "+3", "+4", "+5", "x2", "x3", "^2"]
        a1 = 9
    if a != 0:
        if go == "y":
            nixt = b
            a1 = a1 - 1
            a = random.randint(0, a1)
            a = A[a]
            A.remove(a)  # Error 003: a is not suscriptable (fixed dev_3.0)
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
            b2 = b
            if b == '1':
                print('(' + extra + ' ' + a + ') --> ' + b + ' point')
            else:
                print(
                    '(' + extra + ' ' + a + ') --> ' + b + ' points')  # Error 001: a gave +1 at beginning (fixed dev_1.3-a)
            a = int(a)
            b = int(b)
    if a1 == 0:
        if b == 1:
            print('Game over! You scored 1 point!')  # Error 002: b = 1 still plural point (fixed dev_2.0)
        elif b == 9:
            print('Game over! You scored 9 points!')
            print('Close Call! -be 1 point short')
            print('You are barely not allowed to get to the next level')
        elif b == 42:
            print('Game over! You scored 42 points!')
            print('How do you win?')
            print('42!')
            print('Eh, I lost with 42...')
            print('But 42 is always the answer.')
            print('Sure?')
            print('42!')
            print('Bye.')
            print('Bye.')
        elif b == 69:
            print('Heh... :) Noice')
        elif b == 8100:
            print('Game over! You scored ' + b2 + ' points!')
            print('Max points! Wow you are lucky!')
            n1 = 1
        elif b == 10:
            print('Game over! You scored ' + b2 + ' points!')
            print('EXACT HIT! Achievements... will be added soon!')
            print('You are barely allowed to get to the next level!')
            n1 = 1
        elif b > 9:
            print('Game over! You scored ' + b2 + ' points!')  # Error 000: b was no str (fixed dev_1.0)
            print('You are allowed to get to the next level!')
            n1 = 1
        elif b == 0:
            print('Game over! You scored 0 points!')
            print('This is unlucky, try again.')
        else:
            print('Game over! You scored ' + b2 + ' points!')
        ten = -1
    return n1, a1, a, b, nixt, goal

