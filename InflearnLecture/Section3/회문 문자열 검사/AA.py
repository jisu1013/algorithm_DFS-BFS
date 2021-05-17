import sys
sys.stdin = open("in5.txt","r")

def checkvoc(x):
    check = True
    tmp = list(x)
    for i in range(len(tmp)):
        if tmp[i].lower() != tmp[len(tmp)-1-i].lower():
            check = False
    return check

N = int(input())
voc = []
for i in range(N):
    voc.append(str(input()))
for i in range(N):
    if checkvoc(voc[i]):
        print('#',i+1,' YES')
    else:
        print('#',i+1,' NO')