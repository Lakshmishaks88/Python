def choose_player():
    choice = True
    while choice not in ['O','X']:
        choice = input('Player 1 Choose O or X').upper()
        if choice not in ['O','X']:
            print('Invalid input, please enter X or O')
    if choice == "X":
        return ('X','O')
    else:
        return ('O','X')
