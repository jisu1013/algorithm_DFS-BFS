def balanced_index(p):
    count=0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if i == (len(p)-1):
            return i
        if count == 0:
            return i

def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def soulution(p):
    answer = ''
    if p == '':
        return answer    
    index = balanced_index(p)
    if index == None:
        return answer
    u=p[:index+1]
    v=p[index+1:]
    #if "correct", return function(v)
    if check_proper(u):
        answer=u+soulution(v)
    #if not "correct"
    else:
        answer = '('
        answer += soulution(v)
        answer += ')'
        u=list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] == ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

graph = list(input())
result = soulution(graph)

print(result)