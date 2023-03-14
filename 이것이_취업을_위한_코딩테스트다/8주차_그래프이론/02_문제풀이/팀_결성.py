import sys

#풀이 : 서로소 집합 알고리즘
def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#테스트케이스
n,m = map(int, input().split())
parent = [x for x in range(n+1)]

results = []

for _ in range(m):
    s,a,b = map(int, input().split())
    if s == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            results.append("YES")
        else:
            results.append("NO")

for result in results:
    print(result)