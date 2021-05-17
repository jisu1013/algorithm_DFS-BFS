import sys
sys.stdin = open("in1.txt","r")

N = int(input())
N_list = list(map(int, input().split()))
M =  int(input())
M_list = list(map(int, input().split()))

sum_list = N_list + M_list
#list에서 중복 제거
sum_list = list(set(sum_list))
sum_list.sort()
print(sum_list)