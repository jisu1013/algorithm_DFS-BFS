#거스름돈
rest = (1000 - int(input()))
cnt = 0
while rest > 0:
  if rest > 500 or rest == 500:
    rest -= 500
    cnt += 1
    #print(500)
  elif rest > 100 or rest == 100:
    rest -= 100
    cnt += 1
    #print(100)
  elif rest > 50 or rest == 50:
    rest -= 50
    cnt += 1
    #print(50)
  elif rest > 10 or rest == 10:
    rest -= 10
    cnt += 1
    #print(10)
  elif rest > 5 or rest == 5:
    rest -= 5
    cnt += 1
  else:
    rest -= 1
    cnt += 1
print(cnt)
