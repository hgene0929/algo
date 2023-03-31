'''
[특정 거리의 도시 찾기]
- 구해야하는 것: 최단거리가 K인 도시의 번호 오름차순 => 최단경로 => 다익스트라
- 주어진 값:
    - n개의 노드(도시), m개의 간선(도로 - 단방향), 모든 간선 거리 = 1 
'''
import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

#풀이
def solution(graph, distance, k, x):
    #다익스트라 알고리즘으로 각 노드(도시)별 최단거리 구하기
    q = []
    heapq.heappush(q, (0,x))
    distance[x] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            cost = dist + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost,next[0]))

    #각 노드(도시)별 최단거리가 담긴 리스트의 1~n까지의 인덱스의 원소 중 k와 값이 같은 인덱스를 오름차순
    result = []
    for idx,dist in enumerate(distance):
        if idx != 0 and dist == k:
            result.append(idx)
    result.sort()
    
    return result

#테스트케이스
n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    c1,c2 = map(int, input().split())
    graph[c1].append((c2,1)) #c2는 도착도시, 1은 모든 간선의 거리
distance = [INF] * (n+1)

results = solution(graph, distance, k, x)
if len(results) == 0:
    print(-1)
else:
    for result in results:
        print(result)