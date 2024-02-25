# -*- coding: iso-8859-2 -*-

import random, time, pygame, sys, datetime  # eclipse for launch without download, or hello world
from Changelog import Changelog
from Texts import Texts

from rend import *
from achieve import *

#moved NF1,NF2,NF3 to their respective files
from Level1 import NF1
from Level2 import NF2
from Level3 import NF3

def Numers_Forward(a1, n1, L2, a, go, noxt, naxt, nixt, q, total, b, Ach):
    pre, zu, nex, x, poss, rest, rest1, rest2, rest0, goal = "", "", "", "", 0, 0, 0, 0, 0, 10
    if L2 > 0 and total < 1000000:
        n1, L2, naxt, total, goal, pre, nex, rest1, rest2, rest0, Ach = NF3(L2, go, naxt, Ach)
    elif n1 > 0 and L2 == 0:
        L2, n1, noxt, q, goal, zu, x, poss, rest, Ach = NF2(n1, L2, go, noxt, Ach)
    elif n1 == 0 and L2 == 0:
        n1, a1, a, b, nixt, goal, Ach = NF1(a1, a, go, nixt, Ach)
    return a1, n1, L2, a, go, b, noxt, naxt, nixt, q, total, goal, pre, zu, nex, x, poss, rest, rest1, rest2, rest0, Ach


