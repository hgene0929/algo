import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

#입력
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

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
            cost = next[1] + dist
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost,next[0]))
    return distance

results = []
for i in range(1,n+1):
    result = get_shortest_distance(i)
    results.append(result)

#출력
for result in results:
    for i in range(1, n+1):
        if result[i] == INF:
            print(0,end=' ')
        else:
            print(result[i],end=' ')
    print()