def bfs(graph, src, sink, prev):
    used = []
    queue = []

    queue.append(src)
    
    while queue:
        node = queue.pop(0)
        if node == sink:
            used.append(node)
            return True
        for i in graph[node]:
            if (i in used) == False and graph[node][i]>0:
                queue.append(i)
                used.append(i)
                prev[i] = node
    return False

def ford(graph, src, sink):
    flow = 0
    prev = {}
    for i in graph:
        prev[i] = i
    while bfs(graph, src, sink, prev):
        path_flow = float('inf')
        t = sink
        while t!=src:
            path_flow = min(path_flow, graph[prev[t]][t])
            t = prev[t]
        flow += path_flow

        next_node = sink
        while next_node!=src:
            node = prev[next_node]
            graph[node][next_node] -= path_flow
            graph[next_node][node] += path_flow
            next_node = prev[next_node]
    return flow

n = int(input())
match = {}
graph = {}
graph['src'] = {}
graph['sink'] = {}
for i in range(1,n+1):
    t = str(i)
    graph[t] = {}
    match[i] = []
    big, speed, intel = map(int, input().split())
    graph['src'][t] = 2
    graph[t]['src'] = 0
    match[i].append(big)
    match[i].append(speed)
    match[i].append(intel)
    graph[t+'dst'] = {}

for i in match:
    t = str(i)
    graph[t+'dst']['sink'] = 1
    graph['sink'][t+'dst'] = 0
    for j in match:
        if i != j and match[i][0] >= match[j][0] and match[i][1] >= match[j][1] and match[i][2] >= match[j][2]:
            if match[i][0] == match[j][0] and match[i][1] == match[j][1] and match[i][2] == match[j][2]:
                graph[str(min(i,j))][str(max(i,j))+'dst'] = 1
                graph[str(max(i,j))+'dst'][str(min(i,j))] = 0
            else:
                graph[t][str(j)+'dst'] = 1
                graph[str(j)+'dst'][t] = 0
f = ford(graph, 'src', 'sink')
print(n-f)