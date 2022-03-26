import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b
        
n,m = map(int, input().split())

ans = 0
edges = []
for i in range(m):
    x,y,z = map(int, input().split())
    edges.append((x,y,z))
    ans += z

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

edges.sort()
for edge in edges:
    a,b,cost = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        ans -= cost

print(ans)
