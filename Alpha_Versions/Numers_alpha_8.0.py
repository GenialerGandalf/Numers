# -*- coding: iso-8859-2 -*-

import random, time, pygame, sys, datetime, tkinter  # eclipse for launch without download, or hello world
from Changelog import Changelog
from Texts import Texts

from rend import *
from achieve import *
from save import *

#moved NF1,NF2,NF3 to their respective files
from Level1 import NF1
from Level2 import NF2
from Level3 import NF3

def Numers_Forward(a1, n1, L2, a, go, noxt, naxt, nixt, q, total, b, Ach):
    pre, zu, nex, x, poss, rest, rest1, rest2, rest0, goal = "", "", "", "", 0, 0, 0, 0, 0, 10
    if L2 > 0:
        n1, L2, naxt, total, goal, pre, nex, rest1, rest2, rest0, Ach = NF3(L2, go, naxt, Ach, total)
    elif n1 > 0 and L2 == 0:
        L2, n1, noxt, q, goal, zu, x, poss, rest, Ach = NF2(n1, L2, go, noxt, Ach)
    elif n1 == 0 and L2 == 0:
        n1, a1, a, b, nixt, goal, Ach = NF1(a1, a, go, nixt, Ach)
    return a1, n1, L2, a, go, b, noxt, naxt, nixt, q, total, goal, pre, zu, nex, x, poss, rest, rest1, rest2, rest0, Ach

pygame.init()
root = tkinter.Tk()
root.withdraw()
x1, y1 = root.winfo_screenwidth(), root.winfo_screenheight()
x2 = x1/1280
y2 = y1/786
if x2 > y2:
    x2 = y2
