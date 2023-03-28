'''
[뱀]
- 구해야하는 것: 뱀 도스 게임에서 게임종료 시간
- 게임 규칙:
    - N*N 보드 위에서 뱀 움직임 => 원래 위치하던 칸 마지막 pop + 현재 방향으로 1칸
    - 사과 먹으면 한칸 늘어남 => 원래 위치하던 칸 + 현재 방향으로 1칸
    - 방향회전: D 오른쪽으로 90도, L 왼쪽으로 90도
- 시뮬레이션으로 풀면될듯..
    - direction: 현재 바라보는 방향 (R,D,L,U) => D라면 (방향 인덱스 + 1)%4, L이라면 (방향 인덱스 - 1)%4
    - queue: 현재 뱀의 몸통이 위치하고 있는 칸들의 좌표 
             => 사과 있는 곳으로 이동하면 queue.append((nr,nc)), 사과 없는 곳으로 이동하면 queue.popleft() and queue.append((nr,nc))
'''
from collections import deque
import sys

input = sys.stdin.readline

#입력
n = int(input())
k = int(input())

board = [[0]*(n+1) for _ in range(n+1)] #(n+1)*(n+1) 크기의 보드 생성 -> 뱀이 움직일 수 있는 범위는 1 ~ n 뿐
for _ in range(k): #보드에 사과 배치
    ar,ac = map(int, input().split())
    board[ar][ac] = 1

l = int(input())
direction_change = [tuple(map(str, input().rstrip().split())) for _ in range(l)]

directions = [(0,1),(1,0),(0,-1),(-1,0)]
q = deque() #뱀이 위치한 좌표들을 저장한 큐

d,r,c = 0,1,1 #현재 방향의 인덱스,현재 행번호,현재 열번호
board[r][c] = 2
q.append((r,c))
time = 0 #게임경과 시간

#풀이
while True:
    time += 1

    nr,nc = r+directions[d][0],c+directions[d][1] #다음번에 이동할 위치
    if 0 < nr <= n and 0 < nc <= n and board[nr][nc] != 2: #보드판을 벗어나거나 뱀의 몸통을 물면 => 게임종료
        r,c = nr,nc
        if board[r][c] == 1: #다음 이동할 위치에 사과가 있다면 => 앞으로 += 1, 없다면 => 앞으로 += 1 꼬리 -= 1
            q.append((r,c))
            board[r][c] = 2
        else:
            pr,pc = q.popleft()
            q.append((r,c))
            board[pr][pc] = 0
            board[r][c] = 2
    else:
        break

    for t,dir in direction_change:
        if int(t) == time: #방향을 회전할 타이밍이라면
            if dir == 'L':
                d = (d-1)%4
            else:
                d = (d+1)%4

#출력
print(time)