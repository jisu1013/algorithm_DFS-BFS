import sys
sys.stdin = open("in1.txt","r")

N = int(input())
num_list = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input().split()))
    num_list[i] = tmp
M = int(input())
rotation_order = []
result = 0
for i in range(M):
    rotation_order.append(list(map(int, input().split())))
for i in range(M):
    tmp = [0 for _ in range(N)]
    if rotation_order[i][1] == 0:        
        for j in range(N):
            if j+rotation_order[i][2]-1 < N:
                tmp[j+rotation_order[i][2]-1] = num_list[rotation_order[i][0]][j]
            else:
                tmp[j+rotation_order[i][2]-1-(N+1)] = num_list[rotation_order[i][0]][j]
    else:
        for j in range(N):
            if j-rotation_order[i][2] < 0:
                tmp[j-rotation_order[i][2]+N] = num_list[rotation_order[i][0]][j]
            else:
                tmp[j-rotation_order[i][2]] = num_list[rotation_order[i][0]][j]
    num_list[rotation_order[i][0]] = tmp
    #print(tmp)
line = int((N-1)/2)
index = 0
for i in range(line, -1, -1):
    result += sum(num_list[index][line-i:line+i+1])
    index += 1
for i in range(1,line+1):
    result += sum(num_list[index][line-i:line+i+1])
    index += 1
print(result)
print(tmp)
print(num_list)