# 30 (실버5)
N_input = list(str(input()))
if '0' not in N_input:
    print(-1)
else:
    N_list = list(map(int, N_input))
    if sum(N_list) % 3 != 0:
        print(-1)
    else:
        N_list.sort(reverse=True)
        N_list_s = list(map(str, N_list))
        result = ''.join(N_list_s)
        print(int(result))
