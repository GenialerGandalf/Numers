
# -*- coding: iso-8859-2 -*-

import random, time, pygame, sys, datetime #eclipse for launch without download, or hello world 

def Changelog(screen, down):
    Version = [["dev-0.0", "---{2022-11-15}---", "add: iso-codeline", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "Here is a not added hidden achievement lol"],
               ["dev-0.1", "---{2022-11-15}---", "add: random import"],
               ["dev-0.2", "---{2022-11-15}---", "add: random print 0-8"],
               ["dev-0.3", "---{2022-11-15}---", "add: 0 = Game over"],
               ["dev-0.4", "---{2022-11-15}---", "add: point display"],
               ["dev-0.5", "---{2022-11-15}---", "add: final score print"],
               ["dev-1.0", "---{2022-11-15}---", "fix: final score print"],
               ["dev-1.1", "---{2022-11-15}---", "add: remove 1 every round"],
               ["dev-1.2", "---{2022-11-15}---", "add: 'points' behind the points"],
               ["dev-1.3", "---{2022-11-15}---", "add: points of round print"],
               ["dev-1.3-a", "---{2022-11-15}---", "fix: first round has a +1"],
               ["dev-2.0", "---{2022-11-15}---", "fix: not a singular for 1 point"],
               ["dev-3.0", "---{2022-11-15}---", "fix: every result only once"],
               ["dev-4.0", "---{2022-11-15}---", "fix: dev-3.0 not finished", "add: multipliers, ^2"],
               ["dev-4.1", "---{2022-11-15}---", "fix: broken return of multipliers"],
               ["dev-5.0", "---{2022-11-15}---", "add: enter to get next draw"],
               ["--------------------------------------   Early development   --------------------------------------"],
               ["alpha-1.0", "---{2022-11-15}---", "add: exact hit achievement", "add: text for pt.2"],
               ["alpha-1.1", "---{2022-11-15}---", "add: list of values"],
               ["alpha-1.2", "---{2022-11-15}---", "fix: broken randomisation in pt.2", "add: output of the random value"],
               ["alpha-1.3", "---{2022-11-15}---", "remove: output of the random value", "add: output from the point list"],
               ["alpha-1.4", "---{2022-11-15}---", "fix: remove values from point list"],
               ["alpha-1.5", "---{2022-11-15}---", "fix: deleted optional 2nd space in lv.1 output", "add: all +, *, ** and *0", "add: output for lv.2"],
               ["alpha-1.6", "---{2022-11-15}---", "fix: Achievments now Achievements", "add: text for getting special numbers", "add: final score return in lv.2"],
               ["alpha-2.0", "---{2022-11-15}---", "add: giant loop with question for leaving or staying at the end"],
               ["alpha-2.1", "---{2022-11-15}---", "add: time import", "add: loops now have a 500ms wait time", "add: Numers lv.3 text", "change: now requirering 1 billon instead of 1 million", "change: *0 in lv.1 is now +5"],
               ["alpha-2.2", "---{2022-11-15}---", "add: all 512 different values for lv.3"],
               ["alpha-2.3", "---{2022-11-15}---", "add: random generator for lv.3", "add: pygame import", "change: random generator for lv.2"],
               ["alpha-2.4", "---{2022-11-15}---", "fix: list index out of range in lv.2", "add: output of value in lv.3", "change: now 100ms wait time for new game", "change: only 1 million needed instead of 1 billion for lv.3", "change: random generator for lv.3"],
               ["alpha-2.5", "---{2022-11-15}---", "fix: list index out of range in lv.3", "add: calculation for +, -, *, /, ^", "add: output of final score on lv.3"],
               ["alpha-2.6", "---{2022-11-15}---", "add: output line now shows the change on the score in lv.3", "add: root calculation"],
               ["alpha-2.7", "---{2022-11-15}---", "add: Ready? input at the beginnning", "add: lifes", "add: extra Turns", "add: -score and 1/score", "fix some prints having two operators", "fix: total too long"],
               ["alpha-2.8", "---{2022-11-17}---", "add: sys import", "add: Booster(^-1, *-1, *0, *-1, -3, -2, -1, 1, 2, 3}---", "add: prints if divided or rooted by 0", "fix: shorten numbers even if they're smaller then 1 billion"],
               ["alpha-2.9", "---{2022-11-30}---", "add: round counter", "add: inx, iny, inz, ina", "add: rb, rc", "add: l+n, lxn, l^n, l?n"],
               ["alpha-3.0", "---{2022-12-01}---", "add: repeat x i times", "add: waiting time in lv.2 (1s}---", "change: waiting time in lv.1 to 500ms"],
               ["alpha-3.1", "---{2023-01-13}---", "add: Pygame window", "add: closing the window", "change waiting time in lv.1 to 1s"],
               ["alpha-3.2", "---{2023-01-13}---", "fix: Pygame window showing text", "add: Title screen"],
               ["alpha-3.3", "---{2023-01-13}---", "add: 1. funktion: ptsview", "add: ptsview showing the numberline -1 to 11"],
               ["alpha-3.4", "---{2023-01-13}---", "add: ptsview showing the points with a blue line", "add: ptsview multiplying its numbers by 10", "add: ptsview adds little lines when in lv. 3"],
               ["alpha-3.5", "---{2023-01-14}---", "add: Goal to reach display for lv.1", "add: arrow + number representing current score", "change: waiting time in lv.1 to 200ms", "fix: ptsview showing 0 pts when you lost"],
               ["alpha-3.6", "---{2023-01-15}---", "change: 'NUMERS' in title screen colored yellow", "add: display of the rolled value", "add: goal working for every level", "fix: ptsview now showing the last frame again", "change: waiting time for lv.1 to 1s"],
               ["alpha-3.7", "---{2023-01-15}---", "fix: arrow and number score presentation to low", "change: points required to reach lv.2 to 10", "change: points required to reach lv.3 to 1000", "change: points required to beat Numers Forward to 1000000"],
               ["alpha-3.8", "---{2023-01-16}---", "change: waiting time in numers lv.3 now at the end"],
               ["alpha-3.9", "---{2023-01-24}---", "fix: ptsview in negative areas not working", "fix: pointcounter in negative area compleatly broken", "fix: color cheme in negative areas", "add: millions, billions etc. display"],
               ["alpha-4.0", "---{2023-01-25}---", "add: function Numers Forward", "change: the programm structure"],
               ["alpha-4.1", "---{2023-01-25}---", "add: function Calcul1000", "change: it calculates any given number into M, B, T etc.", "add: automatc update on the version in Start screen by using the file name"],
               ["alpha-4.2", "---{2023-01-31}---", "add: first Frame structure", "change: spliting Numers Forward in 3", "add: NF1 function, which is lv.1", "add: NF2 function, which is lv.2", "add: NF3 function, which is lv.3"],
               ["alpha-4.3", "---{2023-02-17}---", "change: the .x version number is now smaller", "fix: progression to lv.2 and lv.3 not possible", "add: the window can now be closed at any given time", "add: the 'Press Return to Start' text is now animated"],
               ["alpha-4.4", "---{2023-02-20}---", "add: higher combinations of M, B, T etc. so that the maximum is now 10^5999", "fix: .y Version counter not centered"],
               ["alpha-4.5", "---{2023-02-25}---", "add: Pygame Tab now named Numers plus the current version", "add: when the Game starts, a timer in the Game Tab will count up"],
               ["alpha-4.6", "---{2023-02-25}---", "add: end game Screen", "change: faster cycle for the animation of the Game Start"],
               ["alpha-4.7", "---{2023-02-25}---", "add: low row to show what results a left in lv.1", "fix: rest0owed instead of allowed and more", "add: + - turns display on the value line", "change: lv.1 now containing +5 instead of *0"],
               ["alpha-4.8", "---{2023-02-28}---", "add: Menu screen with Play, Statistics, Load save and Changelog", "add: navigation to move left, up, down, right with inputs", "add: Enter at Play to start the game"],
               ["alpha-4.9", "---{2023-02-28}---", "add: function Texts to make text universal", "change: merging some variables to remove lines from the code"],
               ["alpha-5.0", "---{2023-04-18}---", "add: Changelog access", "add: Changelog dev Versions"],
               ["alpha-5.1", "---{2023-04-18}---", "add: Changelog alpha version until alpha 3.0", "fix: blue line, finally"],
               ["alpha-5.2", "---{2023-04-18}---", "fix: Changelog not marked as availiable mode", "add: changelog until current version"],
               ["alpha-5.3", "---{2023-04-18}---", "change: Changelog design", "fix: Changelog render lag", "add: lines at dates and early dev"],
               ["alpha-5.4", "---{2023-04-19}---", "change: colored the dates", "add: holdable up, down, left and right", "fix: left and right pressed in changelog issue"],
               ["alpha-5.5", "---{2023-04-29}---", "change: Load Save now called Savestates", "add: Achievements selection", "fix: after beating the Game it's not possible to get the the Menu", "add: swiching back to the start screen"],
               ["alpha-5.6", "---{2023-06-16}---", "fix: esc to the menu only working on Changelog option", "fix: when playing again, it starts on lv.3", "fix: game starts on menu esc is pressed on 'Play'"],
               ["alpha-5.7", "---{2023-06-16}---", "fix: time resetting itself after restart", "add: save menu", "add: highscore of lv.1 and lv.2", "add: Time display", "add: Games played"],
               ["alpha-5.8", "---{2023-06-16}---", "add: save print", "add: highlight chosen option in saves"],
               ["alpha-5.9", "---{2023-11-10}---", "add: save file loading", "change: '/Alpha 5.8/' part is now a number: '/59/'"],
               ["alpha-5.a", "---{2023-11-19}---", "re-add: enter to continue in game", "fix: Game time running 4 times to fast"],
               ["alpha-5.b", "---{2023-11-20}---", "add: 2 low rows to show possibilities in lv.2", "add: leaving mid game via pressing esc"],
               ["alpha-5.c", "---{2023-11-20}---", "add: lv.3 save", "fix: overwrite of highscores"],
               ["alpha-5.d", "---{2023-11-20}---", "change: 'Games played' now 'Games won'", "fix: Game Over now without 0", "change: loosing lv.3 gets you back to lv.1"],
               ["alpha-5.e", "---{2023-11-20}---", "change: add of '' in changelog", "fix: 'M' shorts number after 'De'", "change: Failing Lv.3 puts you now in the Menu"],
               ["alpha-6.0", "---{2023-11-27}---", "change: lower ^x, due to them being broken", "add: animation to the moving arrow and line"],
               ["alpha-6.1", "---{2023-11-27}---", "change: animation now smoother", "add: animation for lv.2", "fix: max score in Lv.1 not winning"],
               ["alpha-6.2", "---{2023-11-27}---", "add: animation now compleatly working for lv.3", "fix: changelog mistake 't'"],
               ["alpha-6.3", "---{2023-11-29}---", "fix: too much lag due to drawing", "add: Gameover screen for Lv.2", "--------------------------------------------------------------------------", "fix: oldest unknown Bug!", "From (Alpha 1.5) found in (Alpha 6.3)", "Lv.2 Calculuating another turn after getting 'Game Over'", "--------------------------------------------------------------------------"],
               ["alpha-6.4", "---{2023-11-29}---", "fix: Saves score of Lv.2 as score of Lv.1 too", "fix: points wrap after reaching 11*(10^x)", "fix: Lv.3 not having neg-arae when loading", "fix: Number scale now 'Long Scale'", "fix: big numbers overlaping in the scale", "fix: repeater not working due to floats", "fix: Game won screen still showing the line", "fix: the line doesn't move towards 0", "fix: save output for Lv.3 not working for high numbers", "fix: hard to read Save or Load due to the selecor"],
               ["alpha-6.5", "---{2024-01-15}---", "fix: opposing number in Lv.3 not getting smaller", "fix: highscore affected by scores midgame", "add: custom size support"],
               ["alpha-6.6", "---{2024-01-16}---", "fix: most text overlapping after scaling"]
               ]
    screen.fill([0, 0, 0])
    deve = 1
    alp = 0
    line = 0
    T = [None, 100, "Changelog", True, 255, 255, 255, hintergrund.get_width()/2, hintergrund.get_height()/16]
    screen = Texts(T)
    for dev in range(0, len(Version)):
        sub = Version[len(Version)-dev-1]
        if hintergrund.get_height()/8 + 45 + 60*dev + 30*(line+1) - down*25 > hintergrund.get_height()/8 + 50 and hintergrund.get_height()/8 + 45 + 60*dev + 30*(line+1) - down*25 < hintergrund.get_height() - 10:
            if sub[0] == "--------------------------------------   Early development   --------------------------------------":
                if hintergrund.get_height()/8 + 45 + 60*dev + 30*(line+1) - down*25 < hintergrund.get_height() - 10:
                    T = [None, 50, sub[0], True, 255, 255, 127, hintergrund.get_width()/2, hintergrund.get_height()/8 + 45 + 60*dev + 30*(line+1) - down*25]
                    screen = Texts(T)
            if sub[0] != "--------------------------------------   Early development   --------------------------------------":
                T = [None, 50, sub[0], True, 255, 255, 0, hintergrund.get_width()/2, hintergrund.get_height()/8 + 45 + 60*dev + 30*(line+1) - down*25]
            screen = Texts(T)
        if len(sub) > 0:
            for deve in range(1, len(sub)):
                if deve > 1:
                    line = line + 1
                if hintergrund.get_height()/8 + 40 + 60*dev + 30*(line+2) - down*25 > hintergrund.get_height()/8 + 50 and hintergrund.get_height()/8 + 40 + 60*dev + 30*(line+2) - down*25 < hintergrund.get_height() - 10:
                    T = [None, 25, sub[deve], True, 127, 255, 0, hintergrund.get_width()/2, hintergrund.get_height()/8 + 40 + 60*dev + 30*(line+2) - down*25]
                    if deve == 1:
                        T = [None, 25, sub[deve], True, 191, 255, 63, hintergrund.get_width()/2, hintergrund.get_height()/8 + 40 + 60*dev + 30*(line+2) - down*25]
                    screen = Texts(T)
        if sub[0] == "--------------------------------------   Early development   --------------------------------------" and hintergrund.get_height()/8 + 45 + 60*dev + 30*(line+1) - down*25 > hintergrund.get_height()/8 + 50:
            T = [None, 75, "Alpha development", True, 255, 255, 127, hintergrund.get_width()/2, hintergrund.get_height()/8 + 20]
            alp = 1
            screen = Texts(T)
    if hintergrund.get_height()/8 + 25 + 60*dev + 30*(line+1) - down*25 > hintergrund.get_height()/8 and alp == 0:            
        T = [None, 75, "Early development", True, 255, 255, 127, hintergrund.get_width()/2, hintergrund.get_height()/8 + 20]
        screen = Texts(T)
    return screen, down

