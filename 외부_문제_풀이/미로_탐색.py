'''
구해야하는 것: n*m 크기의 미로에서 이동할 수 있는 칸(1)으로만 이동했을 때, (1,1) -> (n,m)까지의 최단거리
이동 규칙:
    - 이동가능한 칸(1)으로만 이동가능 -> 가기전에 확인 조건에 추가
    - 인접한 칸(상하좌우)로만 이동가능 -> moves = [(-1,0),(1,0),(0,-1),(0,1)]
아이디어: 최단거리 => 다익스트라
'''
import sys,heapq

input = sys.stdin.readline
INF = int(1e9)
moves = [(-1,0),(1,0),(0,-1),(0,1)]

#풀이
def solution(n,m,graph,distance):
    q = []
    heapq.heappush(q,(1,0,0)) #칸을 셀 때에는 시작 위치와 도착 위치도 포함한다 => 시작거리 = 1, 시작행 = 0, 시작열 = 0
    distance[0][0] = 1
    while q:
        dist,r,c = heapq.heappop(q)
        if distance[r][c] < dist:
            continue
        for move in moves:
            nr,nc = r+move[0],c+move[1]
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 1: #이동가능한 칸(1)으로만 이동가능 => 해당 좌표의 값이 1인지 확인
                cost = dist+1 #가는데 소요되는 거리 = 1
                if cost < distance[nr][nc]: #최단거리 발견하면 => 거리갱신
                    distance[nr][nc] = cost
                    heapq.heappush(q,(cost,nr,nc))
    return distance[n-1][m-1] #조건은 1,1 좌표부터 시작이니까 -= 1씩 해준 위치

#테스트케이스
n,m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
distance = [[INF]*m for _ in range(n)]

print(solution(n,m,graph,distance))