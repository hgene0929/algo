'''
구해야하는 것: 주어진 시작점에서 다른 모든 정점으로의 최단 경로
아이디어: 최단 경로 & no 선수관계 => 다익스트라
'''
import sys,heapq

input = sys.stdin.readline
INF = int(1e9)

#풀이
def solution(start,graph,distance):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            cost = dist+next[1]
            if distance[next[0]] > cost:
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))
    return distance[1:]

#테스트케이스
v,e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    sv,ev,w = map(int, input().split())
    graph[sv].append((ev,w))
distance = [INF]*(v+1)

results = solution(k,graph,distance)
for result in results:
    if result == INF:
        print('INF')
    else:
        print(result)