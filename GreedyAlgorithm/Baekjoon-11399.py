# ATM
N =  int(input())
N_list = list(map(int, input().split()))
N_list.sort()
result = 0
for i in range(len(N_list)):
    result += sum(N_list[0:i+1])
print(result)
