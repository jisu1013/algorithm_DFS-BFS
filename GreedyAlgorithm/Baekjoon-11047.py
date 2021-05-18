# 동전 0
N, K = map(int, input().split())
N_list = [0 for _ in range(N)]
for i in range(N):
    N_list[i] = int(input())
N_list.sort(reverse=True)
index = 0
cnt = 1
while K > 0:
    if index > N-1:
        break
    if K - N_list[index] > 0:
        K -= N_list[index]
        cnt += 1        
    elif K - N_list[index] < 0:
        index += 1
    else:
        break
print(cnt)
