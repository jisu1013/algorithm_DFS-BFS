import sys
sys.stdin = open("in5.txt","r")

def digit_sum(x):
    tmp = str(x)
    sum_tmp = 0
    for i in range(len(tmp)):
        sum_tmp += int(tmp[i])
    return sum_tmp

N = int(input())
num_list = map(int, input().split())
max_num = []
max_cnt = 0
tmp_num = []
for i in num_list:
    tmp_num.append(i)
    if max_cnt < digit_sum(i):
        max_cnt = digit_sum(i)
for i in tmp_num:
    if max_cnt == digit_sum(i):
        print(i)
        break