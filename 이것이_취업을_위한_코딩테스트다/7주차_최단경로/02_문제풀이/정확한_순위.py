'''
[정확한 순위]
- N명의 성적이 있는데, 학생 2명의 성적을 비교한 횟수가 M번이다.
- 비교를 통해 정확히 순위를 알 수 있는 학생을 숫자는?
- 아이디어 : 
    - 정확한 순위를 알려면?? => 해당 학생이 모든 학생으로 이동할 수 있어야 한다? => 최단 거리 테이블의 모든 값이 INF가 아닌 학생???
    - 학생들이 서로 도달할 수 있어야 한다?? => 학생a -> b경로가 있거나, b -> a 경로가 있어야 한다.
'''
import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

#입력
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))

#풀이
def get_shortest_distance(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            cost = dist + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost,next[0]))
    return distance

results = []
temp = [INF,INF,INF,INF,INF,INF,INF]
results.append(temp)

for i in range(1,n+1):
    result = get_shortest_distance(i)
    results.append(result)

cnt = 0
for i in range(n):
    cnt_not_INF = 0
    for j in range(1,n+1):
        if results[i][j] != INF or results[j][i] != INF:
            cnt_not_INF += 1
    if cnt_not_INF == n: #현재 학생이 다른 학생과 모두 도달할 수 있다면
        cnt += 1

#출력
print(cnt)