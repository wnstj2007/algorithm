def preorder(tree, node):
    result = node
    if tree[node][0] != '.':
        result += preorder(tree, tree[node][0])
    if tree[node][1] != '.':
        result += preorder(tree, tree[node][1])
    return result

def inorder(tree, node):
    result = ''
    if tree[node][0] != '.':
        result += inorder(tree, tree[node][0])
    result += node
    if tree[node][1] != '.':
        result += inorder(tree, tree[node][1])
    return result

def postorder(tree, node):
    result = ''
    if tree[node][0] != '.':
        result += postorder(tree, tree[node][0])
    if tree[node][1] != '.':
        result += postorder(tree, tree[node][1])
    result += node
    return result

import sys

n = int(sys.stdin.readline())
tree = {}
for i in range(n):
    tree[chr(ord('A')+i)] = [[],[]]
for i in range(n):
    root, left, right = map(str, sys.stdin.readline().split())
    tree[root][0] = left
    tree[root][1] = right

print(preorder(tree, 'A'))
print(inorder(tree, 'A'))
print(postorder(tree, 'A'))