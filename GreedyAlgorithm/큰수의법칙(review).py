N,M,K = map(int, input().split())
num_list = list(map(int, input().split()))
num_list = sorted(num_list, reverse=True)
print(num_list)
result = 0
for i in range(1, M+1):
  if i % (K+1) == 0:
    result += num_list[1]
  else:
    result += num_list[0]
  print(result)
