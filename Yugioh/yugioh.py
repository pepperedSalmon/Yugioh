from yugiohGameObjects import YugiohSet
from yugiohGameObjects import YugiohField
from yugiohGameObjects import Ribbon
from yugiohGameObjects import TittleScreen
from yugiohGameObjects import Player
from access_api import get_online_data
from access_api import YugiohSet2
from art2ascii import *
from yugiohGameObjects import Game
import os
import sys

os.system("mode con cols=100 lines=60")

set_names=["arena_of_souls", 
          "destiny_masters"
         ]
cards=[]
for set in set_names:
    cards+=YugiohSet(set).cards

mycards=[]

for i in range(30):
    mycards.append(cards[i])
player1=Player("Bob",mycards)
player2=Player("Jack",mycards)
game1=Game(player1,player2)

game1.run()

#mycards[0].position="face down"
#mycards[1].position="face up def"
#mycards[2].position="face up"

#mycards[22].position="face down"
#mycards[23].position="face up def"
#mycards[24].position="face up"

#mygame=YugiohField()
#mygame2=YugiohField()
#mygame2.deck.append(mycards[22])
#mygame2.m_zone_1.append(mycards[23])
#mygame2.m_zone_2.append(mycards[24])
#mygame2.st_zone_2.append(mycards[25])

#mygame.deck.append(mycards[0])
#mygame.m_zone_1.append(mycards[1])
#mygame.m_zone_2.append(mycards[2])
#mygame.st_zone_2.append(mycards[3])
#mygame.hand.append(mycards[4])
#mygame.hand.append(mycards[5])
#mygame.hand.append(mycards[6])
#mygame.hand.append(mycards[7])
#mygame.hand.append(mycards[8])

#ribbon=Ribbon()
#tittle=TittleScreen()
#ribbon.life('lose','1000','p1')
#ribbon.life('gain','10000','p2')
#ribbon.next_phase()
#ribbon.next_phase()

#tittle.display()
## Clear the screen by printing several newlines:
#print('\n' * 60)
#mygame2.display(view="reverse")
#ribbon.display()
#mygame.display()

#get_online_data()
#cards=YugiohSet2("yugioh.json")
#for card in cards.cards:
#    print(card.name)
#    setup_art(card)
#commandList= [['draw', 'd', 1],
#              ['set', 'st', 2],
#              ['summon','sm',2],
#              ['play','p',2],
#              ['flip','f', 1],
#              ['rotate','rt',2],
#              ['send_to_grave','s2g',1],
#              ['banish','b',1],
#              ['add_tokens_to','at2',1],
#              ['take_damage','td',1],
#              ['attack','a',2],
#              ['select','s', 1],
#              ['show hand','sh',0],
#              ['next_phase','n',0],
#              ['end_turn','et',0],
#              ['undo','z',0],
#              ['help','h',0]
#              ]
#validCmds=[]
#for command in commandList:
#    longCmd,shortCmd,_=command
#    validCmds.append(longCmd)
#    validCmds.append(shortCmd)

#try:
#    while True:
#        player1CMD,*p1Awrgs=input("CMD: ").split(" ")
#        if player1CMD in validCmds:
#            print(player1CMD)
#        else:
#            print("This is not a valid command ")

#except KeyboardInterrupt:
#    print('Yugioh by Ivan Lopez')
#    sys.exit()  # When Ctrl-C is pressed, end the program.)