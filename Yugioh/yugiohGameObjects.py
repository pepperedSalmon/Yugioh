from yugiohBaseObjects import MonsterCard
from yugiohBaseObjects import SpellTrapCard

def empty_zone():   
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
    pass

class Ribbon:
    def __init__(self):
        self.p1_life='8000'
        self.p2_life='8000'
        self.phases=["D","S","M1","B","E"]
        self.p_index=0
        self.phase_text='|D|    S     M1    B    E '
        self.phase=self.phases[self.p_index%len(self.phases)]
        self.turns=["One","Two"]
        self.player_turn= "One"

    def next_phase(self):
        self.p_index+=1
        self.phase=self.phases[self.p_index%len(self.phases)]
        self.player_turn=self.turns[(self.p_index//len(self.phases))%len(self.turns)]

        if self.phase=='D':
            self.phase_text='|D|    S     M1    B    E '
        elif self.phase=='S':
            self.phase_text=' D    |S|    M1    B    E '
        elif self.phase=="M1":
            self.phase_text=' D     S    |M1|   B    E '
        elif self.phase=="B":
            self.phase_text=' D     S     M1   |B|   E '        
        elif self.phase=="E":
            self.phase_text=' D     S     M1    B   |E|'

    def life(self,do="lose",amount='1000',player='p1'):
        '''update players life points'''
        # select player 
        if player=='p1':
            int_life=int(self.p1_life.strip())
        elif player=="p2":
            int_life=int(self.p2_life.strip())
        # gain or lose amount 
        if do=="lose":
            int_life-=int(amount)
            int_life=max(0,int_life) # make sure life does not go negative
        elif do=="gain":
            int_life+=int(amount)
        # update player
        if player=='p1':
            self.p1_life=self.word_format(int_life,5)
        elif player=="p2":
            self.p2_life=self.word_format(int_life,5)

    def display(self):
       # print('================================================================================================')
        print(f"====================================== Player's {self.player_turn} Turn =====================================")
        print(f'   P1:{self.p1_life}                      {self.phase_text}                          P2:{self.p2_life}   ')
       # print('================================================================================================')

    def word_format(self,word,line_width):
        card_name = str(word)
        blank = ""
        if len(card_name) < line_width:
            for i in range(line_width - len(card_name)):
                    blank+=" "
            fword = card_name + blank
        else:
            fword = card_name[0:line_width]
        return fword
        
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
        self.hand=[]
    def display(self,view='normal'):
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
                im.append(empty_zone())
            else:
                im.append(zone[-1].str_img())
# create display strings for empty dotted hand place holders for  4 minus number of cards in hand.
        h_im=[]
        for i in range(max(0,4- len(self.hand))):
            h_im.append(empty_zone())
# create display strings for cards in hand.
        for number, card in enumerate(self.hand):
            card.position="face up"
            h_im.insert(number,card.str_img())

        hand=['','','','','','','','','','','']
        for x in range(len(h_im)):
            for y in range(11):
                hand[y]+=h_im[x][y]

        if view== 'normal':
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
            #print()
            #print("------------------------------============ Hand =========-----------------------------------------")
            print(hand[0])
            print(hand[1])
            print(hand[2])
            print(hand[7])
            print(hand[8])
            print(hand[9])
            print(hand[10])
            for number,cards in enumerate(self.hand):
                print("| -------  ------ |",end='')
            





        else:
            print("|     D: Deck     || ST1: Spell/Trap || ST2: Spell/Trap || ST3: Spell/Trap || FD: Fusion Deck |")
            print(im[9][0]+im[8][0]+im[7][0]+im[6][0]+im[5][0])
            print(im[9][1]+im[8][1]+im[7][1]+im[6][1]+im[5][1])
            print(im[9][2]+im[8][2]+im[7][2]+im[6][2]+im[5][2])
            print(im[9][3]+im[8][3]+im[7][3]+im[6][3]+im[5][3])
            print(im[9][4]+im[8][4]+im[7][4]+im[6][4]+im[5][4])
            print(im[9][5]+im[8][5]+im[7][5]+im[6][5]+im[5][5])
            print(im[9][6]+im[8][6]+im[7][6]+im[6][6]+im[5][6])
            print(im[9][7]+im[8][7]+im[7][7]+im[6][7]+im[5][7])
            print(im[9][8]+im[8][8]+im[7][8]+im[6][8]+im[5][8])
            print(im[9][9]+im[8][9]+im[7][9]+im[6][9]+im[5][9])
            print(im[9][10]+im[8][10]+im[7][10]+im[6][10]+im[5][10])
            
            print("| GY: Grave Yard  ||M1: Monster Zone ||M2: Monster Zone ||M3: Monster Zone || FZ: Field Zone  |")
            print(im[4][0]+im[3][0]+im[2][0]+im[1][0]+im[0][0])
            print(im[4][1]+im[3][1]+im[2][1]+im[1][1]+im[0][1])
            print(im[4][2]+im[3][2]+im[2][2]+im[1][2]+im[0][2])
            print(im[4][3]+im[3][3]+im[2][3]+im[1][3]+im[0][3])
            print(im[4][4]+im[3][4]+im[2][4]+im[1][4]+im[0][4])
            print(im[4][5]+im[3][5]+im[2][5]+im[1][5]+im[0][5])
            print(im[4][6]+im[3][6]+im[2][6]+im[1][6]+im[0][6])
            print(im[4][7]+im[3][7]+im[2][7]+im[1][7]+im[0][7])
            print(im[4][8]+im[3][8]+im[2][8]+im[1][8]+im[0][8])
            print(im[4][9]+im[3][9]+im[2][9]+im[1][9]+im[0][9])
            print(im[4][10]+im[3][10]+im[2][10]+im[1][10]+im[0][10])
            
class TittleScreen:
    def __init__(self):
        t0=' YYYYYYY       YYYYYYY                                           GGGGGGGGGGGGG  iiii                        OOOOOOOOO     hhhhhhh                   !!! '
        t1=' Y:::::Y       Y:::::Y                                        GGG::::::::::::G i::::i                     OO:::::::::OO   h:::::h                  !!:!!'
        t2=' Y:::::Y       Y:::::Y                                      GG:::::::::::::::G  iiii                    OO:::::::::::::OO h:::::h                  !:::!'
        t3=' Y::::::Y     Y::::::Y                                     G:::::GGGGGGGG::::G                         O:::::::OOO:::::::Oh:::::h                  !:::!'
        t4=' YYY:::::Y   Y:::::YYYuuuuuu    uuuuuu                    G:::::G       GGGGGGiiiiiii                  O::::::O   O::::::O h::::h hhhhh            !:::!'
        t5='    Y:::::Y Y:::::Y   u::::u    u::::u                   G:::::G              i:::::i                  O:::::O     O:::::O h::::hh:::::hhh         !:::!'
        t6='     Y:::::Y:::::Y    u::::u    u::::u                   G:::::G               i::::i                  O:::::O     O:::::O h::::::::::::::hh       !:::!'
        t7='      Y:::::::::Y     u::::u    u::::u   --------------- G:::::G    GGGGGGGGGG i::::i  --------------- O:::::O     O:::::O h:::::::hhh::::::h      !:::!'
        t8='       Y:::::::Y      u::::u    u::::u   -:::::::::::::- G:::::G    G::::::::G i::::i  -:::::::::::::- O:::::O     O:::::O h::::::h   h::::::h     !:::!'
        t9='        Y:::::Y       u::::u    u::::u   --------------- G:::::G    GGGGG::::G i::::i  --------------- O:::::O     O:::::O h:::::h     h:::::h     !:::!'
        ta='        Y:::::Y       u::::u    u::::u                   G:::::G        G::::G i::::i                  O:::::O     O:::::O h:::::h     h:::::h     !!:!!'
        tb='        Y:::::Y       u:::::uuuu:::::u                    G:::::G       G::::G i::::i                  O::::::O   O::::::O h:::::h     h:::::h      !!! '
        tc='        Y:::::Y       u:::::::::::::::uu                   G:::::GGGGGGGG::::Gi::::::i                 O:::::::OOO:::::::O h:::::h     h:::::h          '
        td='     YYYY:::::YYYY     u:::::::::::::::u                    GG:::::::::::::::Gi::::::i                  OO:::::::::::::OO  h:::::h     h:::::h      !!! '
        te='     Y:::::::::::Y      uu::::::::uu:::u                      GGG::::::GGG:::Gi::::::i                    OO:::::::::OO    h:::::h     h:::::h     !!:!!'
        tf='     YYYYYYYYYYYYY        uuuuuuuu  uuuu                         GGGGGG   GGGGiiiiiiii                      OOOOOOOOO      hhhhhhh     hhhhhhh      !!! '
        self.tittle=[t0,t1,t2,t3,t4,t5,t6,t7,t8,t9,ta,tb,tc,td,te,tf]
    def display(self):
        for line in self.tittle:
            print(line)
        print()
        print("                                                                Speed Duel ")
        print("                                                              =============")
        print("                                                              1) Beta      ")
        print("                                                              2) Edit Deck ")
        print("                                                              3) Enter Lobby ")
        print("                                                              3) Expectate ")
                  
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

class Player:
    def __init__(self,name,deck):
        self.deck=deck
        self.name=name

class Game:
    def __init__(self,player1,player2):
        self.p1_field=YugiohField()
        self.p2_field=YugiohField()
        self.ribbon=Ribbon()
        self.p1_field.deck=player1.deck
        self.p2_field.deck=player2.deck
        self.command_list= ['draw', 'd',
                           'set', 'st',
                           'summon','sm',
                           'play','p',
                           'flip','f',
                           'rotate','rt',
                           'send_to_grave','s2g',
                           'banish','b',
                           'add_tokens_to','at2',
                           'take_damage','td',
                           'attack','a',
                           'select','s',
                           'show hand','sh',
                           'next_phase','n',
                           'end_turn','end',
                           'undo','z']
        self.zones_names=['fz', 'field_zone', 
                         'm3', 'monster_zone_3' , 
                         'm2', 'monster_zone_2', 
                         'm1', 'monster_zone_1', 
                         'gy', 'grave_yard',
                         'd','deck', 
                         'st1', 'spell_zone_1','trap_zone_1',
                         'st2', 'spell_zone_2','trap_zone_2',
                         'st3', 'spell_zone_3','trap_zone_3',
                         'fd', 'fusion_Deck']
        self.errorMsg=''
        self.message=''
    def run(self):             
        while int(self.ribbon.p1_life)>0 and int(self.ribbon.p2_life)>0:
            self._display()
            self._p1_turn()
 
        self._display()

    def _display(self):
        self.p2_field.display(view="reverse")
        self.ribbon.display()
        self.p1_field.display()
        print(self.errorMsg)
        print(self.message)
        

    def _p1_turn(self):
        p1Cmd,*p1Awrg=self._askForAction()
        self._p1_action(p1Cmd,p1Awrg)
    def _p1_action(self,cmd,cmdAwrgs):
        if cmd == 'error':
            self.errorMsg=cmdAwrgs[0]

        if cmd=='draw' or cmd=='d':
            self.errorMsg=''
            if cmdAwrgs==[]:
                self.p1_field.hand.append(self.p1_field.deck.pop())
            elif cmdAwrgs[0].isnumeric():
                for i in range(int(cmdAwrgs[0])):
                    self.p1_field.hand.append(self.p1_field.deck.pop())

    def _askForAction(self):
        while True:
            player1CMD=input("CMD: ").lower().split(" ") # returns a list of string, with the first beign the cmd followed by awrguments
            if player1CMD[0] in self.command_list:
                if player1CMD[0] in ['draw', 'd']:
                    if len(player1CMD)>2:
                        player1CMD[0]="error"
                        player1CMD[1]="too many awrgument"
                        return(player1CMD)
                    if len(player1CMD)==1:
                        return(player1CMD)
                    if len(player1CMD)==2:
                        if not (player1CMD[1].isnumeric):
                            player1CMD[0]="error"
                            player1CMD[1]="awrgument is not numeric"
                            return(player1CMD)
                        if (player1CMD[1].isnumeric):
                            try:
                                if int(player1CMD[1])>len(self.p1_field.deck):
                                    player1CMD[0]="error"
                                    player1CMD[1]="awrgument exceeds deck size"
                                    return(player1CMD)
                            except ValueError:
                                    player1CMD[0]="error"
                                    player1CMD[1]="awrgument is not numeric"
                                    return(player1CMD)
                        return(player1CMD)

                if player1CMD[0] in ['set', 'st']:
                    if not len(player1CMD)==3:
                        player1CMD[:]=["error","awrgument must equal two"]
                        return(player1CMD)
                    if not player1CMD[1].isnumeric:
                        player1CMD[0]="error"
                        player1CMD[1]="awrgument one is not numeric"
                        return(player1CMD)
                    if not (player1CMD[2] in self.zones_names):
                        player1CMD[0]="error"
                        player1CMD[1]="awrgument two is not a field zone"
                        return(player1CMD)
                    try:
                        if int(player1CMD[1]) > len(self.p1_field.hand):
                            player1CMD[0]="error"
                            player1CMD[1]="awrgument one exceeds hand size"
                            return(player1CMD)
                    except ValueError:
                        player1CMD[:]=["error","awrgument is not numeric"]
                        return(player1CMD)

                    return(player1CMD)

                if player1CMD[0] in['summon','sm']:
                    pass
                if player1CMD[0] in ['play','p']:
                    pass
                if player1CMD[0] in ['flip','f']:
                    pass
                if player1CMD[0] in ['rotate','rt']:
                    pass
                if player1CMD[0] in ['send_to_grave','s2g']:
                    pass
                if player1CMD[0] in ['banish','b']:
                    pass
                if player1CMD[0] in ['add_tokens_to','at2']:
                    pass
                if player1CMD[0] in ['take_damage','td']:
                    pass
                if player1CMD[0] in ['attack','a']:
                    pass
                if player1CMD[0] in ['select','s']:
                    pass
                if player1CMD[0] in ['show hand','sh']:
                    pass
                if player1CMD[0] in ['next_phase','n']:
                    pass
                if player1CMD[0] in ['end_turn','end']:
                    pass
                if player1CMD[0] in ['undo','z']:
                    pass
            else:
                player1CMD=["error","invalid command"]
                return player1CMD

            
         