def Return(go):
    if go == "down-up" or go == "up-up" or go == "right-up" or go == "left-up":
        go = "°"
    elif go == "n" or go == "y" or go == "esc" or go == "":
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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                go = "down-up"
            if event.key == pygame.K_UP:
                go = "up-up"
            if event.key == pygame.K_RIGHT:
                go = "left-up"
            if event.key == pygame.K_LEFT:
                go = "right-up"  
    return go

def Calcul1000(cent):
    cal, ten, mil, deci, centi = cent, 0, 0, 0, 0
    while cent >= 10 or cent <= -10:
        while cent >= 1000000 or cent <= -1000000:
            cent, mil = cent / 1000000, mil + 1
        if cent >= 10 or cent <= -10:
            cent, ten = cent / 10, ten + 1
    while mil >= 10:
        deci = deci + 1
        mil = mil - 10
    while deci >= 10:
        centi = centi + 1
        deci = deci - 10
    MIL, MIL2, DECI, CENTI = ["","M","B","T","Q","q","S","s","O","N"], ["","U","D","T","Q","q","S","s","O","N"], ["","De","Vi","Tr","Qu","qu","Se","se","Ok","No"], ["","Cen","Duc","Tre","Qua","Qui","Ses","Sep","Oct","Non"]
    if cal < 1000000000000000000:
        kar = MIL[mil] + DECI[deci] + CENTI[centi]
    else:
        kar = MIL2[mil] + DECI[deci] + CENTI[centi]
    mil = mil + deci*10 + centi*100
    return kar, ten, mil, cent

