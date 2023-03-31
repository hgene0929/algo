'''
[연구소]
- 구해야하는 것: n*m의 연구소에 벽을 3개 세우고 난 후, 안전영역의 최댓값 => 퍼져나간다 => DFS
- 아이디어:
    - 벽을 3개 세울 수 있는 경우: 0인 칸 중 3개를 선택하는 조합 => itertools.combinations() 사용할 것.
    - 3개의 벽을 세울 수 있는 모든 경우의 수에 대해 dfs를 통해 안전영역을 구한 후, min() 값을 구할 것 => DFS를 활용한 구현(완전탐색).
'''
import sys
from itertools import combinations

input = sys.stdin.readline

#입력
n,m = map(int, input().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

#풀이
#(1) 연구소 중  빈칸의 좌표 따로 담기
empty = []
for r in range(n):
    for c in range(m):
        if graph[r][c] == 0:
            empty.append((r,c))

#(2) 빈칸 중 3개를 뽑아내는 경우의 수를 리스트로 담기
cases = list(combinations(empty,3))
moves = [(-1,0),(1,0),(0,-1),(0,1)]
result = []

#(3) 완전탐색
for case in cases:
    #가벽설치
    temp = [[0]*m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            temp[r][c] = graph[r][c]
    for r,c in case:
        temp[r][c] = 1

    #바이러스 퍼뜨리기
    s = []
    visited = [[False]*m for _ in range(n)]
    for tr in range(n):
        for tc in range(m):
            if temp[tr][tc] == 2:
                s.append((tr,tc))
                visited[tr][tc] = True
                while s:
                    r,c = s.pop()
                    temp[r][c] = 2
                    for move in moves:
                        nr,nc = r+move[0],c+move[1]
                        if 0 <= nr < n and 0 <= nc < m:
                            if not visited[nr][nc] and temp[nr][nc] == 0:
                                s.append((nr,nc))
                                visited[nr][nc] = True
    
    #안전영역 구하기
    cnt_safe = 0
    for r in range(n):
        for c in range(m):
            if temp[r][c] == 0:
                cnt_safe += 1
    result.append(cnt_safe)

#출력
print(max(result))