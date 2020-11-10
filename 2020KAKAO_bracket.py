graph = list(input())
graph = graph[1:-1]

print(graph)
print(len(graph))

u=[]
v=[]
answer=[]
tmp=['(']

def dfs(v_):
    if not v_:
        return []
    u_,v_ = seperateGraph(v_)
    if(checkRight(u_)):
        u.append(u_)
        dfs(v_)
    else:
        tmp.append(v_)
        dfs(v_)

#format
def solution(p):
    u,v = seperateGraph(p)
    print(u)
    print(v)
    if(checkRight(u)):
        if not dfs(v):
            answer=u.append(v)
    else:
        if not dfs(v):
            tmp.append(')')
            u=reverseBracket(u)
            if not v:
                answer=u
            else:    
                answer=u.append(v)    
    return answer

def printAnswer(graph):
    result=''
    answer.append(solution(graph))
    result=result+'"'
    for i in range(0,len(answer)):
        result=result+str(answer[i])
    result=result+'"'
    print(result)

def checkBalance(graph):
    count=0
    for i in graph:
        if(i == '('):
            count+=1
        elif(i == ')'):
            count-=1
    if(count==0):
        return True
    else:
        return False

def checkRight(graph):
    count=0
    before=[]
    for i in range(0,len(graph)):
        if(i == 0):
            before.append(graph[0])
        elif(i == '('):
            before.append(graph[i])
        elif(i == ')'):
            before.pop(graph[i])
    if not before:
        return True
    else:
        return False

def ifGraphEmpty(graph):
    graph.append('"')
    graph.append('"')
    return graph

def seperateGraph(graph):
    u=[]
    v=[]
    for i in range(0,len(graph)):
        if graph == []:
            break
        elif(checkBalance(graph[0:(i+1)])):
            u=graph[0:(i+1)]
            #print("u:",u)
            if(i == len(graph)-1):
                v=[]
            else:
                v=graph[i:]
            break
    return u,v

def reverseBracket(temp):
    for i in range(0,len(temp)):
        if(temp[i] == '('):
            temp[i] == ')'
        elif(temp[i] == ')'):
            temp[i] == '('


printAnswer(graph)
