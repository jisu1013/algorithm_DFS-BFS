n,m = map(int,input().split())
print(n,m)
card_list = []
for i in range(n):
  tmp = list(map(int, input().split()))
  tmp = sorted(tmp)
  card_list.append(tmp[0])
card_list = sorted(card_list, reverse=True)
print(card_list[0])
# min, max 함수와 sorted 함수의 시간 복잡도 차이는???
