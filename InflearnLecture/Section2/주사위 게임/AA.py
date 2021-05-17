import sys
sys.stdin = open("in5.txt","r")

def calculate_reward(num_list):
    max_cnt = 1
    for i in num_list:
        if max_cnt < num_list.count(i):
            max_cnt = num_list.count(i)
        if max_cnt == 3:
            return (10000+(i*1000))
        if max_cnt == 2:
            return (1000+(i*100))
    return max(num_list)*100        
    
N = int(input())
max_reward = 0
for i in range(N):
    num_list = list(map(int, input().split()))
    if max_reward < calculate_reward(num_list):
        max_reward = calculate_reward(num_list)
print(max_reward)
