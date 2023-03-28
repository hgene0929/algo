'''
[음료수 얼려 먹기]
- 그래프다 
    - 영역 퍼져나가는가? => DFS => 당첨
    - 최단경로인가? => 다익스트라
    - 선수관계가 있는가? => 위상 정렬
'''
import sys

#풀이
def solution(n,m,graph):
    s = []
    moves = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우로 퍼져나간다
    visited = [[False]*m for _ in range(n)]
    res = 0

    for r in range(n):
        for c in range(m):
            flag = False
            s.append((r,c))
            while s:
                sr,sc = s.pop()
                for move in moves:
                    nr,nc = sr+move[0],sc+move[1]
                    if 0 <= nr < n and 0 <= nc < m: #범위내에 있고
                        if not visited[nr][nc] and graph[nr][nc] == 0: #방문한 적 없는 구멍인 경우
                            visited[nr][nc] = True
                            s.append((nr,nc)) #방문예정처리
                            flag = True
            if flag == True:
                res += 1
    
    return res

#테스트케이스
n,m = map(int, input().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

print(solution(n,m,graph))