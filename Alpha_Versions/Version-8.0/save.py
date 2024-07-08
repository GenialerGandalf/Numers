import random, time, pygame, sys, datetime, tkinter
from Changelog import Changelog
from Texts import Texts

def Savestates(screen, go, tog, games, save, qhs, bhs, hs, Ach, x2, version, vers):
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
            T = [None, 75*x2, "Paste your save in the Python Shell", True, 255, 255, 255, screen.get_width() / 2,
                 screen.get_height() / 4]
            screen = Texts(T,screen,x2)
            T = [None, 50*x2, "If you don't have one, just press Enter in the Python Shell", True, 255, 255, 255,
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
        pygame.draw.rect(screen, (0, 0, 255), (screen.get_width() / 2 + 20*x2, 250*x2, 480*x2, 550*x2))
        select = 1
        achiev = 0
        for p in range(0, len(Ach)):
            achiev = achiev + 2**Ach[p]
        slv1 = int(bhs)
        slv2 = int(qhs)
        stime = int(str(current_time)[17:19]) + int(str(current_time)[14:16]) * 60 + int(
            str(current_time)[11:13]) * 3600
        sdate = str(current_time)[0:4] + str(current_time)[5:7] + str(current_time)[8:10]
        saveprompt = sdate + "/" + str(stime) + "/" + str(slv1) + "/" + str(slv2) + "/" + vers + "/" + str(games) + "/" + str(
            int(hs)) + "/" + str(achiev) + "/" + "0"
    if go == "left" or select == 2:
        pygame.draw.rect(screen, (0, 0, 255), (140*x2, 250*x2, 480*x2, 550*x2))
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
    T = [None, 150*x2, "Savestates", True, 255, 255, 255, screen.get_width() / 2, screen.get_height() / 8]
    screen = Texts(T,screen,x2)
    T = [None, 75*x2, "<- Load    or    Save ->", True, 255, 255, 255, screen.get_width() / 2, screen.get_height() / 4]
    screen = Texts(T,screen,x2)
    varl = str(Save[4])
    if varl == "Alpha 5.8":
        varl = "58"
    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() / 2 - 20*x2, 250*x2, 40*x2, 550*x2))
    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() / 2 - 500*x2, 250*x2, 1000*x2, 10*x2))
    T = [None, 25*x2, "Record lv.3: " + str(hs), True, 255, 255, 255, screen.get_width() / 4 * 3 - 50*x2,
         screen.get_height() / 32 * 17]
    screen = Texts(T,screen,x2)
    T = [None, 25*x2, "Record lv.2: " + str(qhs), True, 255, 255, 255, screen.get_width() / 4 * 3 - 50*x2,
         screen.get_height() / 2]
    screen = Texts(T,screen,x2)
    T = [None, 25*x2, "Record lv.1: " + str(bhs), True, 255, 255, 255, screen.get_width() / 4 * 3 - 50*x2,
         screen.get_height() / 32 * 15]
    screen = Texts(T,screen,x2)
    T = [None, 25*x2, "Version: " + tog, True, 255, 255, 255, screen.get_width() / 4 * 3 - 50*x2,
         screen.get_height() / 32 * 14]
    screen = Texts(T,screen,x2)
    T = [None, 25*x2, "Date: " + str(current_time)[0:19], True, 255, 255, 255, screen.get_width() / 4 * 3 - 50*x2,
         screen.get_height() / 32 * 13]
    screen = Texts(T,screen,x2)
    T = [None, 25*x2, "Games won: " + str(games), True, 255, 255, 255, screen.get_width() / 4 * 3 - 50*x2,
         screen.get_height() / 32 * 18]
    screen = Texts(T,screen,x2)
    T = [None, 25*x2, "Achievements: " + str(len(Ach)), True, 255, 255, 255, screen.get_width() / 4 * 3 - 50*x2,
         screen.get_height() / 32 * 19]
    screen = Texts(T,screen,x2)
    T = [None, 25*x2, "Version: " + "Alpha " + varl[:1] + "." + varl[1:], True, 255, 255, 255, screen.get_width() / 4 + 50*x2,
         screen.get_height() / 32 * 14]
    screen = Texts(T,screen,x2)
    T = [None, 25*x2, "Record lv.3: " + str(Save[6]), True, 255, 255, 255, screen.get_width() / 4 + 50*x2,
         screen.get_height() / 32 * 17]
    screen = Texts(T,screen,x2)
    T = [None, 25*x2, "Record lv.2: " + str(Save[3]), True, 255, 255, 255, screen.get_width() / 4 + 50*x2,
         screen.get_height() / 2]
    screen = Texts(T,screen,x2)
    T = [None, 25*x2, "Record lv.1: " + str(Save[2]), True, 255, 255, 255, screen.get_width() / 4 + 50*x2,
         screen.get_height() / 32 * 15]
    screen = Texts(T,screen,x2)
    T = [None, 25*x2, "Date: " + str(Save[0])[0:4] + "-" + str(Save[0])[4:6] + "-" + str(Save[0])[6:] + " " + str(hour) + ":" + str(rminu) + ":" + str(rsec), True, 255, 255, 255, screen.get_width() / 4 + 50*x2,
         screen.get_height() / 32 * 13]
    screen = Texts(T,screen,x2)
    T = [None, 25*x2, "Games won: " + str(Save[5]), True, 255, 255, 255, screen.get_width() / 4 + 50*x2,
         screen.get_height() / 32 * 18]
    screen = Texts(T,screen,x2)
    T = [None, 25*x2, "Achievements: " + str(Ach1), True, 255, 255, 255, screen.get_width() / 4 + 50*x2,
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
