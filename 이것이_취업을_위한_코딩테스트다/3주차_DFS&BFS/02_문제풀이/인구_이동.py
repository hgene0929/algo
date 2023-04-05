'''
인구이동규칙:
    - n*n 크기의 땅에서 한칸이 하나의 국가, 각 칸을 나누는 구분선은 국경선, 각 칸의 값은 그 나라의 인구수
    - 하루동안 벌어지는 일:
        - 국경선을 공유하는 두 나라의 인구차이가 L <= 인구차이 <= R 일 경우, 하루동안 국경선 연다
        - 연합 이룸 = (연합의 인구수) // (연합을 이루고 있는 칸의 개수)
        - 국경선 닫는다
=> 최종적으로 인구 이동이 며칠 동안 벌어지는지 출력
아이디어:
    - 결국 상하좌우로 퍼져나가는것 -> 더이상 인구차이가 L <= 인구차이 <= R인 칸이 없을 때까지 퍼트린다
    => DFS 반복문이 끝날 때까지 한 라운드 수 cnt += 1
'''
import sys

input = sys.stdin.readline
moves = [(-1,0),(1,0),(0,-1),(0,1)]

#풀이
def solution(n,left,right,board):
    result = 0
    while True:
        s = []
        visited = [[False]*n for _ in range(n)]
        is_possible = False
        #1.연합조건 충족하는 국가 뽑아내기
        for r in range(n):
            for c in range(n):
                united = []
                population = 0
                if not visited[r][c]:
                    s.append((r,c))
                    visited[r][c] = True
                    #2.연합만들기
                    while s:
                        sr,sc = s.pop()
                        united.append((sr,sc))
                        population += board[sr][sc]
                        for move in moves:
                            nr,nc = sr+move[0],sc+move[1]
                            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and left <= abs(board[nr][nc]-board[sr][sc]) <= right:
                                s.append((nr,nc))
                                visited[nr][nc] = True
                                is_possible = True
                    #3.인구이동시키기
                    for ur,uc in united:
                        p = population // len(united)
                        board[ur][uc] = p
        #4.더이상 연합만들 수 없다면 리턴
        if not is_possible:
            return result
        result += 1
                    


#테스트케이스
n,left,right = map(int, input().split())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]

print(solution(n,left,right,board))