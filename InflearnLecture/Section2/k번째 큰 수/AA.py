import sys
import itertools
sys.stdin = open("in5.txt","r")

N, K = map(int, input().split())
nums = input().split()
nPr = list(itertools.permutations(nums, 3))
tmp = []
for i in range(len(nPr)):
    if (int(nPr[i][0]) + int(nPr[i][1]) + int(nPr[i][2])) in tmp:
        continue
    else:
        tmp.append(int(nPr[i][0]) + int(nPr[i][1]) + int(nPr[i][2]))
tmp.sort(reverse=True)
print(tmp[K-1])
