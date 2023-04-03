'''
[경쟁적 전염]
- 구해야하는 것: n*n 시험관에 1~K 종류의 바이러스가 1초에 차례대로 상하좌우로 전염될 때, s초 후의 (x,y)에 존재하는 바이러스 종류 출력.
- 아이디어: 그래프에서 퍼져나간다 => DFS?! -> 안됨 -> 왜냐하면 퍼저나가는데 우선순위가 있으므로.. queue 사용할 것 => BFS 
    - 일단 종류별로 순서대로 현재 위치에서 상하좌우로 퍼뜨린다 -> s초만큼.. => 큐에 누적시키자 시간은!
'''
import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int, input().split())
graph = []
viruses = []
visited = [[False]*n for _ in range(n)]
for r in range(n):
    datas = list(map(int, input().split()))
    graph.append(datas)
    for c in range(n):
        if datas[c] != 0:
            viruses.append((datas[c],0,r,c)) #q에 (바이러스종류,경과시간,행,열) 삽입
            visited[r][c] = True
s,x,y = map(int, input().split())

viruses.sort() #바이러스 종류 오름차순으로 전염된다
q = deque(viruses)
moves = [(-1,0),(1,0),(0,-1),(0,1)]

while q:
    virus,second,r,c = q.popleft()
    if second > s: #s초 후의 결과를 봐야한다
        break
    graph[r][c] = virus
    for move in moves:
        nr,nc = r+move[0],c+move[1]
        if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] == 0 and not visited[nr][nc]:
            q.append((virus,second+1,nr,nc))
            visited[nr][nc] = True

print(graph[x-1][y-1])