screen = pygame.display.set_mode([x1, y1])  # half is 393
screen.fill([0, 0, 0])
go, shad, uds, menu, game, A, save, achi, game1 = "°", 127, 8, False, False, [], False, False, False
q, b, notthird, goal, x, zu, nex = 0, 0, True, 10, 0, 0, ""
stoppy, ten = False, -1
Ach = []
Choice2 = [255, 127, 127, 127, 127, 127, 127, 127]
total, extra, pre, zu, poss, rest, rest1, rest2, rest0, c = 0, "", "", "", 0, 0, 0, 0, 0, 0
screen.fill([0, 0, 0])
pygame.display.flip()
tick, tack, teck, tock, tuck, a1, n1, L2, a, nah, hs, qhs, bhs, games, go1, nixt, noxt, naxt = 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, False, 0, 0, 0
while go != "n":
    if go != "y" and go != "n" and game == False or menu == True:
        if menu == False and go != "y" and go != "n":
            if "alpha_" in __file__:
                version = __file__.strip('.py')
                totalvs = "Alpha " + version[__file__.index("alpha_") + 6]
                semi = version[__file__.index("alpha_") + 7: len(version)]
                tog = totalvs + semi
                vers = version[__file__.index("alpha_") + 6] + version[__file__.index("alpha_") + 8]
            for sha in range(0, 9):
                T = [None, int(200*x2), "NUMERS", True, 127 + sha * 16, 127 + sha * 16, 127 + sha * 16,
                     screen.get_width() / 2 + sha, 100 + sha,screen,x2]
                screen = Texts(T,screen,x2)
            pygame.display.set_caption("NUMERS " + totalvs + semi)
            for sha in range(0, 5):
                font = pygame.font.Font(None, int(100*x2))
                text = font.render(totalvs, True, (127 + sha * 32, 127 + sha * 32, 0))
                font2 = pygame.font.Font(None, int(75*x2))
                text2 = font2.render(semi, True, (127 + sha * 32, 127 + sha * 32, 0))
                textpos = text.get_rect(centerx=screen.get_width() / 2 + int(sha*x2) - text2.get_width() / 2, y=int(256*x2) + int(sha*x2))
                textpos2 = text2.get_rect(
                    x=text.get_width() / 2 + screen.get_width() / 2 + sha / 2 - text2.get_width() / 2,
                    bottom=int(323*x2) + sha / 2)  # shall work for .x.y too
                screen.blit(text, textpos)
                screen.blit(text2, textpos2)
            T = [None, 50*x2, "Press Return to Start!", True, shad, shad, shad, screen.get_width() / 2,
                 screen.get_height() / 2]
            screen = Texts(T,screen,x2)
            go = Return(go)
            if go == "y":
                menu = True
                screen.fill([0, 0, 0])
                go = "°"
                Choice = [255, 127, 127, 127, 127]
                change = False
                down = 0
            shad = shad - uds
            if shad == 7 or shad == 127:
                uds = -uds
            time.sleep(0.04)
        if menu == True and game1 == False:
            screen.fill([0, 0, 0])
            if change != True and achi != True and save != True:
                T = [None, 200*x2, "MENU", True, 255, 255, 255, screen.get_width() / 2, screen.get_height() / 8]
                screen = Texts(T,screen,x2)
                T = [None, 100*x2, "Play", True, Choice[0], Choice[0], Choice[0], screen.get_width() / 2,
                     screen.get_height() / 8 * 3]
                screen = Texts(T,screen,x2)
                T = [None, 75*x2, "Statistics*", True, Choice[1], Choice[1], Choice[1], screen.get_width() / 4,
                     screen.get_height() / 8 * 4]
                screen = Texts(T,screen,x2)
                T = [None, 75*x2, "Changelog", True, Choice[3], Choice[3], Choice[3], screen.get_width() / 4 * 3,
                     screen.get_height() / 8 * 4]
                screen = Texts(T,screen,x2)
                T = [None, 75*x2, "Savestates", True, Choice[2], Choice[2], Choice[2], screen.get_width() / 2,
                     screen.get_height() / 8 * 4]
                screen = Texts(T,screen,x2)
                T = [None, 50*x2, "*Not available right now", True, 127, 127, 127, screen.get_width() / 2,
                     screen.get_height() / 4 * 3.5]
                screen = Texts(T,screen,x2)
                T = [None, 75*x2, "Achievements", True, Choice[4], Choice[4], Choice[4], screen.get_width() / 2,
                     screen.get_height() / 8 * 5]
                screen = Texts(T,screen,x2)
            go = Return(go)
            if change == True:
                screen, down = Changelog(screen, down, x2)
            if save == True:
                save, games, bhs, qhs, hs, Ach = Savestates(screen, go, tog, games, save, qhs, bhs, hs, Ach, x2, version, vers)
            elif achi == True:
                screen, achi, go = Achieves(Ach, screen, x2, achi)
            elif go == "y" and Choice[0] == 255:
                game1 = True
            elif go == "y" and Choice[1] == 255:
                print("not available yet")
            elif go == "y" and Choice[2] == 255:
                go = ""
                save, games, bhs, qhs, hs, Ach = Savestates(screen, go, tog, games, save, qhs, bhs, hs, Ach, x2, version, vers)
                save = True
            elif go == "y" and Choice[3] == 255:
                change = True
                screen, down = Changelog(screen, down, x2)
            elif go == "y" and Choice[4] == 255:
                achi = True
                screen, achi, go = Achieves(Ach, screen, x2, achi)
            elif go == "up":
                if Choice[3] == 255 and change == True:
                    if down > 0:
                        down = down - 1
                elif Choice[4] == 255:
                    Choice = [127, 127, 255, 127, 127]
                else:
                    Choice = [255, 127, 127, 127, 127]
            elif go == "down":
                if Choice[3] == 255:
                    if change == True:
                        down = down + 1
                if Choice[0] == 255:
                    Choice = [127, 127, 255, 127, 127]
                elif Choice[0] != 255 and change != True:
                    Choice = [127, 127, 127, 127, 255]
            elif go == "right":
                if change != True:
                    if Choice[0] == 255 or Choice[2] == 255 or Choice[4] == 255:
                        Choice = [127, 127, 127, 255, 127]
                    elif Choice[1] == 255:
                        Choice = [127, 127, 255, 127, 127]
                    elif Choice[3] == 255:
                        Choice = [127, 255, 127, 127, 127]
            elif go == "left":
                if change != True:
                    if Choice[0] == 255 or Choice[2] == 255 or Choice[4] == 255:
                        Choice = [127, 255, 127, 127, 127]
                    elif Choice[1] == 255:
                        Choice = [127, 127, 127, 255, 127]
                    elif Choice[3] == 255:
                        Choice = [127, 127, 255, 127, 127]
            elif go == "esc":
                if save == True:
                    save = False
                if achi == True:
                    achi = False
                if change == True:
                    change = False
                elif change == False:
                    menu = False
                screen.fill([0, 0, 0])
    if game1 == True:
        if menu == True:
            screen.fill([0, 0, 0])
            if change != True and achi != True and save != True:
                T = [None, 150*x2, "Select Story", True, 255, 127, 0, screen.get_width() / 2, screen.get_height() / 8]
                screen = Texts(T,screen,x2)
                T = [None, 50*x2, "Numers Nothing", True, Choice2[0], Choice2[0]/2, Choice2[0], screen.get_width() / 2,
                     screen.get_height() / 16 * 5]
                screen = Texts(T,screen,x2)
                T = [None, 50*x2, "Numers Forward", True, Choice2[1], Choice2[1]/2, Choice2[1], screen.get_width() / 2,
                     screen.get_height() / 16 * 6]
                screen = Texts(T,screen,x2)
                T = [None, 50*x2, "Numers Enemies", True, Choice2[2], Choice2[2]/2, Choice2[2], screen.get_width() / 2,
                     screen.get_height() / 16 * 7]
                screen = Texts(T,screen,x2)
                T = [None, 50*x2, "Numers Dungeons", True, Choice2[3], Choice2[3]/2, Choice2[3], screen.get_width() / 2,
                     screen.get_height() / 16 * 8]
                screen = Texts(T,screen,x2)
                T = [None, 50*x2, "Numers Civilisation", True, Choice2[4], Choice2[4]/2, Choice2[4], screen.get_width() / 2,
                     screen.get_height() / 16 * 9]
                screen = Texts(T,screen,x2)
                T = [None, 50*x2, "Numers Beginnings", True, Choice2[5], Choice2[5]/2, Choice2[5], screen.get_width() / 2,
                     screen.get_height() / 16 * 10]
                screen = Texts(T,screen,x2)
                T = [None, 50*x2, "Numers Adventures", True, Choice2[6], Choice2[6]/2, Choice2[6], screen.get_width() / 2,
                     screen.get_height() / 16 * 11]
                screen = Texts(T,screen,x2)
                T = [None, 50*x2, "Numers Spaceworld", True, Choice2[7], Choice2[7]/2, Choice2[7], screen.get_width() / 2,
                     screen.get_height() / 16 * 12]
                screen = Texts(T,screen,x2)
            go = Return(go)
            if change == True:
                screen, down = Changelog(screen, down, x2)
            if save == True:
                save, games, bhs, qhs, hs, Ach = Savestates(screen, go, tog, games, save, qhs, bhs, hs, Ach)
            elif achi == True:
                screen, achi, go = Achieves(Ach, screen, x2, achi)
            elif go == "y" and Choice2[1] == 255:
                menu = False
                game = True
            elif go == "y" and Choice2[0] == 255:
                print("not available yet")
            elif go == "y" and Choice[2] == 255:
                go = ""
                save, games, bhs, qhs, hs, Ach = Savestates(screen, go, tog, games, save, qhs, bhs, hs, Ach)
                save = True
            elif go == "y" and Choice[3] == 255:
                change = True
                screen, down = Changelog(screen, down, x2)
            elif go == "y" and Choice[4] == 255:
                achi = True
                screen, achi, go = Achieves(Ach, screen, x2, achi)
            elif go == "up":
                if Choice2[1] == 255:
                    Choice2 = [255, 127, 127, 127, 127, 127, 127, 127]
                elif Choice2[2] == 255:
                    Choice2 = [127, 255, 127, 127, 127, 127, 127, 127]
                elif Choice2[3] == 255:
                    Choice2 = [127, 127, 255, 127, 127, 127, 127, 127]
                elif Choice2[4] == 255:
                    Choice2 = [127, 127, 127, 255, 127, 127, 127, 127]
                elif Choice2[5] == 255:
                    Choice2 = [127, 127, 127, 127, 255, 127, 127, 127]
                elif Choice2[6] == 255:
                    Choice2 = [127, 127, 127, 127, 127, 255, 127, 127]
                elif Choice2[7] == 255:
                    Choice2 = [127, 127, 127, 127, 127, 127, 255, 127]
            elif go == "down":
                if Choice2[0] == 255:
                    Choice2 = [127, 255, 127, 127, 127, 127, 127, 127]
                elif Choice2[1] == 255:
                    Choice2 = [127, 127, 255, 127, 127, 127, 127, 127]
                elif Choice2[2] == 255:
                    Choice2 = [127, 127, 127, 255, 127, 127, 127, 127]
                elif Choice2[3] == 255:
                    Choice2 = [127, 127, 127, 127, 255, 127, 127, 127]
                elif Choice2[4] == 255:
                    Choice2 = [127, 127, 127, 127, 127, 255, 127, 127]
                elif Choice2[5] == 255:
                    Choice2 = [127, 127, 127, 127, 127, 127, 255, 127]
                elif Choice2[6] == 255:
                    Choice2 = [127, 127, 127, 127, 127, 127, 127, 255]
            elif go == "esc":
                if game1 == True:
                    game1 = False
                screen.fill([0, 0, 0])
    if game == True:
        menu = False
        sec, minit, hour, day = "", "", "", ""
        go = Return(go)
        if go == "y":
            go1 = True
        if L2 == -1 and go == "y":
            game = False
            go == "°"
            menu = True
            total = 0
            screen.fill([0, 0, 0])
            a1, n1, L2, a, nah = 0, 0, 0, 1, 0
            games = games + 1
        if go == "n":
            game = False
            break
        if go == "esc" or L2 == -1 and n1 == -1:
            game = False
            menu = True
        c, stoppy, ten = PV_ani(b, extra, notthird, goal, A, tick, nixt, stoppy, a, ten, screen, noxt, naxt, q, total, pre, zu, x, nex, poss, rest, rest1, rest2, rest0, x2)
        if tick == 100:
            if go1 == True:
                go = "y"
                go1 = False
                stoppy = False
            tick = 0
            tack = tack + 1
            a1, n1, L2, a, go, b, noxt, naxt, nixt, q, total, goal, pre, zu, nex, x, poss, rest, rest1, rest2, rest0, Ach = Numers_Forward(a1, n1, L2, a, go, noxt, naxt, nixt, q, total, b, Ach)
            if naxt >= 1000000 and L2 == -2:
                screen.fill([0, 0, 0])
                goal = 0
                T = [None, 100, "Points: " + str(total), True, 255, 255, 255, screen.get_width() / 2,
                     screen.get_height() / 2]
                screen = Texts(T,screen,x2)
                if total > hs:
                    hs = total
                if b > bhs:
                    bhs = b
                if q > qhs:
                    qhs = q
                L2 = -1
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
        pygame.display.set_caption("NUMERS " + totalvs + semi + day + hour + minit + sec + " " + str(tick * 10) + "ms")
        tick = tick + 4  # normaly 4
        time.sleep(0.04)
    pygame.display.flip()
pygame.quit()
