from statistics import mean

class YugiohCard:
    '''This object describes a Yugioh card at a high level'''
    def __init__(self,name,frame,rarity,card_set,text="N/A",position="face down",s_frame="monster"):
        self.name=name
        self.frame=frame
        self.rarity=rarity
        self.card_set=card_set
        self.text=text
        self.position=position
        self.s_frame=s_frame

    def reveal(self):
        print(self.name)

class MonsterCard(YugiohCard):
    '''This object is a child of Yugioh cards'''
    ''' It discribes Monster cards  '''
    def __init__(self,name,frame,rarity,card_set,
                 text,atribute,monster_type,level,
                 _atk,_def,position="face down",s_frame="monster"):
        super().__init__(name,frame,rarity,card_set,text,position="face down",s_frame="monster")
        self.atribute=atribute
        self.moster_type=monster_type
        self.level=level
        self._atk=_atk
        self._def=_def
                      
class SpellTrapCard(YugiohCard):
    def __init__(self,name,frame,rarity,card_set,text,card_icon,position="face down",s_frame="monster"):
        super().__init__(name,frame,rarity,card_set,text,position="face down",s_frame="monster")
        self.card_icon=card_icon



