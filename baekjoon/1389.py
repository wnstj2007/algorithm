def bfs(graph, start, end):
    used = []
    queue = []
    prev = {}

    for i in graph:
        prev[i] = 0

    queue.append(start)

    while queue:
        node = queue.pop(0)
        if node not in used:
            tmp = graph[node]
            used.append(node)
            for i in tmp:
                if i not in queue and i not in used:
                    prev[i] = node
            queue.extend(tmp)
        if node == end:
            a = 0
            while node != start:
                pre = prev[node]
                a += graph[node][pre]
                node = pre
            break
    return a

n, m = map(int, input().split())
graph = {}
kevin = {}
for i in range(n):
    graph[i+1] = {}
    kevin[i+1] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in graph:
    for j in graph:
        if i != j:
            kevin[i] += bfs(graph, i, j)
            
for i in kevin:
    if kevin[i] == min(kevin.values()):
        print(i)
        break