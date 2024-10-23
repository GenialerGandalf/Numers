from Texts import Texts
from rend import *

def Achtexts(Sach):
    Sachtexts = ["Lost with 0 pts in Lv.1",
                 "Lost with 9 pts in Lv.1",
                 "Finished Lv.1 with 10 pts",
                 "Game Over with 69 pts",
                 "Game Over with 420 pts",
                 "Finished Lv.1 with 8100 pts",
                 "Lost with 999 pts in Lv.2",
                 "Finished Lv.2 with 1000 pts",
                 "Game Over with 65536 pts",
                 "Game Over with 69420 pts",
                 "Finished Lv.2 with the perfect score!"
                 ]
    Sach = Sachtexts[Sach]
    return Sach

def Achieves(Ach, screen, x2, achi):
    screen.fill([0, 0, 0])
    if Ach != []:
        for hidder in range(0, len(Ach)):
            for hidden in range(hidder, Ach[len(Ach)-1]+1):
                if hidden == Ach[hidder]:
                    Sach = Ach[hidder]
                    Sach = Achtexts(Sach)
                    T = [None, 25*x2, "---[" + Sach + "]---", True, 255, 127, 255, screen.get_width()/2, screen.get_height()/32*(6+hidden)]
                    screen = Texts(T,screen,x2)
        Sach = Ach   
    if Ach == []:
        Sach = "Nothing here yet, start hunting already!"
    T = [None, 100*x2, "Achievements", True, 255, 127, 255, screen.get_width()/2, screen.get_height()/16]
    screen = Texts(T,screen,x2)
    T = [None, 50*x2, str(Sach), True, 255, 127, 127, screen.get_width()/2, screen.get_height()/8]
    screen = Texts(T,screen,x2)
    go = ""
    go = Return(go)
    if go == "esc":
        achi = False
    return screen, achi, go