def Rlsview(A):
    if len(A) > 0:
        if len(A) < 10 and A[0] != "[":
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
        else:
            font = pygame.font.Font(None, 22)
            B1 = str(A)
            text = font.render((B1), True, (255, 255, 0))
            if A[0] != "[":
                textpos = text.get_rect(centerx = screen.get_width()/2, y = 700)
            else:
                text = font.render((B1), True, (255, 127, 0))
                textpos = text.get_rect(centerx = screen.get_width()/2, y = 666)
        screen.blit(text, textpos)

def Drawline():
    if game == True:
        print("hello")
    
def Ptsview(c,extra,a,notthird,goal,A,nuxt):
    global nah, ten
    cent = int(c)
    lten = ten
    kar, ten, mil, cent = Calcul1000(cent)
    rz, wz, mn1, p0 = 255, 0, 1, 140
    if ten != lten or c == 0:
        screen.fill([0, 0, 0])
    if tick == 100 or ten != lten or c == 0:
        mark = pygame.draw.rect(screen, (0, 0, 0), (0, 450, 1280, 350))
        Rlsview(A)
        if goal == 1000:
            A1 = A
            A = str(rest)
            Rlsview(A)
            A = A1
        if goal == 1000000:
            Rlsview(rest1)
            Rlsview(rest2)
    if cent + cent < cent:
        rz, wz, p0, mn1 = 0, 255, 1140, -1
    yik = p0 + int(c*100/((10**ten)*(1000000**mil)))
    if c < nuxt and nuxt >= 0:
        line = pygame.draw.rect(screen, (255, rz, rz), (p0*rz/255, 390, 1140, 5))
    elif c > nuxt and c < 0:
        line = pygame.draw.rect(screen, (255, rz, rz), (p0*rz/255, 390, 1140, 5))
    if ten != lten or c == 0:
        line = pygame.draw.rect(screen, (255, rz, rz), (p0*rz/255, 390, 1140, 5))
        for dec in range(0, 12):
            if dec == 10 or dec == 0:
                mark = pygame.draw.rect(screen, (255, rz, rz), ((p0 - 2 + mn1 * 100 * dec), 375, 5, 35))
            mark = pygame.draw.rect(screen, (255, rz, rz), ((p0 - 1 + mn1 * 100 * dec), 380, 3, 25))
        if goal == 1000000:
            mark = pygame.draw.rect(screen, (255, wz, wz), (p0 - 140*rz/255, 390, 138, 5))
            mark = pygame.draw.rect(screen, (255, wz, wz), (p0 - 100 * mn1 - 1, 380, 3, 25))
            font = pygame.font.Font(None, 40-ten*3)
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
            font = pygame.font.Font(None, 40-ten*3)
            if dec == 0:
                text = font.render(str(dec * (10**ten)), True, (255, rz, rz))
            else:
                text = font.render(str(dec * (10**ten)) + kar, True, (255, rz, rz))
            textpos = text.get_rect(centerx = p0 + dec * 100, y = 420)
            screen.blit(text, textpos)
    else:
        mark = pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1280, 372))
    if ten + mil > 0 and notthird == True:
        for dec in range(0, 115):
            mark = pygame.draw.rect(screen, (255, rz, rz), ((140 + 10 * dec), 385, 1, 15))
    zun = p0 - p0*wz/255 + yik*wz/255
    line = pygame.draw.rect(screen, (0, 0, 255), (zun, 391, (yik-140)*rz/255+(p0-zun)*wz/255, 3))
    pygame.draw.polygon(screen, (0,255,0), ([yik-8,350],[yik,370],[yik+8,350]))
    font = pygame.font.Font(None, 40)
    text = font.render(str(c), True, (0, 255, 0))
    textpos = text.get_rect(centerx = yik, y = 320)
    screen.blit(text, textpos)
    font = pygame.font.Font(None, 40)
    if int(c) <= goal/10 and goal != 10:
        text = font.render("Goal: " + str(goal), True, (255, 255, 255))
        pygame.draw.polygon(screen, (255,255,255), ([1220,270],[1220,290],[1240,280]))
    elif int(c) >= goal:
        text = font.render("Goal: " + str(goal), True, (0, 255, 0))
    else:
        text = font.render("Goal: " + str(goal), True, (255, 255, 255))
        pygame.draw.polygon(screen, (255,255,255), ([1130,300],[1140,320],[1150,300]))
    textpos = text.get_rect(right = 1200, centery = 280)
    screen.blit(text, textpos)
    if extra != "a":
        font = pygame.font.Font(None, 100)
        if extra != "Game Over":
            text = font.render((str(extra) + " " + str(a)), True, (0, 255, 255))
        else:
            text = font.render(str(extra), True, (0, 255, 255))
        textpos = text.get_rect(centerx = 640, y = 200)
        screen.blit(text, textpos)
    nah = int(b)
    pygame.display.flip()

