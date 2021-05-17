import sys
sys.stdin = open("in5.txt","r")

N = int(input())
#print(N)
num_list = [[0 for _ in range(N)] for _ in range(N)]
result = 0
col_sum = 0
left_dig = 0
right_dig = 0
index = 0

for i in range(N):
    tmp = list(map(int, input().split()))
    num_list[i] = tmp

for i in range(N):
    if sum(num_list[i]) > result:
        #print('in')
        result = sum(num_list[i])
    for j in range(N):
        col_sum += num_list[j][i]
    if col_sum > result:
        #print('in')
        result = col_sum
    col_sum = 0
    left_dig += num_list[i][index]
    right_dig += num_list[i][N-index-1]
    if i == (N-1):
        if left_dig > result:
            #print('in')
            result = left_dig
        if right_dig > result:
            #print('in')
            result = right_dig

print(result)    