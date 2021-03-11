def choose_position():
    choice = 'k'
    while choice.isdigit() == False or int(choice) not in range(1,10):
        choice = (input('Please choose your next position'))

        if choice.isdigit() == False or int(choice) not in range(1,10):
            print('Invalide input, please enter between 1 and 9')
    return int(choice)
