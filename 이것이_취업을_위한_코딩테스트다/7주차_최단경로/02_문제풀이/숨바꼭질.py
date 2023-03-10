import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

#입력
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))
distance = [INF] * (n+1)

#풀이
def get_shortest_distance():
    q = []
    heapq.heappush(q, (0,1))
    distance[1] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next in graph[now]:
            cost = dist + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost,next[0]))
    return distance[1:] #0번째는 INF값일 것이기 때문에 제외

#출력
temp = get_shortest_distance()

max_dist = max(temp)
max_idx = temp.index(max_dist)+1 #어차피 max 값이 여러개라면 가장 작은 인덱스를 반환할 것
max_cnt = 0

for i in range(n):
    if temp[i] == max_dist:
        max_cnt += 1

print(max_idx, max_dist, max_cnt)