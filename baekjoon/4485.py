import heapq
import sys
def dijkstra(graph, start, end):
    distance = {}
    queue = []
    for i in graph:
        if i == start:
            distance[i] = 0
        else:
            distance[i] = float('inf')
    queue.append(start)
    node = start
    while queue:
        if node == start:
            queue.remove(start)
        for i in graph[node]:
            n = distance[node]+graph[node][i]
            if distance[i] > n:
                distance[i] = n
                heapq.heappush(queue, (distance[i], i))
        node = heapq.heappop(queue)[1]
    return distance[end]

test = 1
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    name = [['W' for i in range(n+2)]]
    for i in range(n):
        name.append(['W']+sys.stdin.readline().split()+['W'])
    name.append(['W' for i in range(n+2)])
    result = int(name[1][1])
    graph = {}
    for i in range(1,n+1):
        for j in range(1,n+1):
            node = name[i][j]
            t = str(i)+" "+str(j)
            graph[t] = {}

    for i in range(1,n+1):
        for j in range(1,n+1):
            if name[i][j] == 'W':
                continue
            down = name[i+1][j]
            right = name[i][j+1]
            up = name[i-1][j]
            left = name[i][j-1]
            t = str(i)+" "+str(j)
            if up == 'W':
                pass
            else:
                graph[t][str(i-1)+" "+str(j)] = int(up)
            if down == 'W':
                pass
            else:
                graph[t][str(i+1)+" "+str(j)] = int(down)
            if left == 'W':
                pass
            else:
                graph[t][str(i)+" "+str(j-1)] = int(left)
            if right == 'W':
                pass
            else:
                graph[t][str(i)+" "+str(j+1)] = int(right)
    result += dijkstra(graph, '1 1', str(n)+' '+str(n))
    print('Problem {}: {}'.format(test, result))
    test += 1