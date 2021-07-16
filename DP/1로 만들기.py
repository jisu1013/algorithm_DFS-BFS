### 내가 짠 코드
### DP를 활용하지 못했음.
x = int(input())
def cal(x, cnt):
	if x % 5 == 0:
		x = (x // 5)
		cnt += 1
	elif x % 3 == 0:
		x = (x // 3)
		cnt += 1
	elif x % 2 == 0:
		x = (x // 2)
		cnt += 1
	else:
		x -= 1
		cnt += 1
	if x == 1:
		print(cnt)
	else:
		cal(x, cnt)
cal(x, 0)


### DP 코드
### 보텀업 다이나믹 프로그래밍으로 구현
x = int(input())
d = [0] * 30001
for i in range(2, x+1):
	d[i] = d[i - 1] + 1
	if i % 2 == 0:
		d[i] = min(d[i], d[i // 2]+1)
	if i % 3 == 0:
		d[i] = min(d[i], d[i // 3]+1)
	if i % 5 == 0:
		d[i] = min(d[i], d[i // 5]+1)
print(d[x])
