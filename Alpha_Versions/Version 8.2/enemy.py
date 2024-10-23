# -*- coding: iso-8859-2 -*-
#
# ----   Reminders   ----
#

import random

class Card:

    def drawc(self):
        self.draw = random.choice(self.Drawpile)
        self.Drawpile.remove(self.draw)
        #self.Droppile.append(self.draw)
    def shuffle(self):
        for j in range(0, len(self.Drawpile)):
           self.drawc()
        self.Drawpile = self.Droppile
    def add(self):
        print (self.cards)
        self.addi = int(input("new card: "))
        if self.addi in self.cards:
            self.Drawpile.append(self.addi)
            self.cards.remove(self.addi)
    def addop(self):
        #print (self.cards)
        self.addi = random.choice(self.cards)
        if self.addi in self.cards:
            self.Drawpile.append(self.addi)
            self.cards.remove(self.addi)
    def play(self):
        rturn = False
        while rturn == False:
            self.place = int(input("play card: "))
            if self.place in hand:
                self.Droppile.append(self.place)
                hand.remove(self.place)
                print(hand)
                rturn = True
    def playop(self):
        self.place = random.choice(hand2)
        self.Droppile.append(self.place)
        hand2.remove(self.place)
        #print(hand2)
        
def vsgame():
    global hand, hand2
    Collection = [1,2,3,4,5,6,7,8,9,0]
    Deck = Collection
    Deck2 = [1,2,3,4,5,6,7,8,9,0]
    Droppile = []
    Droppile2 = []
    Drawpile = []
    Drawpile2 = []
    hand = []
    hand2 = []

    Drawpi = Card()
    Drawpi.Droppile = Droppile
    Drawpi.Drawpile = Drawpile
    Drawpi.draw = ""
    Drawpi.place = ""
    Drawpi.addi = ""
    Drawpi.cards = Deck

    Drawpi2 = Card()
    Drawpi2.Droppile = Droppile2
    Drawpi2.Drawpile = Drawpile2
    Drawpi2.draw = ""
    Drawpi2.place = ""
    Drawpi2.addi = ""
    Drawpi2.cards = Deck2

    decklengh = int(input("Maximum Number of Cards in Deck? > "))
    handlengh = int(input("Maximum Number of Cards in Hand? > "))
    gamelengh = int(input("maximum Number of Cards in Play? > "))
    if decklengh > len(Collection):
        decklengh = len(Collection)
        print ("Maximum Card Limit reached... set to " + str(decklengh))

    for i in range(0, decklengh+1):
        while len(Drawpi.Drawpile) < i:
            Drawpi.add()

    for i in range(0, decklengh+1):
        while len(Drawpi2.Drawpile) < i:
            Drawpi2.addop()
        
    for i in range(0, handlengh):
        Drawpi.drawc()
        hand.append(Drawpi.draw)
        print ("Drew a " + str(Drawpi.draw))

    for i in range(0, handlengh):
        Drawpi2.drawc()
        hand2.append(Drawpi2.draw)
        #print ("Drew a " + str(Drawpi2.draw))

    #print ("The enemy hand: " + str(sorted(hand2)))

    for i in range(0, gamelengh):
        print ("The own hand: " + str(sorted(hand)))
        Drawpi.play()
        Drawpi2.playop()
        print ("You: " + str(Drawpi.place) + " vs " + str(Drawpi2.place))
        if Drawpi.place > Drawpi2.place:
            print ("You won a round!")
        Drawpi.drawc()
        hand.append(Drawpi.draw)
        print ("Drew a " + str(Drawpi.draw))
        Drawpi2.drawc()
        hand2.append(Drawpi.draw)

    print (Drawpi.Drawpile)
    Drawpi.shuffle()
    print (Drawpi.Drawpile)
    Drawpi2.shuffle()
    #print (Drawpi2.Drawpile)
