import random, time, pygame, sys, datetime

def Return(go):
    if go == "down-up" or go == "up-up" or go == "right-up" or go == "left-up":
        go = "Â°"
    elif go == "n" or go == "y" or go == "esc" or go == "":
        go = "Â°"
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
    MIL, MIL2, DECI, CENTI = ["", "M", "B", "T", "Q", "q", "S", "s", "O", "N"], ["", "U", "D", "T", "Q", "q", "S", "s", "O", "N"], ["", "De", "Vi", "Tr", "Qu", "qu", "Se", "se", "Ok", "No"], ["", "Cen", "Duc", "Tre", "Qua", "Qui", "Ses", "Sep", "Oct", "Non"]
    if cal < 1000000000000000000:
        kar = MIL[mil] + DECI[deci] + CENTI[centi]
    else:
        kar = MIL2[mil] + DECI[deci] + CENTI[centi]
    mil = mil + deci * 10 + centi * 100
    return kar, ten, mil, cent


def Rlsview(A, screen, x2):
    if len(A) > 0:
        if len(A) < 10 and A[0] != "[":
            if len(A) > 0:
                B1 = "["
            else:
                B1 = ""
            for lena in range(0, len(A)):
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
                if lena != len(A) - 1:
                    B1 = B1 + ", "
                else:
                    B1 = B1 + "]"
            B1 = str(B1)
            font = pygame.font.Font(None, 96)
            text = font.render((B1), True, (255, 255, 0))
            textpos = text.get_rect(centerx=screen.get_width() / 2, y=700*x2)
        else:
            font = pygame.font.Font(None, 22)
            B1 = str(A)
            text = font.render((B1), True, (255, 255, 0))
            if A[0] != "[":
                textpos = text.get_rect(centerx=screen.get_width() / 2, y=700*x2)
            else:
                text = font.render((B1), True, (255, 127, 0))
                textpos = text.get_rect(centerx=screen.get_width() / 2, y=666*x2)
        screen.blit(text, textpos)


def Drawline():
    if game == True:
        print("hello")


