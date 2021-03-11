def automat_player():
    choice = True
    while choice not in ['Y','N']:
        choice = input('Do you want computer player as player 2. Enter Y or N').upper()
        if choice not in ['Y','N']:
            print('Invalid input, please enter Y or N')
    if choice == 'Y':
        choice = True
    else:
        choice = False
    return choice
