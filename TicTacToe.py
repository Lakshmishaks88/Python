from automat_player import automat_player
from automater import automater
from check_same import check_same
from choose_other import choose_other
from choose_player import choose_player
from choose_position import choose_position
from display import display
from flipbinary import flip_binary
from game_continue import game_continue
from winner_check import winner_check



def Tictactoe3():
    game = 'Y'
    while game == 'Y':
        p1,p2 = choose_player()
        count = 0
        update = [p1,p2]
        player = ['Player 1','Player 2']
        r = automat_player()
        import random
        p = random.randint(0,1)
        #p = 0
        board = ['#','1','2','3','4','5','6','7','8','9']
        display(board)
        print(f'Player 1 - {p1}, Player 2 - {p2}')
        board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        while count < 9:
            if r and p == 1:
                i = automater(p1,p2,board)
            else:
                i = choose_position()
                while board[i] != ' ':
                    print('Position already entered!!')
                    i = choose_position()
            board[i] = update[p]
            if winner_check(board):
                display(board)
                print(f'Player 1 - {p1}, Player 2 - {p2}')
                print(f"We have a winner : {player[p]}")
                break
            p = flip_binary(p)
            count += 1
            display(board)
            print(f'Player 1 - {p1}, Player 2 - {p2}')
        if count == 9:
            print("Game is draw")
        game = game_continue()
        if game == 'N':
            print('Thank you')

#Ryb the program
Tictactoe3()
