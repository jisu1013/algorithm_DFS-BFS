import sys
sys.stdin = open("in2.txt","r")

N = int(input())
num_list = [0]*(N+1)
cnt = 0
for i in range(2, N+1):
    if num_list[i] == 0:
        cnt += 1
        for j in range(i, N+1, i):
            num_list[j] = 1

print(cnt)
