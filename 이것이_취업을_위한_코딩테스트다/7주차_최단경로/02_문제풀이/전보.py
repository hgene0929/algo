import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

#입력
n,m,c = map(int, input().split())
graph = [[] for _ in range(n+1)] #연결된 도시간의 거리를 저장할 연결 리스트
for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z)) #x -> y 까지 통로가 있고, c만큼 거리이다
distance = [INF] * (n+1) #최단 거리 테이블

#풀이 : 다익스트라 알고리즘 활용 -> 결과는 c -> 모든 노드 중 가장 멀리있는 노드와의 최단거리와 거리 테이블의 값이 INF가 아닌 도시의 개수
def get_shortest_distance(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: #이미 방문한 적있다면 -> 최단거리 결정남 -> 건너뛴다
            continue
        for next in graph[now]: #현재 방문 중인 노드와 연결된 다른 노드들을 모두 살펴본다
            cost = dist + next[1]
            if cost < distance[next[0]]: #더 짧은 노드가 발견되면 -> 탐색할 노드 변경
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

get_shortest_distance(c)

max_distance = 0
cnt = 0
for d in distance:
    if d != INF:
        max_distance = max(max_distance, d)
        cnt += 1

#출력
print(cnt-1, max_distance)