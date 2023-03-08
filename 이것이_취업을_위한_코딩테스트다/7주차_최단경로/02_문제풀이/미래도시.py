import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

#입력
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)] #연결된 노드(건물)들을 연결 리스트로 저장 -> 저장값은 (거리,노드)
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append((y,1))
    graph[y].append((x,1))
x,k = map(int, input().split()) #최종목적지, 중간목적지
distance = [INF] * (n+1) #최단거리 테이블 생성

#풀이 : 최단거리(다익스트라)로 1->k 거리와 k->x의 각각 최단거리 합을 구해보자
def get_shortest_distance(start):
    q = []
    heapq.heappush(q, (0,start)) #시작노드 설정
    distance[start] = 0 #최단경로 테이블
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: #방문한 적이 있다면 -> 방문할 필요 X
            continue
        for next in graph[now]: #다음 방문 가능한 회사 살펴보기
            cost = dist + next[1]
            if cost < distance[next[0]]: #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))

get_shortest_distance(1) #1 -> k
first = distance[k]
get_shortest_distance(k) #k -> x
second = distance[x]

#출력
if first == INF or second == INF:
    print(-1)
else:
    print(first+second)