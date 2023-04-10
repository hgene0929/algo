'''
구해야하는 것: 주어진 두 사람 간의 촌수 출력
조건:
    - 촌수는 간선 하나당 1촌
    - 노드 들 간의 최소거리가 촌수 -> 연결 리스트를 통해 전체 촌수 구한 다음, 입력받은 두사람 사이의 촌수 구하기(시작 노드는 주어진 촌수) => 다익스트라
'''
import sys,heapq

input = sys.stdin.readline
INF = int(1e9)

#풀이
def solution(start,end,graph,distance):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            cost = dist + 1
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q,(cost,next))
    return distance[end]

#테스트케이스
n = int(input())
people = list(map(int, input().split()))
people.sort()
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
distance = [INF] * (n+1)

result = solution(people[0],people[1],graph,distance)
if result == INF:
    print(-1)
else:
    print(result)