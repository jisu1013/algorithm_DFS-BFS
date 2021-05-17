import sys
sys.stdin = open("in5.txt","r")

N, M = map(int, input().split())
sum_list = []
for i in range(1, N+1):
    for j in range(1, M+1):
        sum_list.append(i+j)
sum_list.sort()
max_cnt = 0
for i in range(len(sum_list)):
    if max_cnt < sum_list.count(sum_list[i]):
        max_cnt = sum_list.count(sum_list[i])
result = []

for i in range(len(sum_list)):
    if max_cnt == sum_list.count(sum_list[i]):
        if sum_list[i] not in result:
            result.append(sum_list[i])
            max_cnt = sum_list.count(sum_list[i])
          
print(result)