def PV_ani(b,extra,notthird,goal,A,tick,nixt):
    global stoppy
    if goal == 10:
        if stoppy == True:
            c = b
        else:
            c1 = b -(b-nixt)*(100-tick)/100
            c = int(c1)
            if c != c1:
                c = int(c1*100)/100
        Ptsview(c, extra, a, notthird, goal, A, nixt)
        if tick == 96:
            stoppy = True
    if goal == 1000:
        if stoppy == True:
            c = q
        else:
            c1 = q -(q-noxt)*(100-tick)/100
            c = int(c1)
            if c != c1:
                c = int(c1*100)/100
        Ptsview(c, zu, x, notthird, goal, poss, noxt)
        if tick == 96:
            stoppy = True
    if goal == 1000000:
        if stoppy == True:
            c = total
        else:
            c1 = total -(total-naxt)*(100-tick)/100
            c = int(c1)
            if c != c1:
                c = int(c1*100)/100
        Ptsview(c, pre, nex, notthird, goal, rest0, naxt)
        if tick == 96:
            stoppy = True

def Texts(T):
    font = pygame.font.Font(T[0], int(T[1]*x2))
    text = font.render(T[2], T[3], (T[4], T[5], T[6]))
    textpos = text.get_rect(centerx = T[7], centery = T[8])
    screen.blit(text, textpos)
    return screen

