import sys
for i in range(1,6):
    sys.stdin = open("in%d.txt" % i,"r")
    board = [[0 for _ in range(7)] for _ in range(7)]
    for i in range(7):
        board[i] = list(map(int, input().split()))
    #print(board)
    cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][i] == board[i+3][i] and board[i+1][i] == board[i+4][i]:
                cnt += 1
            if board[i][i] == board[i][i+3] and board[i][i+1] == board[i][i+4]:
                cnt += 1
    print(cnt)