import sys
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

graph = {}
graph['src'] = {}
graph['sink'] = {}
n, m = map(int, sys.stdin.readline().split())
for i in range(n):
    graph['src'][i] = 1
    graph[i] = {}
    graph[i]['src'] = 0
for i in range(1,m+1):
    graph['work'+str(i)] = {}
    graph['work'+str(i)]['sink'] = 1
    graph['sink']['work'+str(i)] = 0
for i in range(n):
    tmp = sys.stdin.readline().split()
    for j in range(1,len(tmp)):
        graph[i]['work'+str(tmp[j])] = 1
        graph['work'+str(tmp[j])][i] = 0
print(ford(graph, 'src', 'sink'))