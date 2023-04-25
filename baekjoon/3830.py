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
                a -= graph[node][pre]
                node = pre
            return a
    return 'UNKNOWN'

ans = []
while True:
    n, m = map(int, input().split())
    if n==0 and m==0:
        break
    graph = {}
    for i in range(n):
        graph[i+1] = {}
    for i in range(m):
        tmp = input().split()
        q = tmp.pop(0)
        if q == '!':
            a, b, w = map(int, tmp)
            graph[a][b] = w
            graph[b][a] = -w
        elif q == '?':
            a, b = map(int, tmp)
            ans.append(bfs(graph, a, b))
for i in ans:
    print(i)

'''
2 2
! 1 2 1
? 1 2
2 2
! 1 2 1
? 2 1
4 7
! 1 2 100
? 2 3
! 2 3 100
? 2 3
? 1 3
! 4 3 150
? 4 1
0 0
'''