def Savestates(screen, go, tog, games, save, qhs, bhs, hs, Ach):
    global select, saveprompt, sinput, Save
    if go == "":
        select = 0
        try:
            file = open('save.txt', 'r')
            sinput = file.read()
            file.close()
        except FileNotFoundError as e:
            base = 8  # Amount of parameters in Save prompt
            screen.fill([0, 0, 0])
            T = [None, 75, "Paste your save in the Python Shell", True, 255, 255, 255, screen.get_width() / 2,
                 screen.get_height() / 4]
            screen = Texts(T,screen,x2)
            T = [None, 50, "If you don't have one, just press Enter in the Python Shell", True, 255, 255, 255,
                 screen.get_width() / 2, screen.get_height() / 2]
            screen = Texts(T,screen,x2)
            pygame.display.flip()
            sinput = input(">>> ") + "/"
            file = open('save.txt', 'w')
            file.write(sinput)
            file.close()
        Save = []
        while sinput.find("/") != -1:
            posi = sinput.find("/")
            if posi != 0:
                Save.append(sinput[:posi])
            sinput = sinput[posi + 1:]
        if Save == []:
            Save = [0, 0, 0, 0, 0, 0]
        if len(Save) == 6:
            Save.append(0)
            Save.append(0)
        if len(Save) == 8:
            Save.append(0)
            Save.append(0)
        save = False
        go = ""
        saveprompt = "no"
    current_time = datetime.datetime.now()
    screen.fill([0, 0, 0])
    if go == "right" or select == 1:
        pygame.draw.rect(screen, (0, 0, 255), (screen.get_width() / 2 + 20, 250, 480, 550))
        select = 1
        achiev = 0
        for p in range(0, len(Ach)):
            achiev = achiev + 2**Ach[p]
        slv1 = int(bhs)
        slv2 = int(qhs)
        stime = int(str(current_time)[17:19]) + int(str(current_time)[14:16]) * 60 + int(
            str(current_time)[11:13]) * 3600
        sdate = str(current_time)[0:4] + str(current_time)[5:7] + str(current_time)[8:10]
        saveprompt = sdate + "/" + str(stime) + "/" + str(slv1) + "/" + str(slv2) + "/" + version[
            __file__.index("alpha_") + 6] + version[__file__.index("alpha_") + 8] + "/" + str(games) + "/" + str(
            int(hs)) + "/" + str(achiev) + "/" + "0"
    if go == "left" or select == 2:
        pygame.draw.rect(screen, (0, 0, 255), (140, 250, 480, 550))
        select = 2
    hour = int(Save[1]) / 3600
    rhour = hour - int(hour)
    minu = rhour * 60
    rminu = int(minu)
    sec = minu * 60 - rminu * 60
    rsec = int(sec)
    hour = int(hour)
    if hour < 10:
        hour = "0" + str(hour)
    if rminu < 10:
        rminu = "0" + str(rminu)
    if rsec < 10:
        rsec = "0" + str(rsec)
    Ach2 = bin(int(Save[7]))[2:]
    Ach1 = Ach2.count("1")
    Ach3 = []
    for k in range(0, len(Ach2)+1):
        if Ach2[(len(Ach2)-k):(len(Ach2)-k+1)] == "1":
            Ach3.append(k-1)
    T = [None, 150, "Savestates", True, 255, 255, 255, screen.get_width() / 2, screen.get_height() / 8]
    screen = Texts(T,screen,x2)
    T = [None, 75, "<- Load    or    Save ->", True, 255, 255, 255, screen.get_width() / 2, screen.get_height() / 4]
    screen = Texts(T,screen,x2)
    varl = str(Save[4])
    if varl == "Alpha 5.8":
        varl = "58"
    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() / 2 - 20, 250, 40, 550))
    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() / 2 - 500, 250, 1000, 10))
    T = [None, 25, "Record lv.3: " + str(hs), True, 255, 255, 255, screen.get_width() / 4 * 3 - 50,
         screen.get_height() / 32 * 17]
    screen = Texts(T,screen,x2)
    T = [None, 25, "Record lv.2: " + str(qhs), True, 255, 255, 255, screen.get_width() / 4 * 3 - 50,
         screen.get_height() / 2]
    screen = Texts(T,screen,x2)
    T = [None, 25, "Record lv.1: " + str(bhs), True, 255, 255, 255, screen.get_width() / 4 * 3 - 50,
         screen.get_height() / 32 * 15]
    screen = Texts(T,screen,x2)
    T = [None, 25, "Version: " + tog, True, 255, 255, 255, screen.get_width() / 4 * 3 - 50,
         screen.get_height() / 32 * 14]
    screen = Texts(T,screen,x2)
    T = [None, 25, "Date: " + str(current_time)[0:19], True, 255, 255, 255, screen.get_width() / 4 * 3 - 50,
         screen.get_height() / 32 * 13]
    screen = Texts(T,screen,x2)
    T = [None, 25, "Games won: " + str(games), True, 255, 255, 255, screen.get_width() / 4 * 3 - 50,
         screen.get_height() / 32 * 18]
    screen = Texts(T,screen,x2)
    T = [None, 25, "Achievements: " + str(len(Ach)), True, 255, 255, 255, screen.get_width() / 4 * 3 - 50,
         screen.get_height() / 32 * 19]
    screen = Texts(T,screen,x2)
    T = [None, 25, "Version: " + "Alpha " + varl[:1] + "." + varl[1:], True, 255, 255, 255, screen.get_width() / 4 + 50,
         screen.get_height() / 32 * 14]
    screen = Texts(T,screen,x2)
    T = [None, 25, "Record lv.3: " + str(Save[6]), True, 255, 255, 255, screen.get_width() / 4 + 50,
         screen.get_height() / 32 * 17]
    screen = Texts(T,screen,x2)
    T = [None, 25, "Record lv.2: " + str(Save[3]), True, 255, 255, 255, screen.get_width() / 4 + 50,
         screen.get_height() / 2]
    screen = Texts(T,screen,x2)
    T = [None, 25, "Record lv.1: " + str(Save[2]), True, 255, 255, 255, screen.get_width() / 4 + 50,
         screen.get_height() / 32 * 15]
    screen = Texts(T,screen,x2)
    T = [None, 25, "Date: " + str(Save[0])[0:4] + "-" + str(Save[0])[4:6] + "-" + str(Save[0])[6:] + " " + str(hour) + ":" + str(rminu) + ":" + str(rsec), True, 255, 255, 255, screen.get_width() / 4 + 50,
         screen.get_height() / 32 * 13]
    screen = Texts(T,screen,x2)
    T = [None, 25, "Games won: " + str(Save[5]), True, 255, 255, 255, screen.get_width() / 4 + 50,
         screen.get_height() / 32 * 18]
    screen = Texts(T,screen,x2)
    T = [None, 25, "Achievements: " + str(Ach1), True, 255, 255, 255, screen.get_width() / 4 + 50,
         screen.get_height() / 32 * 19]
    screen = Texts(T,screen,x2)
    if go == "left":
        saveprompt = "noo"
    if go == "y" and saveprompt != "no" and saveprompt != "noo":
        file = open('save.txt', 'w')
        file.write(saveprompt)
        file.close()
        save = False
    if go == "y" and saveprompt == "noo":
        Ach = Ach3
        save = False
        if Save != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            games = int(Save[5])
            bhs = int(Save[2])
            qhs = int(Save[3])
            hs = int(Save[6])
    return save, games, bhs, qhs, hs, Ach

pygame.init()
try:
    x1 = int(input("Recommended Screenlength: 1280 | Screenhight: 786\nScreenlengh:"))
except ValueError:
    x1 = 1280
try:
    y1 = int(input("Screenhight:"))
except ValueError:
    y1 = 786
