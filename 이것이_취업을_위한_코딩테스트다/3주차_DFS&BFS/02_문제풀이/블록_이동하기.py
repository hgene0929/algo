'''
이동 => moves[(-1,0),(1,0),(0,-1),(0,1)]
회전: [(r1,c1), (r2,c2)]
    - 가로 to 세로:
        - 왼쪽 기준으로 => (r1,c1)는 그대로 유지
            - 아래로 회전 => (r2,c2) -> (r1+1,c1)
            - 위로 회전 => (r2,c2) -> (r1-1,c1)
        - 오른쪽 기준으로 => (r2,c2)는 그대로 유지
            - 아래로 회전 => (r1,c1) -> (r2+1,c2)
            - 위로 회전 => (r1,c1) -> (r2-1,c2)
    - 세로 to 가로:
        - 위쪽 기준으로 => (r1,c1)는 그대로 유지
            - 왼쪽으로 회전 => (r2,c2) -> (r1,c1-1)
            - 오른쪽으로 회전 => (r2,c2) -> (r1,c1+1)
        - 아래쪽 기준으로 => (r2,c2)는 그대로 유지
            - 왼쪽으로 회전 => (r1,c1) -> (r2,c2-1)
            - 오른쪽으로 회전 => (r1,c1) -> (r2,c2+1)
제약조건:
    - 범위를 벗어난 경우 => if 0 <= nr < 가로길이 and 0 <= nc < 세로길이
    - 이동할 칸이 1이 아닌 경우 => if graph[nr][nc] == 0
구해야하는 것: (1,1) 에서 (N,N)까지 이동하는 최소시간 => 최단거리 => 다익스트라
'''
from collections import deque

def get_next_cases(n,robot,board):
    cases = []
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    #사용할 데이터 추출 및 변환
    r = list(robot)
    r1,c1,r2,c2 = r[0][0],r[0][1],r[1][0],r[1][1]
    #이동 - 상하좌우
    for move in moves:
        nr1,nc1,nr2,nc2 = r1+move[0],c1+move[1],r2+move[0],c2+move[1]
        if 0 <= nr1 < n and 0 <= nc1 < n and 0 <= nr2 < n and 0 <= nc2 < n: #범위 확인
            if board[nr1][nc1] == 0 and board[nr2][nc2] == 0: #벽인지 확인
                cases.append({(nr1,nc1),(nr2,nc2)})
    #회전 - 키포인트는 현재 집합 자료형이기 때문에 순서가 무관하다 => 즉, 모두 회전가능할 때 한꺼번에 회전시킨다!
    if r1 == r2:
        if r1+1 < n and r2+1 < n and board[r1+1][c1] == 0 and board[r2+1][c2] == 0: #수평에서 수직 아래로 회전(범위, 벽인지 확인)
            cases.append({(r1+1,c1),(r1,c1)})
            cases.append({(r2+1,c2),(r2,c2)})
        elif r1-1 >= 0 and r2-1 >= 0 and board[r1-1][c1] == 0 and board[r2-1][c2] == 0: #수평에서 수직 위로 회전(범위, 벽인지 확인)
            cases.append({(r1-1,c1),(r1,c1)})
            cases.append({(r2-1,c2),(r2,c2)})
    else:
        if c1+1 < n and c2+1 < n and board[r1][c1+1] == 0 and board[r2][c2+1] == 0: #수직에서 수평 오른쪽으로 회전(범위, 벽인지 확인)
            cases.append({(r1,c1+1),(r1,c1)})
            cases.append({(r2,c2+1),(r2,c2)})
        elif c1-1 >= 0 and c2-1 >= 0 and board[r1][c1-1] == 0 and board[r2][c2-1] == 0: #수직에서 수평 왼쪽으로 회전(범위, 벽인지 확인)
            cases.append({(r1,c1-1),(r1,c1)})
            cases.append({(r2,c2-1),(r2,c2)})
    return cases

def get_shortest_distance(n,board,start):
    #초기화
    visited = []
    q = deque()
    q.append((0,start))
    visited.append(start)
    #탐색
    while q:
        time,robot = q.popleft()
        if (n-1,n-1) in robot: #도착지점에 도달하면 경과시간 반환
            return time
        cases = get_next_cases(n,robot,board)
        for case in cases:
            if case not in visited: #방문여부 확인
                q.append((time+1,case))
                visited.append(case)
    

def solution(board):
    n = len(board)
    start = {(0,0),(0,1)} #키: 집합자료형으로 로봇의 좌표를 저장해 순서무관하도록 한다!
    return get_shortest_distance(n,board,start)