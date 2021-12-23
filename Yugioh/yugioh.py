from yugiohGameObjects import YugiohSet
from yugiohGameObjects import YugiohField
from yugiohGameObjects import Ribbon
from yugiohGameObjects import TittleScreen
from access_api import get_online_data
from access_api import YugiohSet2
from art2ascii import *
import os
import sys
os.system("mode con cols=100 lines=60")

set_names=["arena_of_souls", 
          "destiny_masters",
         ]
cards=[]
for set in set_names:
    cards+=YugiohSet(set).cards

mycards=[]

for i in range(30):
    mycards.append(cards[i])

mycards[0].position="face down"
mycards[1].position="face up def"
mycards[2].position="face up"

mycards[22].position="face down"
mycards[23].position="face up def"
mycards[24].position="face up"

mygame=YugiohField()
mygame2=YugiohField()
mygame2.deck.append(mycards[22])
mygame2.m_zone_1.append(mycards[23])
mygame2.m_zone_2.append(mycards[24])
mygame2.st_zone_2.append(mycards[25])

mygame.deck.append(mycards[0])
mygame.m_zone_1.append(mycards[1])
mygame.m_zone_2.append(mycards[2])
mygame.st_zone_2.append(mycards[3])
mygame.hand.append(mycards[4])
mygame.hand.append(mycards[5])
mygame.hand.append(mycards[6])
mygame.hand.append(mycards[7])
mygame.hand.append(mycards[8])

ribbon=Ribbon()
tittle=TittleScreen()
ribbon.life('lose','1000','p1')
ribbon.life('gain','10000','p2')
ribbon.next_phase()
ribbon.next_phase()

tittle.draw()
# Clear the screen by printing several newlines:
print('\n' * 60)
mygame2.draw(view="reverse")
ribbon.draw()
mygame.draw()

#get_online_data()
#cards=YugiohSet2("yugioh.json")
#for card in cards.cards:
#    print(card.name)
#    setup_art(card)
command_list= ['draw', 'd',
              'set', 'st',
              'summon','sm',
              'play','p',
              'flip','f',
              'rotate','rt'
              'send_to_grave','s2g'
              'banish','b',
              'Add_tokens_to','at2'
              'take_damage','td'
              'Attack','a'
              'select','s'
              'show hand','sh'
              'next_phase','n'
              'end_turn','et',
              'undo','z'
              ]



try:
    while True:
        player1CMD=input("CMD: ").split(" ")
        if player1CMD[0] in command_list:
            print(player1CMD[0])
        else:
            print("This is not a valid command ")

except KeyboardInterrupt:
    print('Yugioh by Ivan Lopez')
    sys.exit()  # When Ctrl-C is pressed, end the program.)