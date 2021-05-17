import sys
sys.stdin = open("in5.txt","r")

card_list = [i for i in range(1,21)]

for i in range(10):
    nums = list(map(int, input().split()))
    nums[0] -= 1
    tmp = card_list[nums[0]:nums[1]]
    tmp.reverse()
    card_list[nums[0]:nums[1]] = tmp

print(card_list)