def NF1(a1, a, go):
    global extra, goal, ten
    goal = 10
    if a1 == 0:
        global b, notthird, n1, A, nixt
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
            A.remove(a)                             #Error 003: a is not suscriptable (fixed dev_3.0)
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
                print ('(' + extra  +' '+ a + ') --> ' + b +' point')
            else:
                print ('(' + extra  +' '+ a + ') --> ' + b +' points')         #Error 001: a gave +1 at beginning (fixed dev_1.3-a)                                            
            a = int(a)
            b = int(b)
    if a1 == 0:
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
            n1 = 1
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
        ten = -1
    return n1, a1, a

def NF2(n1):
    global goal, noxt
    goal = 1000
    global q, poss, rest, g, zu, x, a2, extra, p, b, L2
    if n1 == 3 and go == "y":
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
        a2 = 0
        n1 = 4
    if n1 == 1 and L2 == 0:
        print ("This is the next level, it's a modified version of the very first numers.")
        a2 = 1
        q = 0
        poss = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,7,7,7,7,10,10,10,10,13,13,13,13,16,16,16,16,20,20,20,20,30,30,30,30,60,60,90,90,200,200,400,0]
        rest = [8,8,8,8,8,8,8,8]
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
            dop = random.randint(0,7)
            kop = random.randint(0,rest[dop])                           #Error 005:IndexError: list index out of range (fixed alpha_2.4)
            mop = random.randint(0,g)
            if kop == 0:
                n1 = 3
                zu = "Game Over"
            else:
                hop = dop
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
        else:
            L2 = 0
    return L2, n1

