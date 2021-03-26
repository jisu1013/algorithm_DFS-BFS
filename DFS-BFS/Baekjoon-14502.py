from collections import deque

N, M = map(int, input().split()) #N: column, M: row

dx=[-1,0,1,0]
dy=[0,1,0,-1]
 
graph = [] #inital map list
temp = [[0] * M for _ in range(N)] #map list after making wall

for _ in range(N):
    graph.append(list(map(int,input())))
print(graph)
result = 0

#DFS
def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx >= 0 or ny >= 0 or nx < N or ny < M:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx,ny)

def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score += 1
    return score

#calculate safety zone
def dfs(count):
    global result
    if count == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j]=graph[i][j]
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    virus(i,j)
        result=max(result, get_score())
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)
