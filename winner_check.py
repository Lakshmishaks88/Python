from check_same import check_same

def winner_check(board):
    return check_same(board,1,4,7) or check_same(board,2,5,8) or check_same(board,3,6,9) or check_same(board,7,8,9) or check_same(board,4,5,6) or check_same(board,1,2,3) or check_same(board,1,5,9) or check_same(board,3,5,7)
