def bfs(graph, start, end):
    used = []
    queue = []
    prev = {}

    for i in graph:
        prev[i] = 0

    queue.append(start)
    a = -1
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
            a += 1
            break
    return a

n, k, m = map(int, input().split())
graph = {}
for i in range(n):
    graph[i+1] = {}
for i in range(m):
    tmp = list(map(int, input().split()))
    for j in tmp:
        for k in tmp:
            if j != k:
                graph[j][k] = 1
print(bfs(graph, 1, n))