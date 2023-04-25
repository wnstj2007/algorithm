import sys
import heapq
def dijkstra(graph, start, end):
    queue = []
    visit = []
    dist = {}

n, m = map(int, sys.stdin.readline())
graph = {}
for i in range(1,n+1):
    graph[i] = {}
for i in range(m):
    a, b, c, d = map(int, sys.stdin.readline())
    graph[a][b] = c
    graph[b][a] = d
print(graph)