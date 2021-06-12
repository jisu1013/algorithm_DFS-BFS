from collections import deque
import sys

n = int(input())
k = int(input())
input = sys.stdin.readline
student_list = list(map(int, input().split()))
photo = deque([0] * (n))
recommend = deque([0] * (n))

for student in student_list:
  min_rec = []
  full = True
  for i in range(n):
    if photo[i] == 0:
      full = False
    if len(min_rec) == 0:
      min_rec.append(i)
    elif recommend[i] < recommend[min_rec[0]] or recommend[i] == recommend[min_rec[0]]:
      min_rec.append(i)
  if full:
    if student in list(photo):
      index = list(photo).index(student)
      recommend[index] += 1
    else:
      photo.remove(photo[min_rec[0]])
      recommend.remove(recommend[min_rec[0]])
      photo.append(student)
      recommend.append(1)
  else:
    photo.popleft()
    recommend.popleft()
    photo.append(student)
    recommend.append(1)

result = sorted(list(photo))
for i in range(len(result)):
  if i == len(result)-1:
    print(result[i], end='\n')
  else:
    print(result[i], end=' ')
