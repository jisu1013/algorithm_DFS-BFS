import sys

for i in range(1,6):
    sys.stdin = open("in%d.txt" % i,"r")
    board = [[0 for _ in range(9)] for _ in range(9)]
    check_list = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        board[i] = list(map(int, input().split()))
    check = True
    for i in range(9):    
        tmp = board[i]
        if sorted(tmp) != check_list:
            check = False        
        if i % 3 == 0:
            for j in [0,3,6]:
                box = board[j : j+3]
                sum_ = box[0][i : i+3] + box[1][i : i+3] + box[2][i : i+3]
                tmp = sorted(sum_)                
                if tmp != check_list:
                    check = False
    if check:
        print("YES")
    else:
        print("NO")
        


