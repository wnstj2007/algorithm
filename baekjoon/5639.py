import sys
tree = {}
root = 0
def insert(node):
    tree[node] = []
    if len(tree) == 1:
        root = node
        node = root
    else:
        pass
while True:
    node = int(sys.stdin.readline())
    insert(node)