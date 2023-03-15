import sys

input = sys.stdin.readline

#풀이: 크루스칼 활용 -> 최소신장트리 구한다(전체 마을의 최소비용) -> 가장 큰 비용을 제거한다(마을 분할)
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#테스트케이스
n,m = map(int, input().split())
parent = [x for x in range(n+1)]

graph = []
result = 0

for _ in range(m):
    a,b,cost = map(int, input().split())
    graph.append((cost,a,b))

graph.sort()
selected = []

#크루스칼을 통해 최소신장트리 구현
for cost,a,b in graph:
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        selected.append(cost)
        result += cost

#최소신장트리에서 가장 큰 비용이 드는 간선 제거
result -= selected.pop()

print(result)