#주유소
N = int(input())
N_list = list(map(int, input().split()))
price = list(map(int, input().split()))
result = price[0] * N_list[0]
min_price = price[0]
for i in range(1, N - 1):
	min_price = min(price[i], min_price)
	result += (min_price * N_list[i])
print(result)
