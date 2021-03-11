def automater(x,y,board):
    s = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    p = [0,0,0,0,0,0,0,0]
    dic = {x:-2,y:4,' ':2}
    i = 0
    while i < len(s):
        for z in s[i]:
            p[i] += dic[board[z]]
        i += 1
    e = 0
    while e < len(s):
        count = 0
        for k in s[e]:
            if board[k] == x:
                count += 1
        if count == 2:
            p[e] = 9
        e += 1
    n = 0
    while n < len(s):
        count = 0
        for k in s[n]:
            if board[k] != ' ':
                count += 1
        if count == 3:
            p[n] = 0
        n += 1

    q = p.index(max(p))
    m = 0
    while m < 3 and board[s[q][m]] != ' ':
        m += 1
    #print(p)
    #print(q,m)
    return s[q][m]
