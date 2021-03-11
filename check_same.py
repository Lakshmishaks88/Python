def check_same(board,a,b,c):
    A = board[a] == 'X' and board[b] == 'X' and board[c] == 'X'
    B = board[a] == 'O' and board[b] == 'O' and board[c] == 'O'
    return A or B 
