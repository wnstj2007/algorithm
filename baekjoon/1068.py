import sys
def delete(tree, node):
    for i in tree[node]:
        delete(tree, i)
    del tree[node]

n = int(sys.stdin.readline())
tree = {}
for i in range(n):
    tree[i] = []
nodes = list(map(int, sys.stdin.readline().split()))
for i in range(len(nodes)):
    if nodes[i] == -1:
        continue
    tree[nodes[i]].append(i)
remove = int(sys.stdin.readline())
if nodes[remove] != -1:
    tree[nodes[remove]].remove(remove)
delete(tree, remove)
ans = 0
for i in tree:
    if len(tree[i]) == 0:
        ans += 1
print(ans)