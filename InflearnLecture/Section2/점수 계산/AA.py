import sys
sys.stdin = open("in5.txt","r")

N = int(input())
num_list = list(map(int, input().split()))
cnt = 0
result = 0
for i in range(N):
    if num_list[i] == 1:
        cnt += 1
        result += cnt
    else:
        cnt = 0

print(result)
