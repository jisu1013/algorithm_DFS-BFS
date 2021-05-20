#잃어버린 괄호
N_input = list(map(str,input().split('-')))
for i in range(len(N_input)):
    if i == 0:
        tmp = list(map(int,N_input[i].split('+')))
        result = sum(tmp)
    else:
        tmp = list(map(int,N_input[i].split('+')))
        result -= sum(tmp)
print(result)
