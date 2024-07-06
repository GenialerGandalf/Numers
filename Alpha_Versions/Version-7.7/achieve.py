from Texts import Texts
from rend import *

def Achieves(Ach, screen, x2, achi):
    if Ach != []:
        Sach = Ach.sort()
        print (Sach)
    screen.fill([0, 0, 0])
    T = [None, 100*x2, "Achievements", True, 255, 127, 255, screen.get_width()/2, screen.get_height()/16]
    screen = Texts(T,screen,x2)
    go = ""
    go = Return(go)
    if go == "esc":
        achi = False
    return screen, achi, go
