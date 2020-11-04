#freezing drink

N, M = map(int, input().split()) #N : row, M: column 
ice_count = 0

ice_tool = [] 
for i in range(N):
    ice_tool.append(list(map(int,input())))
    #print(ice_tool[i])

def dfs(x,y):    
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if ice_tool[x][y] == 0:
        ice_tool[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False
 
ice_count = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            ice_count += 1

print(ice_count)