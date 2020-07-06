from yugiohBaseObjects import MonsterCard
from yugiohBaseObjects import SpellTrapCard

def name_format(card_name,LINE_WIDTH):
    card_name=str(card_name)
    b1=""
    b2=""
    b3=""
    if len(card_name)<LINE_WIDTH:
        for i in range(LINE_WIDTH-len(card_name)):
                b1+=" "
        for i in range(LINE_WIDTH):
            b2+=" "
        f1=card_name+b1
        f2=b2
    elif len(card_name)<2*LINE_WIDTH:
         for i in range(2*LINE_WIDTH-len(card_name)):
                b2+=" "
         f1=card_name[0:LINE_WIDTH]
         f2=card_name[LINE_WIDTH:len(card_name)]+b2
    else:
        f1=card_name[0:LINE_WIDTH]
        f2=card_name[LINE_WIDTH:LINE_WIDTH*2]
    return [f1,f2]

def level_format(card_rank,LINE_WIDTH=10):
    try:
        i_rank=int(card_rank)
    except ValueError:
        i_rank=LINE_WIDTH+1     
        
    b1=""
    r1=""
    if i_rank<=LINE_WIDTH:
        for i in range(LINE_WIDTH-i_rank):
            b1+=" "
        for i in range(i_rank): 
            r1+="*"
        f_rank=b1+r1
        return f_rank
    else:
        for i in range(LINE_WIDTH):
            b1+=" "
        return b1

def card_2_str(card=0):
    if card==0: 
        fd00="   .............   "
        fd01="  :             :  "           
        fd02="  :             :  "
        fd03="  :             :  "
        fd04="  :             :  "
        fd05="  :             :  "
        fd06="  :             :  "
        fd07="  :             :  "
        fd08="  :             :  "
        fd09="  :             :  "
        fd10="  :.............:  "
        fd=[fd00,fd01,fd02,fd03,fd04,fd05,fd06,fd07,fd08,fd09, fd10]
        return fd
    else:
        fname=name_format(card.name,16)
        if card.position.lower()=="set":
             fd00="   .............   "
             fd01="  :             :  "           
             fd02="  :             :  "
             fd03="  :             :  "
             fd04="  :             :  "
             fd05=" _:_____________:_ "
             fd06="|    _________    |"
             fd07="|   /         \   |"
             fd08="|  |           |  |"
             fd09="|   \_________/   |"
             fd10="|_________________|"
             fd=[fd00,fd01,fd02,fd03,fd04,fd05,fd06,fd07,fd08,fd09, fd10]
             return fd
        elif card.position.lower()=="face down":
             fd00="  ________________ " 
             fd01=" |      ____      |"  
             fd02=" |     /    \     |"
             fd03=" |    |      |    |"
             fd04=" |    |      |    |"
             fd05=" |    |      |    |"
             fd06=" |    |      |    |"
             fd07=" |    |      |    |"
             fd08=" |    |      |    |"
             fd09=" |     \____/     |"
             fd10=" |________________|" 
             fd=[fd00,fd01,fd02,fd03,fd04,fd05,fd06,fd07,fd08,fd09, fd10]
             return fd
        elif card.position.lower()=="face up": 
            if card.frame.lower()=="trap card":  
                mz00="  _________________ "
                mz01=f" |{fname[0]}|"
                mz02=f" |{fname[1]}|"
                mz03=" |   _________Trap|"
                mz04=" |  |          |  |"
                mz05=" |  |          |  |"
                mz06=" |  |          |  |"
                mz07=" |  |__________|  |"
                mz08=" | .............  |"
                mz09=" | :...........:  |"
                mz10=" |________________|"
                if mz02==" |                |":
                    mz02=" |            Trap|"
                    mz03=" |   __________   |"
                mz=[mz00,mz01,mz02,mz03,mz04,mz05,mz06,mz07,mz08,mz09,mz10]
                return mz
            elif card.frame.lower()=="spell card":            
                mz00="  ________________ "
                mz01=f" |{fname[0]}|"
                mz02=f" |{fname[1]}|"
                mz03=" |   ________Spell|"
                mz04=" |  |          |  |"
                mz05=" |  |          |  |"
                mz06=" |  |          |  |"
                mz07=" |  |__________|  |"
                mz08=" | .............  |"
                mz09=" | :...........:  |"
                mz10=" |________________|"
                if mz02==" |                |":
                    mz02=" |           Spell|"
                    mz03=" |   __________   |"
                mz=[mz00,mz01,mz02,mz03,mz04,mz05,mz06,mz07,mz08,mz09,mz10]
                return mz
            elif card.s_frame.lower()=="monster":
                f_atk=name_format(card._atk,4)
                f_def=name_format(card._def,4)
                f_level=level_format(card.level)
                mz00="  ________________ "
                mz01=f" |{fname[0]}|"
                mz02=f" |{fname[1]}|"
                mz03=f" |    {f_level}  |"
                mz04=" |   __________   |"
                mz05=" |  |          |  |"
                mz06=" |  |          |  |"
                mz07=" |  |__________|  |"
                mz08=f" | ATK {f_atk[0]}       |"
                mz09=f" | DEF {f_def[0]}       |"
                mz10=" |________________|"
                if mz02==" |                |":
                    mz02=mz03
                    mz03=mz04
                    mz04=mz05
                mz=[mz00,mz01,mz02,mz03,mz04,mz05,mz06,mz07,mz08,mz09,mz10]
                return mz
        elif card.position.lower()=="face up def":
                f_atk=name_format(card._atk,4)
                f_def=name_format(card._def,4)
                f_level=level_format(card.level)
                mz00="  ...............  "  
                mz01=f"{fname[0]}:  "         
                mz02=f"  :   {f_level}:  "
                mz03=f"  :   ATK: {f_atk[0]} :  "
                mz04=f"  :   DEF: {f_def[0]} :  "
                mz05=" _:_____________:_ "
                mz06="|  ______   ..... |"
                mz07="| |      |  :   : |"
                mz08="| |      |  :   : |"
                mz09="| |______|  :...: |"
                mz10="|_________________|"
                mz=[mz00,mz01,mz02,mz03,mz04,mz05,mz06,mz07,mz08,mz09,mz10]
                return mz