def Ptsview(c, extra, a, notthird, goal, A, nuxt, ten, screen, tick, b, rest, rest1, rest2, x2):
    global nah
    cent = int(c)
    lten = ten
    kar, ten, mil, cent = Calcul1000(cent)
    rz, wz, mn1, p0 = 255, 0, 1, 140*x2
    if ten != lten or c == 0:
        screen.fill([0, 0, 0])
    if tick == 100 or ten != lten or c == 0:
        mark = pygame.draw.rect(screen, (0, 0, 0), (0, 450*x2, 1280*x2, 350*x2))
        Rlsview(A, screen, x2)
        if goal == 1000:
            A1 = A
            A = str(rest)
            Rlsview(A, screen, x2)
            A = A1
        if goal == 1000000:
            Rlsview(rest1, screen, x2)
            Rlsview(rest2, screen, x2)
    if cent + cent < cent:
        rz, wz, p0, mn1 = 0, 255, 1140*x2, -1
    yik = p0/x2 + int(c * 100 / ((10 ** ten) * (1000000 ** mil)))
    if c < nuxt and nuxt >= 0:
        line = pygame.draw.rect(screen, (255, rz, rz), (p0 * rz / 255, 390*x2, 1140*x2, 5*x2))
    elif c > nuxt and c < 0:
        line = pygame.draw.rect(screen, (255, rz, rz), (p0 * rz / 255, 390*x2, 1140*x2, 5*x2))
    if ten != lten or c == 0:
        line = pygame.draw.rect(screen, (255, rz, rz), (p0 * rz / 255, 390*x2, 1140*x2, 5*x2))
        for dec in range(0, 12):
            if dec == 10 or dec == 0:
                mark = pygame.draw.rect(screen, (255, rz, rz), ((p0 - 2*x2 + mn1 * 100 * dec*x2), 375*x2, 5*x2, 35*x2))
            mark = pygame.draw.rect(screen, (255, rz, rz), ((p0 - 1*x2 + mn1 * 100 * dec*x2), 380*x2, 3*x2, 25*x2))
        if goal == 1000000:
            mark = pygame.draw.rect(screen, (255, wz, wz), (p0 - 140 * rz / 255*x2, 390*x2, 138*x2, 5*x2))
            mark = pygame.draw.rect(screen, (255, wz, wz), (p0 - 100 * mn1*x2 - 1*x2, 380*x2, 3*x2, 25*x2))
            font = pygame.font.Font(None, int(40*x2 - ten * 3*x2))
            text = font.render(str(-1 * mn1 * (10 ** ten)) + kar, True, (255, wz, wz))
            textpos = text.get_rect(centerx=p0 - 100 * mn1*x2, y=420*x2)
            screen.blit(text, textpos)
            for dec in range(0, 115):
                mark = pygame.draw.rect(screen, (255, rz, rz), (((140 * rz / 255*x2) + 10 * dec*x2), 385*x2, 1*x2, 15*x2))
            for dec in range(1, 16):
                mark = pygame.draw.rect(screen, (255, wz, wz), ((p0 - 10 * dec * mn1*x2), 385*x2, 1*x2, 15*x2))
        for dec in range(0, 12):
            if rz == 0:
                dec = 0 - dec
            font = pygame.font.Font(None, int(40*x2 - ten * 3*x2))
            if dec == 0:
                text = font.render(str(dec * (10 ** ten)), True, (255, rz, rz))
            else:
                text = font.render(str(dec * (10 ** ten)) + kar, True, (255, rz, rz))
            textpos = text.get_rect(centerx=p0 + dec * 100*x2, y=420*x2)
            screen.blit(text, textpos)
    else:
        mark = pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1280*x2, 372*x2))
    if ten + mil > 0 and notthird == True:
        for dec in range(0, 115):
            mark = pygame.draw.rect(screen, (255, rz, rz), ((140*x2 + 10 * dec*x2), 385*x2, 1*x2, 15*x2))
    zun = p0 - p0 * wz / 255 + yik * wz / 255*x2
    line = pygame.draw.rect(screen, (0, 0, 255), (zun, 391*x2, (yik*x2 - 140*x2) * rz / 255 + (p0 - zun) * wz / 255, 3*x2))
    pygame.draw.polygon(screen, (0, 255, 0), ([yik*x2 - 8*x2, 350*x2], [yik*x2, 370*x2], [yik*x2 + 8*x2, 350*x2]))
    font = pygame.font.Font(None, int(40*x2))
    text = font.render(str(c), True, (0, 255, 0))
    textpos = text.get_rect(centerx=yik*x2, y=320*x2)
    screen.blit(text, textpos)
    font = pygame.font.Font(None, int(40*x2))
    if int(c) <= goal / 10 and goal != 10:
        text = font.render("Goal: " + str(goal), True, (255, 255, 255))
        pygame.draw.polygon(screen, (255, 255, 255), ([1220*x2, 270*x2], [1220*x2, 290*x2], [1240*x2, 280*x2]))
    elif int(c) >= goal:
        text = font.render("Goal: " + str(goal), True, (0, 255, 0))
    else:
        text = font.render("Goal: " + str(goal), True, (255, 255, 255))
        pygame.draw.polygon(screen, (255, 255, 255), ([1130*x2, 300*x2], [1140*x2, 320*x2], [1150*x2, 300*x2]))
    textpos = text.get_rect(right=1200*x2, centery=280*x2)
    screen.blit(text, textpos)
    if extra != "a":
        font = pygame.font.Font(None, int(100*x2))
        if extra != "Game Over":
            text = font.render((str(extra) + " " + str(a)), True, (0, 255, 255))
        else:
            text = font.render(str(extra), True, (0, 255, 255))
        textpos = text.get_rect(centerx=640*x2, y=200*x2)
        screen.blit(text, textpos)
    nah = int(b)
    pygame.display.flip()
    return ten


def PV_ani(b, extra, notthird, goal, A, tick, nixt, stoppy, a, ten, screen, noxt, naxt, q, total, pre, zu, x, nex, poss, rest, rest1, rest2, rest0, x2):
    c = 0
    if goal == 10:
        if stoppy == True:
            c = b
        else:
            c1 = b - (b - nixt) * (100 - tick) / 100
            c = int(c1)
            if c != c1:
                c = int(c1 * 100) / 100
        ten = Ptsview(c, extra, a, notthird, goal, A, nixt, ten, screen, tick, b, rest, rest1, rest2, x2)
        if tick == 96:
            stoppy = True
    if goal == 1000:
        if stoppy == True:
            c = q
        else:
            c1 = q - (q - noxt) * (100 - tick) / 100
            c = int(c1)
            if c != c1:
                c = int(c1 * 100) / 100
        ten = Ptsview(c, zu, x, notthird, goal, poss, noxt, ten, screen, tick, q, rest, rest1, rest2, x2)
        if tick == 96:
            stoppy = True
    if goal == 1000000:
        if stoppy == True:
            c = total
        else:
            c1 = total - (total - naxt) * (100 - tick) / 100
            c = int(c1)
            if c != c1:
                c = int(c1 * 100) / 100
        ten = Ptsview(c, pre, nex, notthird, goal, rest0, naxt, ten, screen, tick, total, rest, rest1, rest2, x2)
        if tick == 96:
            stoppy = True
    return c, stoppy, ten
