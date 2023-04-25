n = int(input())
m = int(input())
graph = {}

for i in range(1,n+1):
    graph[i] = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

tmp = []
for i in graph[1]:
    tmp.append(i)
li = []
for i in tmp:
    li.append(i)
for i in tmp:
    for j in graph[i]:
        if j not in li:
            li.append(j)
print(len(li)-1)
'''
queue = []
visit = []
cnt = 0
tmp = graph[1][len(graph[1])-1]

queue.append(1)
while queue:
    node = queue.pop(0)
    li = sorted(graph[node])
    if node == tmp:
        cnt += 1
        if cnt == 2:
            visit.append(node)
            break
        tmp = li[len(li)-1]
    if node not in visit:
        for i in li:
            queue.append(i)
        visit.append(node)
'''
#print(visit)
#print(li)
#print(len(li)-1)