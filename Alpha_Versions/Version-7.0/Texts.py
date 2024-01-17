# -*- coding: iso-8859-2 -*-
#from Numers_launcher import module





import random, time, pygame, sys, datetime

def Texts(T, screen,x2):
    font = pygame.font.Font(T[0], int(T[1]))
    text = font.render(T[2], T[3], (T[4], T[5], T[6]))
    textpos = text.get_rect(centerx = T[7], centery = T[8])
    screen.blit(text, textpos)
    return screen