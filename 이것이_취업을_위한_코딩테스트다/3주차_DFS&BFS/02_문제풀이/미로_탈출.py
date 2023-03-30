'''
[미로 탈출]
- 구해야하는 것: n*m 미로에사 (1,1) -> (n,m) 까지 최단경로
- 아이디어:
    - 그래프다!
        - 퍼져나가는가? DFS
        - 최단경로인가? 다익스트라 => 당첨
        - 선수관계가 있는가? 위상정렬
- 다익스트라 알고리즘으로 최단경로 구한다.
'''
import sys, heapq

input = sys.stdin.readline
INF = int(1e9)
moves = [(-1,0),(1,0),(0,-1),(0,1)]

#풀이
def get_shortest_distance(n,m,graph,distance):
    q = [] #다음 이동할 좌표를 저장해둔 큐
    heapq.heappush(q, (1,0,0)) #큐에 dist(0),시작좌표_r(0),시작좌표_c(0) 담는다
    distance[0][0] = 1
    while q:
        dist,r,c = heapq.heappop(q)
        if distance[r][c] < dist: #이미 방문한 적 있다면
            continue
        for move in moves:
            nr,nc = r+move[0],c+move[1]
            cost = dist+1
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 1: #범위내에 있다면
                if cost < distance[nr][nc]:
                    distance[nr][nc] = cost
                    heapq.heappush(q, (cost,nr,nc))
    return distance[n-1][m-1]

#테스트케이스
n,m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
distance = [[INF]*m for _ in range(n)] #현재 위치까지의 최단 경로를 저장해둘 리스트

print(get_shortest_distance(n,m,graph,distance))