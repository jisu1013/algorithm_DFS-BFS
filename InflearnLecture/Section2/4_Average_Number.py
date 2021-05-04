import sys
sys.stdin = open("in4.txt","r")

N = int(input())
nums = [int(i) for i in input().split()]
avg = round(sum(nums) / N)
min_num = nums[0]
min_student = 0
for i in range(N):
    if (abs(nums[i] - avg) < abs(min_num - avg)):
        min_num = nums[i]
        min_student = i
        #print(min_num , i)
    elif abs(nums[i] - avg) == abs(min_num - avg):
        min_student = min(min_student, i)

print(avg, min_student+1)

