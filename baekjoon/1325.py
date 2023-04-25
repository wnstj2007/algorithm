def bfs(graph, start):
    used = []
    queue = []

    queue.append(start)

    while queue:
        node = queue.pop(0)
        if node not in used:
            used.append(node)
            queue.extend(graph[node])

    return len(used)

n, m = map(int, input().split())
graph = {}
li = []
ans = []
for i in range(n):
    graph[i+1] = {}
for i in range(m):
    a, b = map(int, input().split())
    graph[b][a] = 1
for i in graph:
    li.append(bfs(graph,i))
t = max(li)
for i in range(len(li)):
    if li[i] == t:
        ans.append(i+1)
print(" ".join(map(str, ans)))