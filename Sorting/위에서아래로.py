N = int(input())
num_list = []
for i in range(N):
  num_list.append(int(input()))
num_list.sort(reverse=True)
for i in num_list:
  print(num_list[i], end=' ')
