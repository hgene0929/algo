'''
[DFS와 BFS]
- 구해야하는 것 : 주어진 그래프를 각각 DFS, BFS로 탐색한 결과.
- 그래프 나왔다 => 최단경로? 선수관계? 탐색? => 탐색 => 퍼지는거? 빨리가는거? => 둘 다 => DFS & BFS
- DFS : stack 을 사용하여 깊이우선탐색 구현.
- BFS : queue 를 사용하여 너비우선탐색 구현.
- 조건 : 
    - 더이상 탐색할 노드가 없다면 종료.
    - 두개를 동시에 방문할 수 있는 경우, 더 작은 노드부터 방문.
'''
import sys
from collections import deque

input = sys.stdin.readline

#풀이
def dfs(graph,start,n):
    result = []
    visited = [False] * (n+1)
    s = [start]
    while s:
        now = s.pop()
        if not visited[now]:
            result.append(now)
            visited[now] = True
            graph[now].sort(reverse=True)
            for next in graph[now]:
                s.append(next)
    return result


def bfs(graph, start, n):
    result = []
    visited = [False] * (n+1)
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        result.append(now)
        graph[now].sort()
        for next in graph[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True
    return result

#테스트케이스
n,m,start = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    l,r = map(int, input().split())
    graph[l].append(r)
    graph[r].append(l)

res_dfs = dfs(graph, start, n)
res_bfs = bfs(graph, start, n)

for res in res_dfs:
    print(res, end=' ')
print()
for res in res_bfs:
    print(res, end=' ')