def NF3(L2):
    global goal
    goal = 1000000
    if L2 == 1:
        global naxt, notthird, count, roun, rest0, rest1, rest2, rest3, PTR, agob, rounb, l, k, rep, a2, total, cal, prei, inx, iny, inz, ina, rinx, riny, rinz, rina, rb, rc, t, bra, brat, bratt, ln, mul, pre, last, nex, div, neg, live, redt, TC, mi, br, BSTv, BST, total
        notthind = False
        print ('This is the planned Numers 2.0')
        print ('Today it should show the great viarity of values u can have. And there will be added even more!')
        count = 0
        roun = 0
        n1 = 2
        rest0 = [-16384000000000,-128000000000,-128000000000,-128000000000,-960000000,-480000000,-480000000,-480000000,-240000000,-240000000,-240000000,-240000000,-240000000,-120000000,-120000000,-120000000,-120000000,-120000000,-120000000,-120000000,-60000000,-50000000,-50000000,-50000000,-40000000,-40000000,-40000000,-40000000,-40000000,-30000000,-30000000,-30000000,-30000000,-30000000,-30000000,-30000000,-20000000,-20000000,-20000000,-20000000,-20000000,-20000000,-20000000,-20000000,-20000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-10000000,-1048576,-1024,-1024,-1024,-512,-256,-256,-256,-128,-128,-128,-128,-128,-64,-64,-64,-64,-64,-64,-64,-32,-28,-28,-28,-24,-24,-24,-24,-24,-20,-20,-20,-20,-20,-20,-20,-16,-16,-16,-16,-16,-16,-16,-16,-16,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-12,-8,-7,-7,-7,-6,-6,-6,-6,-6,-5,-5,-5,-5,-5,-5,-5,-4,-4,-4,-4,-4,-4,-4,-4,-4,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,15,15,15,15,15,15,15,15,22,22,22,22,22,22,22,22,29,29,29,29,29,29,29,29,36,36,36,36,36,36,36,36,43,43,43,43,43,43,43,43,50,50,50,50,50,50,50,50,57,57,57,57,57,57,57,57,64,64,64,64,64,64,64,64,128,128,128,128,128,128,128,192,192,192,192,192,192,192,256,256,256,256,256,256,256,320,320,320,320,320,320,320,384,384,384,384,384,384,384,448,448,448,448,448,448,448,512,512,512,512,512,512,512,1000,1000,1000,1000,1000,1000,2000,2000,2000,2000,2000,2000,3000,3000,3000,3000,3000,3000,4000,4000,4000,4000,4000,4000,5000,5000,5000,5000,5000,5000,6000,6000,6000,6000,6000,6000,12000,12000,12000,12000,12000,18000,18000,18000,18000,18000,24000,24000,24000,24000,24000,30000,30000,30000,30000,30000,36000,36000,36000,36000,36000,81000,81000,81000,81000,126000,126000,126000,126000,171000,171000,171000,171000,216000,216000,216000,216000,2000000,2000000,2000000,3000000,3000000,3000000,4000000,4000000,5000000,5000000,6000000,6000000,7000000,8000000,"^-1","x0","x-1","x-2","-3","-2","-1","1","2","3","inx","iny","inz","ina","rb","rc","(i)","t","-4t","-3t","-2t","-1t","0t","1t","2t","3t","4t","l+n","l+n","l+n","lxn","lxn","l^n","l?n","^(-1)","^(-1)","^(-1)","x(-1)","x(-1)","x(-1)","x0","^0","/0","l"]
        rest1 = [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]
        rest2 = [64,64,64,64,64,64,64,64]
        rest3, PTR, agob, rounb, l, k, rep, a2, total, L2, cal, prei, inx, rinx, riny, rinz, rina, iny, inz, ina, rb, rc, bra, bratt, t, brat, ln, mul, pre, last, nex = 512, [], 0, [], 64, 8, 1, 1, 0, 2, 0, "", 0, 0, 0, 0, 0, 0, 0, 0, False, False, False, False, 0, 0, 0, "", "", 0, ""
        div, neg, live, redt, TC, mi, br, BSTv, BST = False, False, 0, False, [0,0,0,0,0,0,0,0,0,0,0], 1, 0, [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0] # for negative at ^-1
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
            for why in range (0,int(rep)):
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
        else:
            idk = 1
    if t < 0:
        print (TC[-t])
        L2 = -1
        n1 = -1
    return n1, L2
             
def Numers_Forward(a1, n1, L2, a, go):
    if L2 > 0 and total < 1000000:
        n1, L2 = NF3(L2)
    elif n1 > 0 and L2 == 0:
        L2, n1 = NF2(n1)
    elif n1 == 0 and L2 == 0:
        n1, a1, a = NF1(a1, a, go)
    return a1, n1, L2, a, go

