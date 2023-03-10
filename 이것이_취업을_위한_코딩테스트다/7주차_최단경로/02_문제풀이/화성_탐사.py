import sys, heapq

input = sys.stdin.readline
INF = int(1e9)

#풀이 : 다익스트라 알고리즘을 이용한 최단 경로 -> 상하좌우로 움직임을 고려
moves = [(-1,0),(1,0),(0,-1),(0,1)]

def get_shortest_distance(graph, distance, n):
    q = []
    heapq.heappush(q, (graph[0][0],0,0))
    distance[0][0] = graph[0][0]
    while q:
        dist,x,y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for move in moves:
            if 0 <= x+move[0] < n and 0 <= y+move[1] < n:
                nx,ny = x+move[0],y+move[1]
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost,nx,ny))
    return distance[n-1][n-1]


#테스트케이스
t = int(input())
results = []
for _ in range(t):
    n = int(input())
    graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
    distance = [[INF]*n for _ in range(n)]
    results.append(get_shortest_distance(graph, distance, n))
for result in results:
    print(result)