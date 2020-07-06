from yugiohGameObjects import YugiohSet
from yugiohGameObjects import YugiohField

set_names=["arena_of_souls", 
          "destiny_masters",
         ]
cards=[]
for set in set_names:
    cards+=YugiohSet(set).cards

mycards=[]

for i in range(10):
    mycards.append(cards[i])

mycards[0].position="face down"
mycards[1].position="face up def"
mycards[2].position="face up"

mygame=YugiohField()
mygame.deck.append(mycards[0])
mygame.m_zone_1.append(mycards[1])
mygame.m_zone_2.append(mycards[2])
mygame.st_zone_2.append(mycards[3])

mygame.draw()