import sys
sys.stdin = open("input.txt","r")
N,K = map(int, input().split())
count = 0

for i in range(1, N+1):
    if N % i == 0: 
        count += 1
        if count == K:
            print(i)
            break
    if count < K and i == N: 
        print(-1)
        break
