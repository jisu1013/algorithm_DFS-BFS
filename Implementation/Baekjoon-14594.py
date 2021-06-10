#동방프로젝트(small)
N = int(input())
M = int(input())
wall = [1 for _ in range(1, N)]
for i in range(M):
    input_ = list(map(int,input().split()))
    tmp = [i-1 for i in range(input_[0],input_[1])]
    for j in tmp:
        wall[j] = 0
print(wall.count(1)+1)