def Savestates(screen, go, tog, games, save, qhs, bhs, hs):
    global select, saveprompt, sinput, Save
    if go == "":
        base = 8 #Amount of parameters in Save prompt
        select = 0
        screen.fill([0, 0, 0])
        T = [None, 75, "Paste your save in the Python Shell", True, 255, 255, 255, screen.get_width()/2, screen.get_height()/4]
        screen = Texts(T)
        T = [None, 50, "If you don't have one, just press Enter in the Python Shell", True, 255, 255, 255, screen.get_width()/2, screen.get_height()/2]
        screen = Texts(T)
        pygame.display.flip()
        sinput = input (">>> ") + "/"
        Save = []
        while sinput.find("/") != -1:
            posi = sinput.find("/")
            if posi != 0:
                Save.append(sinput[:posi])
            sinput = sinput[posi+1:]
        if Save == []:
            Save = [0,0,0,0,0,0]
        if len(Save) == 6:
            Save.append(0)
            Save.append(0)
        save = False
        go = ""
        saveprompt = "no"
    current_time = datetime.datetime.now()
    screen.fill([0, 0, 0])
    if go == "right" or select == 1:
        pygame.draw.rect(screen, (0, 0, 255), (screen.get_width()/2+20, 250, 480, 550))
        select = 1
        slv1 = int(bhs)
        slv2 = int(qhs)
        stime = int(str(current_time)[17:19]) + int(str(current_time)[14:16])*60 + int(str(current_time)[11:13])*3600
        sdate = str(current_time)[0:4] + str(current_time)[5:7] + str(current_time)[8:10]
        saveprompt = sdate + "/" + str(stime) + "/" + str(slv1) + "/" + str(slv2) + "/" + version[__file__.index("alpha_")+6] + version[__file__.index("alpha_")+8] + "/" + str(games) + "/" + str(int(hs))
    if go == "left" or select == 2:
        pygame.draw.rect(screen, (0, 0, 255), (140, 250, 480, 550))
        select = 2
    hour = int(Save[1])/3600
    rhour = hour - int(hour)
    minu = rhour * 60
    rminu = int(minu)
    sec = minu * 60 - rminu*60
    rsec = int(sec)
    hour = int(hour)
    if hour < 10:
        hour = "0" + str(hour)
    if rminu < 10:
        rminu = "0" + str(rminu)
    if rsec < 10:
        rsec = "0" + str(rsec)
    T = [None, 150, "Savestates", True, 255, 255, 255, screen.get_width()/2, screen.get_height()/8]
    screen = Texts(T)
    T = [None, 75, "<- Load    or    Save ->", True, 255, 255, 255, screen.get_width()/2, screen.get_height()/4]
    screen = Texts(T)
    varl = str(Save[4])
    if varl == "Alpha 5.8":
        varl = "58"
    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width()/2-20, 250, 40, 550))
    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width()/2-500, 250, 1000, 10))
    T = [None, 25, "Record lv.3: " + str(hs), True, 255, 255, 255, screen.get_width()/4*3 - 50, screen.get_height()/32*17]
    screen = Texts(T)
    T = [None, 25, "Record lv.2: " + str(qhs), True, 255, 255, 255, screen.get_width()/4*3 - 50, screen.get_height()/2]
    screen = Texts(T)
    T = [None, 25, "Record lv.1: " + str(bhs), True, 255, 255, 255, screen.get_width()/4*3 - 50, screen.get_height()/32*15]
    screen = Texts(T)
    T = [None, 25, "Version: " + tog, True, 255, 255, 255, screen.get_width()/4*3 - 50, screen.get_height()/32*14]
    screen = Texts(T)
    T = [None, 25, "Date: " + str(current_time)[0:19], True, 255, 255, 255, screen.get_width()/4*3 - 50, screen.get_height()/32*13]
    screen = Texts(T)
    T = [None, 25, "Games won: " + str(games), True, 255, 255, 255, screen.get_width()/4*3 - 50, screen.get_height()/32*18]
    screen = Texts(T)
    T = [None, 25, "Version: " + "Alpha " + varl[:1] + "." + varl[1:], True, 255, 255, 255, screen.get_width()/4 + 50, screen.get_height()/32*14]
    screen = Texts(T)
    T = [None, 25, "Record lv.3: " + str(Save[6]) , True, 255, 255, 255, screen.get_width()/4 + 50, screen.get_height()/32*17]
    screen = Texts(T)
    T = [None, 25, "Record lv.2: " + str(Save[3]), True, 255, 255, 255, screen.get_width()/4 + 50, screen.get_height()/2]
    screen = Texts(T)
    T = [None, 25, "Record lv.1: " + str(Save[2]), True, 255, 255, 255, screen.get_width()/4 + 50, screen.get_height()/32*15]
    screen = Texts(T)
    T = [None, 25, "Date: " + str(Save[0])[0:4] + "-" + str(Save[0])[4:6] + "-" + str(Save[0])[6:] + " " + str(hour) + ":" + str(rminu) + ":" + str(rsec), True, 255, 255, 255, screen.get_width()/4 + 50, screen.get_height()/32*13]
    screen = Texts(T)
    T = [None, 25, "Games won: " + str(Save[5]), True, 255, 255, 255, screen.get_width()/4 + 50, screen.get_height()/32*18]
    screen = Texts(T)
    if go == "left":
        saveprompt = "noo"
    if go == "y" and saveprompt != "no":
        print (saveprompt)
        save = False
    if go == "y" and saveprompt == "noo":
        save = False
        if Save != [0,0,0,0,0,0,0,0]:
            games = int(Save[5])
            bhs = int(Save[2])
            qhs = int(Save[3])
            hs = int(Save[6])
    return save, games, bhs, qhs, hs
        

pygame.init()
print("Recommended Screenlength: 1280 | Screenhight: 786")
x1 = int(input("Screenlengh:"))
y1 = int(input("Screenhight:"))
x2 = x1/1280
y2 = y1/786
if x2 > y2:
    x2 = y2
