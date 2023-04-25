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
            return a+1
    return -1