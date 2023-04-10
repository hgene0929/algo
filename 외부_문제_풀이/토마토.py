'''
구해야하는 것: 상자 안의 토마토가 모두 익는 최소 일수
토마토 보관:
    - M*N*H 크기의 상자 -> M*N 크기의 2차원 배열이 H만큼 쌓인 형태 => array[높이][행][열]
    - 익지 않은 토마토는 퍼뜨려짐 -> 위,아래,상,하,좌,우 => moves = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]
    - 칸마다 보관 종류 -> X, 익음, 안익음 => -1,1,0
'''
import sys
from collections import deque

input = sys.stdin.readline
moves = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]

#입력
m,n,h = map(int, input().split())
graph = [[list(map(int, input().rstrip().split())) for _ in range(n)] for _ in range(h)]
distances = [[[0]*m for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

#풀이
def check():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    return False
    return True

def solution():
    if check():
        return 0
    
    q = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    q.append((0,i,j,k))
                    visited[i][j][k] = True
    
    while q:
        dist,th,tr,tc = q.popleft()
        graph[th][tr][tc] = 1
        for move in moves:
            nh,nr,nc = th+move[0],tr+move[1],tc+move[2]
            cost = dist+1
            if 0 <= nh < h and 0 <= nr < n and 0 <= nc < m and not visited[nh][nr][nc] and graph[nh][nr][nc] == 0:
                distances[nh][nr][nc] = cost
                q.append((cost,nh,nr,nc))
                visited[nh][nr][nc] = True
    
    result = 0
    if not check():
        return -1
    else:
        for i in range(h):
            for j in range(n):
                for k in range(m):
                    result = max(result, distances[i][j][k])
        return result

#출력
print(solution())