#흙길 보수
N,L = map(int, input().split())
water = []
pos = 0
result = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    water.append(tmp)
water = sorted(water)
for i in range(N):
    cnt = 0
    pos = max(water[i][0], pos)
    diff = water[i][1] - pos
    cnt = (diff+L-1) // L
    #print(cnt)
    result += cnt
    pos += cnt * L
    #print(pos)
print(result)