class YugiohField:
    def __init__(self):
        self.grave=[]
        self.deck=[]
        self.m_zone_1=[]
        self.m_zone_2=[]
        self.m_zone_3=[]
        self.st_zone_1=[]
        self.st_zone_2=[]
        self.st_zone_3=[]
        self.fieldzone=[]
        self.fusion_deck=[]
        self.banish=[]
        self.skills=[]
    def draw(self):
        zones=[self.fieldzone,
                self.m_zone_3,
                self.m_zone_2,
                self.m_zone_1,
                self.grave,
                self.fusion_deck,
                self.st_zone_3,
                self.st_zone_2,
                self.st_zone_1,
                self.deck]
        im=[]
        for zone in zones:
            if len(zone)==0:
                im.append(card_2_str())
            else:
                im.append(card_2_str(zone[-1]))
        print(im[0][0]+im[1][0]+im[2][0]+im[3][0]+im[4][0])
        print(im[0][1]+im[1][1]+im[2][1]+im[3][1]+im[4][1])
        print(im[0][2]+im[1][2]+im[2][2]+im[3][2]+im[4][2])
        print(im[0][3]+im[1][3]+im[2][3]+im[3][3]+im[4][3])
        print(im[0][4]+im[1][4]+im[2][4]+im[3][4]+im[4][4])
        print(im[0][5]+im[1][5]+im[2][5]+im[3][5]+im[4][5])
        print(im[0][6]+im[1][6]+im[2][6]+im[3][6]+im[4][6])
        print(im[0][7]+im[1][7]+im[2][7]+im[3][7]+im[4][7])
        print(im[0][8]+im[1][8]+im[2][8]+im[3][8]+im[4][8])
        print(im[0][9]+im[1][9]+im[2][9]+im[3][9]+im[4][9])
        print(im[0][10]+im[1][10]+im[2][10]+im[3][10]+im[4][10])
        print("| FZ: Field Zone  ||M3: Monster Zone ||M2: Monster Zone ||M1: Monster Zone || GY: Grave Yard  |")
        
        print(im[5][0]+im[6][0]+im[7][0]+im[8][0]+im[9][0])
        print(im[5][1]+im[6][1]+im[7][1]+im[8][1]+im[9][1])
        print(im[5][2]+im[6][2]+im[7][2]+im[8][2]+im[9][2])
        print(im[5][3]+im[6][3]+im[7][3]+im[8][3]+im[9][3])
        print(im[5][4]+im[6][4]+im[7][4]+im[8][4]+im[9][4])
        print(im[5][5]+im[6][5]+im[7][5]+im[8][5]+im[9][5])
        print(im[5][6]+im[6][6]+im[7][6]+im[8][6]+im[9][6])
        print(im[5][7]+im[6][7]+im[7][7]+im[8][7]+im[9][7])
        print(im[5][8]+im[6][8]+im[7][8]+im[8][8]+im[9][8])
        print(im[5][9]+im[6][9]+im[7][9]+im[8][9]+im[9][9])
        print(im[5][10]+im[6][10]+im[7][10]+im[8][10]+im[9][10])
        print("| FD: Fusion Deck || ST3: Spell/Trap || ST2: Spell/Trap || ST1: Spell/Trap ||     D: Deck     |")
      
class Deck:
    def __init__(self, cards):
        self.cards=cards
        
class YugiohSet:
    '''Extracts information from cvs file to create yugioh cards objects'''
    def __init__(self,name):
        self.name=name
        self.cards=[]
        self.build()
        self.len=len(self.cards)

    def build(self):
        filename = f"{self.name}.csv"
        try:
            with open(filename, encoding='utf-8') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Sorry, the file {filename} does not exist.")
        else:
            # create a yugioh card object per line.
            for line in lines:
                fields = line.split(",")
                
                if (fields[11].lower()).rstrip()=='monster':
                    
                    if fields[5]!="?":
                        try:
                            fields[5]=int(fields[5])
                        except ValueError:
                            pass
                    if fields[6]!="?":
                        try:
                            fields[6]!=int(fields[6])
                        except ValueError:
                            pass
                    self.cards.append(MonsterCard(name=fields[0],
                                        frame=fields[1],
                                        rarity=fields[8],
                                        card_set=fields[9],
                                        text=fields[10],
                                        atribute=fields[2],
                                        monster_type=fields[3],
                                        level=fields[4],
                                        _atk=fields[5],
                                        _def=fields[6],
                                        s_frame=fields[11]))
                elif (fields[11].lower()).rstrip()=="spell/trap":
                        self.cards.append(SpellTrapCard(name=fields[0],
                                            frame=fields[1],
                                            rarity=fields[8],
                                            card_set=fields[9],
                                            text=fields[10],
                                            card_icon=fields[7],
                                            s_frame=fields[11]))





         