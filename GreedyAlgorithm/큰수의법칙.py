N,M,K=list(map(int,input().split()))
print(N,M,K)
num_list = list(map(int,input().split()))
print(num_list)
num_list.sort(reverse=True)
print(num_list)
result = 0
cnt = 0
index = 0
for i in range(M):
  if cnt == K:
    cnt = 0
    if index == 0:
      index += 1
  elif index == 1:
    index -= 1 
    cnt = 0 
  result += num_list[index]
  cnt += 1
  print(i,result)
print(result)
