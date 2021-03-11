def game_continue():
    choice = True
    while choice not in ['Y','N']:
        choice = input('Press Y to continue and N to stop').upper()
        if choice not in ['Y','N']:
            print('Invalid input, please enter Y or N')
    return choice
