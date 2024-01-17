# from Numers_launcher import module

from Texts import Texts

def Changelog(screen, down, x2):
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
               ["alpha-6.6", "---{2024-01-16}---", "fix: most text overlapping after scaling"],
               ["alpha-7.0", "---{2024-01-17}---", "change: FINALLY MADE OOP /w 5pelf A.K.A King Canute of England"],
               ["alpha-7.0", "---{2024-01-17}---", "add: more /w 5pelf A.K.A King Canute of England"]
               ]
    screen.fill([0, 0, 0])
    deve = 1
    alp = 0
    line = 0
    T = [None, 100, "Changelog", True, 255, 255, 255, screen.get_width()/2, screen.get_height()/16]
    screen = Texts(T,screen,x2)
    for dev in range(0, len(Version)):
        sub = Version[len(Version)-dev-1]
        if screen.get_height()/8 + 45 + 60*dev + 30*(line+1) - down*25 > screen.get_height()/8 + 50 and screen.get_height()/8 + 45 + 60*dev + 30*(line+1) - down*25 < screen.get_height() - 10:
            if sub[0] == "--------------------------------------   Early development   --------------------------------------":
                if screen.get_height()/8 + 45 + 60*dev + 30*(line+1) - down*25 < screen.get_height() - 10:
                    T = [None, 50, sub[0], True, 255, 255, 127, screen.get_width()/2, screen.get_height()/8 + 45 + 60*dev + 30*(line+1) - down*25]
                    screen = Texts(T,screen,x2)
            if sub[0] != "--------------------------------------   Early development   --------------------------------------":
                T = [None, 50, sub[0], True, 255, 255, 0, screen.get_width()/2, screen.get_height()/8 + 45 + 60*dev + 30*(line+1) - down*25]
            screen = Texts(T,screen,x2)
        if len(sub) > 0:
            for deve in range(1, len(sub)):
                if deve > 1:
                    line = line + 1
                if screen.get_height()/8 + 40 + 60*dev + 30*(line+2) - down*25 > screen.get_height()/8 + 50 and screen.get_height()/8 + 40 + 60*dev + 30*(line+2) - down*25 < screen.get_height() - 10:
                    T = [None, 25, sub[deve], True, 127, 255, 0, screen.get_width()/2, screen.get_height()/8 + 40 + 60*dev + 30*(line+2) - down*25]
                    if deve == 1:
                        T = [None, 25, sub[deve], True, 191, 255, 63, screen.get_width()/2, screen.get_height()/8 + 40 + 60*dev + 30*(line+2) - down*25]
                    screen = Texts(T,screen,x2)
        if sub[0] == "--------------------------------------   Early development   --------------------------------------" and screen.get_height()/8 + 45 + 60*dev + 30*(line+1) - down*25 > screen.get_height()/8 + 50:
            T = [None, 75, "Alpha development", True, 255, 255, 127, screen.get_width()/2, screen.get_height()/8 + 20]
            alp = 1
            screen = Texts(T,screen,x2)
    if screen.get_height()/8 + 25 + 60*dev + 30*(line+1) - down*25 > screen.get_height()/8 and alp == 0:
        T = [None, 75, "Early development", True, 255, 255, 127, screen.get_width()/2, screen.get_height()/8 + 20]
        screen = Texts(T,screen,x2)
    return screen, down