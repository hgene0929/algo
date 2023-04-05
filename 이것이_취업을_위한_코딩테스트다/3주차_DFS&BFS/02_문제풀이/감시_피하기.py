import sys
from itertools import combinations

input = sys.stdin.readline
moves = [(-1,0),(1,0),(0,-1),(0,1)]

#풀이
def solution(x,board,teachers,empties):
    cases = list(combinations(empties,3))

    for case in cases:
        is_possible = True
        s = []
        #벽설치
        for cr,cc in case:
            board[cr][cc] = 'O'
        #핵심로직: 선생님 감시 퍼트리기 => 초기에는 상하좌우로 퍼트리기 시작, 이후부터는 이전의 감시방향을 유지하면서 퍼져나가야 한다
        for tr,tc in teachers:
            for d in range(4):
                s.append((tr,tc,d))
        while s:
            tr,tc,td = s.pop()
            nr,nc = tr+moves[td][0],tc+moves[td][1]
            if 0 <= nr < n and 0 <= nc < n:
                if board[nr][nc] == 'X':
                    s.append((nr,nc,td))
                elif board[nr][nc] == 'S':
                    is_possible = False
                    break
        #현재 경우의 수에서 감시피할 수 있다면 리턴 YES
        if is_possible:
            return 'YES'
        #다른 경우의 수 확인해보기 전에 벽설치한거 원복
        for cr,cc in case:
            board[cr][cc] = 'X'
    #모든 경우의 수 살펴봤는데, 감시 피할 수 없음
    return 'NO'

#테스트케이스
n = int(input())
board = [list(map(str, input().rstrip().split())) for _ in range(n)]

teachers = []
empties = []
for r in range(n):
    for c in range(n):
        if board[r][c] == 'T':
            teachers.append((r,c))
        elif board[r][c] == 'X':
            empties.append((r,c))

print(solution(n,board,teachers,empties))