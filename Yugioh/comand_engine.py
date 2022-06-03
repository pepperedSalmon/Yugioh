command_list= ['draw', 'd',
              'set', 'st',
              'summon','sm',
              'play','p',
              'flip','f',
              'rotate','rt',
              'send_to_grave','s2g'
              'banish','b',
              'Add_tokens_to','at2',
              'take_damage','td',
              'Attack','a',
              'select','s',
              'show hand','sh',
              'next_phase','n',
              'end_turn','et',
              'undo','z'
              'help','h'
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
