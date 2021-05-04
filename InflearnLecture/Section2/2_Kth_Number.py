import sys
sys.stdin = open("in5.txt","r")

T = int(input())
for i in range(T):
    N, s, e, k = map(int, input().split())
    nums = input().split()
    #print(nums)
    for j in range(N):
        nums[j] = int(nums[j])
    tmp = nums[s-1:e]
    tmp.sort()
    print('#',i+1,' ',tmp[k-1])    