x2 = x1/1280
y2 = y1/786
if x2 > y2:
    x2 = y2
screen = pygame.display.set_mode([x1, y1])  # half is 393
screen.fill([0, 0, 0])
go, shad, uds, menu, game, A, save, achi = "°", 127, 8, False, False, [], False, False
q, b, notthird, goal, x, zu, nex = 0, 0, True, 10, 0, 0, ""
stoppy, ten = False, -1
Ach = []
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
            for sha in range(0, 9):
                T = [None, int(200), "NUMERS", True, 127 + sha * 16, 127 + sha * 16, 127 + sha * 16,
                     screen.get_width() / 2 + sha, 100 + sha,screen,x2]
                screen = Texts(T,screen,x2)
            pygame.display.set_caption("NUMERS " + totalvs + semi)
            for sha in range(0, 5):
                font = pygame.font.Font(None, 100)
                text = font.render(totalvs, True, (127 + sha * 32, 127 + sha * 32, 0))
                font2 = pygame.font.Font(None, 75)
                text2 = font2.render(semi, True, (127 + sha * 32, 127 + sha * 32, 0))
                textpos = text.get_rect(centerx=screen.get_width() / 2 + sha - text2.get_width() / 2, y=256 + sha)
                textpos2 = text2.get_rect(
                    x=text.get_width() / 2 + screen.get_width() / 2 + sha / 2 - text2.get_width() / 2,
                    bottom=323 + sha / 2)  # shall work for .x.y too
                screen.blit(text, textpos)
                screen.blit(text2, textpos2)
            T = [None, 50, "Press Return to Start!", True, shad, shad, shad, screen.get_width() / 2,
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
        if menu == True:
            screen.fill([0, 0, 0])
            if change != True and achi != True and save != True:
                T = [None, 200, "MENU", True, 255, 255, 255, screen.get_width() / 2, screen.get_height() / 8]
                screen = Texts(T,screen,x2)
                T = [None, 100, "Play", True, Choice[0], Choice[0], Choice[0], screen.get_width() / 2,
                     screen.get_height() / 8 * 3]
                screen = Texts(T,screen,x2)
                T = [None, 75, "Statistics*", True, Choice[1], Choice[1], Choice[1], screen.get_width() / 4,
                     screen.get_height() / 8 * 4]
                screen = Texts(T,screen,x2)
                T = [None, 75, "Changelog", True, Choice[3], Choice[3], Choice[3], screen.get_width() / 4 * 3,
                     screen.get_height() / 8 * 4]
                screen = Texts(T,screen,x2)
                T = [None, 75, "Savestates", True, Choice[2], Choice[2], Choice[2], screen.get_width() / 2,
                     screen.get_height() / 8 * 4]
                screen = Texts(T,screen,x2)
                T = [None, 50, "*Not available right now", True, 127, 127, 127, screen.get_width() / 2,
                     screen.get_height() / 4 * 3.5]
                screen = Texts(T,screen,x2)
                T = [None, 75, "Achievements", True, Choice[4], Choice[4], Choice[4], screen.get_width() / 2,
                     screen.get_height() / 8 * 5]
                screen = Texts(T,screen,x2)
            go = Return(go)
            if change == True:
                screen, down = Changelog(screen, down, x2)
            elif save == True:
                save, games, bhs, qhs, hs, Ach = Savestates(screen, go, tog, games, save, qhs, bhs, hs, Ach)
            elif achi == True:
                screen, achi = Achieves(Ach, screen, x2, achi)
            elif go == "y" and Choice[0] == 255:
                menu = False
                game = True
            elif go == "y" and Choice[1] == 255:
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
                screen, achi = Achieves(Ach, screen, x2, achi)
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
    if game == True:
        menu = False
        sec, minit, hour, day = "", "", "", ""
        go = Return(go)
        if go == "y":
            go1 = True
        if total >= 1000000 and go == "y":
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
        c, stoppy, ten = PV_ani(b, extra, notthird, goal, A, tick, nixt, stoppy, a, ten, screen, noxt, naxt, q, total, pre, zu, x, nex, poss, rest, rest1, rest2, rest0)
        if tick == 100:
            if go1 == True:
                go = "y"
                go1 = False
                stoppy = False
            tick = 0
            tack = tack + 1
            if total < 999999:
                a1, n1, L2, a, go, b, noxt, naxt, nixt, q, total, goal, pre, zu, nex, x, poss, rest, rest1, rest2, rest0, Ach = Numers_Forward(a1, n1, L2, a, go, noxt, naxt, nixt, q, total, b, Ach)
            if total >= 1000000:
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
