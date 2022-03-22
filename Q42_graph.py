import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

g = int(input())
p = int(input())
data = []
for i in range(p):
    data.append(int(input()))
    
parent = [0] * (g+1)
for i in range(1,g+1):
    parent[i] = i

ans = 0
for i in range(p):
    root = find_parent(parent,data[i])
    if root == 0:
        break
    union_parent(parent, root, root-1)
    ans += 1

print(ans)
