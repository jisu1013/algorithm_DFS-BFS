import sys
for i in range(1,6):
    sys.stdin = open("in%d.txt" % i,"r")

    N = int(input())
    board = [[0 for _ in range(N+2)] for _ in range(N+2)]
    cnt = 0
    for i in range(1, N+1):
        board[i][1:N+1] = list(map(int, input().split()))
    for i in range(1, N+1):
        for j in range(1, N+1):
            now = board[i][j]
            up = board[i-1][j]
            down = board[i+1][j]
            left = board[i][j-1]
            right = board[i][j+1]
            if now > up and now > down and now > left and now > right:
                cnt += 1
    print(cnt)