from collections import deque

N, M, K, X = map(int, input().split()) #N : num of city, M: num of road, K: distance, X: city number 

graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

distance = [-1]*(N+1)
distance[X] = 0

queue = deque([X])
while queue:
    now = queue.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

check=False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check=True

if check==False:
    print(-1)
