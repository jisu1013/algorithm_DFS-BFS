import sys
sys.stdin = open("in5.txt","r")

def reverse(x):
    x_str = str(x)
    tmp = ''
    for i in reversed(x_str):
        tmp += i
    return int(tmp)

def isPrime(x):
    if(x < 2):
        return False
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True

N = int(input())
num_list = map(int, input().split())
result = []
for i in num_list:
    if isPrime(reverse(i)):
        result.append(reverse(i))
print(result)