screen = pygame.display.set_mode([x1,y1]) # half is 393
hintergrund = pygame.Surface(screen.get_size())
screen.fill([0, 0, 0])
go, shad, uds, menu, game, A, save = "°", 127, 8, False, False, [], False
q, b, notthird, goal, x, zu = 0, 0, True, 10, 0, 0
stoppy, ten = False, -1
total, extra = 0, ""
screen.fill([0, 0, 0])
pygame.display.flip()
tick, tack, teck, tock, tuck, a1, n1, L2, a, nah, hs, qhs, bhs, games, go1, nixt = 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, False, 0
while go != "n":
    if go != "y" and go != "n" and game == False or menu == True:
        if menu == False and go != "y" and go != "n":
            if "alpha_" in __file__:
                version = __file__.strip('.py')
                totalvs = "Alpha " + version[__file__.index("alpha_")+6]
                semi = version[__file__.index("alpha_")+7 : len(version)]
                tog = totalvs + semi
            for sha in range(0, 9):
                T = [None, int(200), "NUMERS", True, 127+sha*16, 127+sha*16, 127+sha*16, hintergrund.get_width() / 2+sha, 100+sha]
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
            go = Return(go)
            if go == "y":
                menu = True
                screen.fill([0, 0, 0])
                go = "°"
                Choice = [255,127,127,127,127]
                change = False
                down = 0
            shad = shad - uds
            if shad == 7 or shad == 127:
                uds = -uds
        if menu == True:
            screen.fill([0, 0, 0])
            if change != True:
                T = [None, 200, "MENU", True, 255, 255, 255, screen.get_width()/2, screen.get_height()/8]
                screen = Texts(T)
                T = [None, 100, "Play", True, Choice[0], Choice[0], Choice[0], screen.get_width()/2, screen.get_height()/8*3]
                screen = Texts(T)
                T = [None, 75, "Statistics*", True, Choice[1], Choice[1], Choice[1], screen.get_width()/4, screen.get_height()/8*4]
                screen = Texts(T)
                T = [None, 75, "Changelog", True, Choice[3], Choice[3], Choice[3], screen.get_width()/4*3, screen.get_height()/8*4]
                screen = Texts(T)
                T = [None, 75, "Savestates", True, Choice[2], Choice[2], Choice[2], screen.get_width()/2, screen.get_height()/8*4]
                screen = Texts(T)
                T = [None, 50, "*Not available right now", True, 127, 127, 127, screen.get_width()/2, screen.get_height()/4*3.5]
                screen = Texts(T)
                T = [None, 75, "Achievements*", True, Choice[4], Choice[4], Choice[4], screen.get_width()/2, screen.get_height()/8*5]
                screen = Texts(T)
            go = Return(go)
            if change == True:
                screen, down = Changelog(screen, down)
            if save == True:
                save, games, bhs, qhs, hs = Savestates(screen, go, tog, games, save, qhs, bhs,hs)
            elif go == "y" and Choice[0] == 255:
                menu = False
                game = True
            elif go == "y" and Choice[1] == 255:
                print ("not available yet")
            elif go == "y" and Choice[2] == 255:
                go = ""
                save, games, bhs, qhs, hs = Savestates(screen, go, tog, games, save, qhs, bhs,hs)
                save = True
            elif go == "y" and Choice[3] == 255:
                change = True
                screen, down = Changelog(screen, down)
            elif go == "y" and Choice[4] == 255:
                print ("not available yet")
            elif go == "up":
                if Choice[3] == 255 and change == True:
                    if down > 0:
                        down = down - 1
                elif Choice[4] == 255:
                    Choice = [127,127,255,127,127]
                else:
                    Choice = [255,127,127,127,127]
            elif go == "down":
                if Choice[3] == 255:
                    if change == True:
                        down = down + 1
                if Choice[0] == 255:
                    Choice = [127,127,255,127,127]
                elif Choice[0] != 255 and change != True:
                    Choice = [127,127,127,127,255]
            elif go == "right":
                if change != True:
                    if Choice[0] == 255 or Choice[2] == 255 or Choice[4] == 255:
                        Choice = [127,127,127,255,127]
                    elif Choice[1] == 255:
                        Choice = [127,127,255,127,127]
                    elif Choice[3] == 255:
                        Choice = [127,255,127,127,127]
            elif go == "left":
                if change != True:
                    if Choice[0] == 255 or Choice[2] == 255 or Choice[4] == 255:
                        Choice = [127,255,127,127,127]
                    elif Choice[1] == 255:
                        Choice = [127,127,127,255,127]
                    elif Choice[3] == 255:
                        Choice = [127,127,255,127,127]
            elif go == "esc":
                if change == True:
                    change = False
                    screen.fill([0,0,0])
                if save == True:
                    save = False
                    screen.fill([0,0,0])
                elif change == False:
                    menu = False
                screen.fill([0,0,0])
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
        PV_ani(b,extra,notthird,goal,A,tick,nixt)
        if tick == 100:
            if go1 == True:
                go = "y"
                go1 = False
                stoppy = False
            tick = 0
            tack = tack + 1
            if total < 999999:
                a1, n1, L2, a, go = Numers_Forward(a1, n1, L2, a, go)
            if total >= 1000000:
                screen.fill([0, 0, 0])
                goal = 0
                T = [None, 100, "Points: " + str(total), True, 255, 255, 255, hintergrund.get_width()/2, hintergrund.get_height()/2]
                screen = Texts(T)
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
        pygame.display.set_caption("NUMERS " + totalvs + semi + day + hour + minit + sec + " " + str(tick*10) + "ms")
        tick = tick + 4 # normaly 4
        time.sleep(0.04)
    pygame.display.flip()
pygame.quit()
